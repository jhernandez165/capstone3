#!/bin/bash

# To end all running microservices, CTRL C and delete the shell instance.

start_microservice() {
    # $1 = port to be assigned to the microservice yaml at runtime
    export APP_PORT=$1
    # $2 = jar file to run (found in microservice readme)
    java -jar $2 &
    # gives time for each service to start up before swapping ports to start next service
    sleep 18
}

# Gateway Microservice
start_microservice 8080 "aline-gateway/target/aline-gateway-0.0.1-SNAPSHOT.jar --server.port=8090"

# Underwriter Microservice
start_microservice 8071 "aline-underwriter-microservice/underwriter-microservice/target/underwriter-microservice-0.1.0.jar" 

# User Microservice
start_microservice 8070 "aline-user-microservice/user-microservice/target/user-microservice-0.1.0.jar" 

# Bank Microservice
start_microservice 8073 "aline-bank-microservice/bank-microservice/target/bank-microservice-0.1.0.jar" 

# Account Microservice
start_microservice 8074 "aline-account-microservice/account-microservice/target/account-microservice-0.1.0.jar" 

# Transaction Microservice
start_microservice 8072 "aline-transaction-microservice/transaction-microservice/target/transaction-microservice-0.1.0.jar" 
