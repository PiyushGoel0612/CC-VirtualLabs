# OS Simulation APIs

This repository contains a collection of FastAPI-based REST APIs that simulate various operating system concepts. These simulations are designed for educational purposes to help students understand fundamental OS concepts through practical examples.

## Table of Contents

- [Concurrency Simulator](#concurrency-simulator)
  - [Producer-Consumer Problem](#producer-consumer-problem)
  - [Dining Philosophers Problem](#dining-philosophers-problem)
- [Deadlock Simulator](#deadlock-simulator)
- [File System Simulator](#file-system-simulator)
- [API Documentation](#api-documentation)

## Concurrency Simulator

The Concurrency Simulator demonstrates classic concurrency problems in operating systems.

### Producer-Consumer Problem

Simulates a shared buffer with multiple producers and consumers, demonstrating synchronization mechanisms to handle resource sharing.

**Features:**
- Configurable buffer size
- Adjustable producer and consumer speeds
- Real-time monitoring of buffer states
- Pause/resume functionality to observe the system at different stages

### Dining Philosophers Problem

Simulates the classic synchronization problem where multiple philosophers alternate between thinking and eating, but must acquire shared forks to eat.

**Features:**
- Configurable number of philosophers
- Adjustable thinking and eating times
- Deadlock prevention with asymmetric resource acquisition
- Real-time status monitoring of each philosopher

## Deadlock Simulator

A comprehensive simulator for demonstrating resource allocation and deadlock scenarios in operating systems.

**Features:**
- Create processes and resources
- Request and release resources
- Deadlock detection using wait-for graph method
- Visualization of system state and resource allocation
- Real-time tracking of blocked processes

## File System Simulator

Simulates a hierarchical file system with concurrent access control mechanisms.

**Features:**
- Create, read, write, and delete files
- Create and list directories
- File locking mechanism for concurrent access control
- Track file metadata (creation time, modification time, size)
- Hierarchical directory structure

## API Documentation

Once the servers are running, you can access the auto-generated Swagger UI documentation at:

- Concurrency Simulator: http://localhost:8000/docs
- Deadlock Simulator: http://localhost:8001/docs  
- File System Simulator: http://localhost:8002/docs

### Concurrency Simulator Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/simulations/` | POST | Create a new simulation (Producer-Consumer or Dining Philosophers) |
| `/simulations/` | GET | List all running simulations |
| `/simulations/{sim_id}/start` | POST | Start a simulation |
| `/simulations/{sim_id}/pause` | POST | Pause a running simulation |
| `/simulations/{sim_id}/resume` | POST | Resume a paused simulation |
| `/simulations/{sim_id}/stop` | POST | Stop a simulation |
| `/simulations/{sim_id}/status` | GET | Get the current status of a simulation |

### Deadlock Simulator Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/processes/` | POST | Create a new process |
| `/processes/` | GET | List all processes |
| `/processes/{process_id}` | GET | Get details of a specific process |
| `/resources/` | POST | Create a new resource |
| `/resources/` | GET | List all resources |
| `/resources/{resource_id}` | GET | Get details of a specific resource |
| `/processes/{process_id}/request` | POST | Request resource allocation |
| `/processes/{process_id}/release` | POST | Release allocated resources |
| `/detect` | GET | Run deadlock detection |
| `/status` | GET | Get the current system state |
| `/reset` | POST | Reset the simulator |

### File System Simulator Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/files/` | POST | Create a new file |
| `/files/{file_id}` | GET | Read a file |
| `/files/{file_id}` | PUT | Write to a file |
| `/files/{file_id}` | DELETE | Delete a file |
| `/files/{file_id}/lock` | POST | Lock a file |
| `/files/{file_id}/unlock` | POST | Unlock a file |
| `/directories/` | POST | Create a new directory |
| `/directories/{dir_path}` | GET | List directory contents |

## Use Cases

These simulators can be used to:

1. **Educational Purposes:**
   - Demonstrate OS concepts in operating systems courses
   - Allow students to interact with and observe complex OS mechanisms

2. **Algorithm Analysis:**
   - Compare different resource allocation strategies
   - Study deadlock prevention and detection techniques

3. **Debugging Practice:**
   - Introduce concurrency bugs and challenge students to fix them
   - Simulate race conditions and synchronization issues
