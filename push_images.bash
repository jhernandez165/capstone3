#!/bin/bash

# Define AWS account and region details
AWS_ACCOUNT_ID="992382630898"
AWS_REGION="us-east-1"
ECR_URI="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com"

# List of your service names - ensure these match your local Docker image names or adjust accordingly
declare -a services=("landing-portal" "member-dashboard" "admin-portal" "bank-service" "gateway" "user-service" "transaction-service" "underwriter-service" "account-service")

# Loop through all service names, tag, and push each Docker image
for service in "${services[@]}"; do
  # Tag your Docker image with the ECR repository URI
  echo "Tagging image for $service..."
  docker tag "direstbounty/capstone:$service" "$ECR_URI/jh-$service:latest"
  
  # Push the image to ECR
  echo "Pushing $service to ECR..."
  docker push "$ECR_URI/jh-$service:latest"
done

echo "All images have been pushed to ECR."
