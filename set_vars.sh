#!/bin/bash

# Database configuration
export DB_USERNAME=root
export DB_PASSWORD=12345678
export DB_HOST=localhost
export DB_PORT=3306
export DB_NAME=aline-financial

# Service configuration
export APP_SERVICE_HOST=http://localhost

# JWT secret keys
export APP_USER_ACCESS_KEY=ThisIsAGreatSecretKey!!!
export APP_LOAN_ACCESS_KEY=ThisIsAGreatSecretKey!!!
export APP_USER_SECRET_KEY=ThisIsAGreatSecretKey!!!

# Portal configuration
export PORTAL_LANDING=http://localhost:3000
export PORTAL_DASHBOARD=http://localhost:4200
export PORTAL_ADMIN=http://localhost:8080

# Gateway specific vars
export GATEWAY_PORT=8080
export USER_MICROSERVICE_PORT=8070
export UNDERWRITER_MICROSERVICE_PORT=8071
export ACCOUNT_MICROSERVICE_PORT=8074
export BANK_MICROSERVICE_PORT=8073
export TRANSACTION_MICROSERVICE_PORT=8072

# Encryption key for sensitive data
export ENCRYPT_SECRET_KEY=ThisIsAGreatSecretKey!!!

# JWT Secret for token generation and validation
export JWT_SECRET_KEY="eyJhbGciOiJIUzIlNiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMONTY30DkwIiwibmFtZSI6IkpvaG4gRG91liwiaWF0IjoxNTE2MjM5MDIyfQ.Sf1KxwRJSMeKKF2QT4fwpMeJf36P0k6yJV_adQssw5c"
