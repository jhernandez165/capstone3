#!/bin/bash

# Function to start a microservice
start_microservice() {
  # $1 = port to be assigned to the microservice
  # $2 = path to the JAR file to run
  echo "Starting microservice on port $1..."
  
  java -jar "$2" --server.port="$1" &
  
  # Gives time for the service to start up before starting the next one.
  sleep 18
}

# Start each microservice with the correct port and path to the JAR file
# Make sure the path to the JAR files is correct

start_microservice 8071 "/Users/jonathanhernandez/capstone_project_smoothstack/aline-underwriter-microservice/underwriter-microservice/target/underwriter-microservice-0.1.0.jar"
start_microservice 8070 "/Users/jonathanhernandez/capstone_project_smoothstack/aline-user-microservice/user-microservice/target/user-microservice-0.1.0.jar"
start_microservice 8073 "/Users/jonathanhernandez/capstone_project_smoothstack/aline-bank-microservice/bank-microservice/target/bank-microservice-0.1.0.jar"
start_microservice 8074 "/Users/jonathanhernandez/capstone_project_smoothstack/aline-account-microservice/account-microservice/target/account-microservice-0.1.0.jar"
start_microservice 8072 "/Users/jonathanhernandez/capstone_project_smoothstack/aline-transaction-microservice/transaction-microservice/target/transaction-microservice-0.1.0.jar"
start_microservice 8080 "/Users/jonathanhernandez/capstone_project_smoothstack/aline-gateway/target/aline-gateway-0.0.1-SNAPSHOT.jar"

# Wait for all services to start
wait
