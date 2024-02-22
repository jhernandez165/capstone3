#!/bin/bash

# Define an array of service ports your microservices use
declare -a service_ports=(8070 8071 8072 8080 8074 8073 8090)

# Function to kill a process given its port
kill_service_on_port() {
    local port=$1
    echo "Attempting to stop service on port $port..."

    # Find the process ID (PID) using the port
    local pid=$(lsof -t -i:$port)

    # If a process is found, kill it
    if [ ! -z "$pid" ]; then
        echo "Service found on port $port with PID $pid. Stopping it now..."
        kill -9 $pid
        echo "Service on port $port stopped."
    else
        echo "No service found on port $port."
    fi
}

# Iterate over the service ports and attempt to stop services on each
for port in "${service_ports[@]}"
do
    kill_service_on_port $port
done
