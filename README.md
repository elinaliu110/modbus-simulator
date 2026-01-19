# modbus-simulator
A practical development and testing toolset designed to simulate a Modbus TCP Server. This project is specifically optimized for testing IoT Edge modules, and DataHub integrations.

## Key Features
Modbus TCP Simulation: Fully functional simulation of a Modbus server.
Containerized: Includes a Dockerfile for easy deployment in containerized environments.
Cloud Ready: Pre-configured Kubernetes YAML files for K8s clusters.
Lightweight: Minimal dependencies, focused on performance and reliability.

## Getting Started
1. Prerequisites
Python 3.x

Docker (Optional, for containerized execution)

Kubernetes (Optional, for orchestration)

2. Local Setup
Clone the repository and install the required dependencies (assuming pymodbus is used):

Bash

pip install pymodbus
python MODBUS_TCP_Server_v22_IoTEdge.py
3. Docker Deployment
To run the simulator as a background service using Docker:

Bash

# Build the image
docker build -t modbus-simulator -f docker.Dockerfile .

# Run the container (Mapping default Modbus port 502)
docker run -d -p 502:502 --name modbus-server modbus-simulator
☸️ Kubernetes Orchestration
For large-scale testing or integration with Azure IoT Edge, use the provided manifest files:

Bash

# Deploy the simulator
kubectl apply -f modbus-sim-iothub-deployment.yaml

# Expose the service
kubectl apply -f modbus-sim-iothub-service.yaml
