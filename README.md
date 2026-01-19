# modbus-simulator
A practical development and testing toolset designed to simulate a Modbus TCP Server. This project is specifically optimized for testing IoT Edge modules, and DataHub integrations.

## Key Features
* **Modbus TCP Simulation**: Fully functional simulation of a Modbus server.
* **Containerized**: Includes a `Dockerfile` for easy deployment in containerized environments.
* **Cloud Ready**: Pre-configured Kubernetes YAML files for Azure IoT Hub or local K8s clusters.
* **Lightweight**: Minimal dependencies, focused on performance and reliability.

## Getting Started

### 1. Prerequisites
* Python 3.x
* modbus-tk
* numpy
* Docker (Optional, for containerized execution)
* Kubernetes (Optional, for orchestration)

### 2. Local Setup
```bash
# Installation
pip install modbus-tk numpy
```
```bash
# Run the simulator (Default Modbus port 502)
python MODBUS_TCP_Server_v22_IoTEdge.py
```
### 3. Run with Docker
To run the simulator using Docker:
```bash
# Build the image
docker build -t modbus-simulator -f docker.Dockerfile .

# Run the container
docker run -d -p 502:502 --name modbus-server modbus-simulator
```

### 4. Deploy to Kubernetes
Apply deployment:
```bash
# Deploy the simulator
kubectl apply -f modbus-sim-iothub-deployment.yaml

# Expose the service
kubectl apply -f modbus-sim-iothub-service.yaml
```
Check status:
```bash
# List all running pods
kubectl get pods

# Get service details for modbus-sim-iothub
kubectl get svc modbus-sim-iothub
```
