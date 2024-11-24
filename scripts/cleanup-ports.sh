#!/bin/bash

# Define ports to clean
PORTS=(7071 4280)

# Function to kill processes on a port
kill_port() {
    local port=$1
    echo "Checking port $port..."
    
    # Find PIDs using the port
    pids=$(lsof -ti :$port)
    
    if [ ! -z "$pids" ]; then
        echo "Found processes on port $port. PIDs: $pids"
        echo "Killing processes..."
        kill -9 $pids
        echo "Processes on port $port killed"
    else
        echo "No processes found on port $port"
    fi
}

# Clean each port
for port in "${PORTS[@]}"; do
    kill_port $port
done

echo "Cleanup complete!"