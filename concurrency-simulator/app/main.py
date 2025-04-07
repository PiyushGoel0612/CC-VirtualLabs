from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import Dict, Optional
import threading
import uuid
from enum import Enum

app = FastAPI()

class SimulationStatus(str, Enum):
    READY = "ready"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETED = "completed"

class SimulationType(str, Enum):
    PRODUCER_CONSUMER = "producer_consumer"
    READERS_WRITERS = "readers_writers"

simulations: Dict[str, "BaseSimulation"] = {}

class BaseSimulation:
    def __init__(self, sim_type: SimulationType):
        self.sim_type = sim_type
        self.status = SimulationStatus.READY
        self.log = []
        self.threads = []
    
    def start(self):
        self.status = SimulationStatus.RUNNING
    
    def pause(self):
        self.status = SimulationStatus.PAUSED
    
    def resume(self):
        self.status = SimulationStatus.RUNNING
    
    def stop(self):
        self.status = SimulationStatus.COMPLETED
        for thread in self.threads:
            thread.join(timeout=1.0)
    
    def get_state(self):
        return {"type": self.sim_type, "status": self.status, "log": self.log[-20:]}

class ProducerConsumerSimulation(BaseSimulation):
    def __init__(self, buffer_size: int = 5):
        super().__init__(SimulationType.PRODUCER_CONSUMER)
        self.buffer = []
        self.buffer_size = buffer_size
        self.lock = threading.Lock()

    def producer(self):
        while self.status == SimulationStatus.RUNNING:
            with self.lock:
                if len(self.buffer) < self.buffer_size:
                    self.buffer.append("Item")
                    self.log.append("Produced an item")
            threading.Event().wait(1)

    def consumer(self):
        while self.status == SimulationStatus.RUNNING:
            with self.lock:
                if self.buffer:
                    self.buffer.pop(0)
                    self.log.append("Consumed an item")
            threading.Event().wait(1)
    
    def start(self):
        super().start()
        self.threads = [threading.Thread(target=self.producer), threading.Thread(target=self.consumer)]
        for t in self.threads:
            t.start()

class CreateSimulationRequest(BaseModel):
    sim_type: SimulationType
    buffer_size: Optional[int] = 5

@app.post("/simulations/")
def create_simulation(request: CreateSimulationRequest):
    sim_id = str(uuid.uuid4())
    if request.sim_type == SimulationType.PRODUCER_CONSUMER:
        simulations[sim_id] = ProducerConsumerSimulation(request.buffer_size)
    return {"sim_id": sim_id, "status": simulations[sim_id].status}

@app.get("/simulations/")
def list_simulations():
    return {"simulations": list(simulations.keys())}

@app.post("/simulations/{sim_id}/start")
def start_simulation(sim_id: str):
    if sim_id not in simulations:
        raise HTTPException(status_code=404, detail="Simulation not found")
    simulations[sim_id].start()
    return {"status": simulations[sim_id].status}

@app.post("/simulations/{sim_id}/pause")
def pause_simulation(sim_id: str):
    if sim_id not in simulations:
        raise HTTPException(status_code=404, detail="Simulation not found")
    simulations[sim_id].pause()
    return {"status": simulations[sim_id].status}

@app.post("/simulations/{sim_id}/resume")
def resume_simulation(sim_id: str):
    if sim_id not in simulations:
        raise HTTPException(status_code=404, detail="Simulation not found")
    simulations[sim_id].resume()
    return {"status": simulations[sim_id].status}

@app.post("/simulations/{sim_id}/stop")
def stop_simulation(sim_id: str):
    if sim_id not in simulations:
        raise HTTPException(status_code=404, detail="Simulation not found")
    simulations[sim_id].stop()
    return {"status": simulations[sim_id].status}

@app.get("/simulations/{sim_id}/status")
def get_simulation_status(sim_id: str):
    if sim_id not in simulations:
        raise HTTPException(status_code=404, detail="Simulation not found")
    return simulations[sim_id].get_state()
