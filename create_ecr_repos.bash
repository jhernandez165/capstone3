#!/bin/bash

# Define AWS region
region="us-east-1"

# List of your service names
declare -a services=("landing-portal" "member-dashboard" "admin-portal" "bank-service" "gateway" "user-service" "transaction-service" "underwriter-service" "account-service")

# Loop through all service names and create an ECR repository for each
for service in "${services[@]}"; do
  repository_name="jh-$service"
  echo "Creating repository: $repository_name"

  # Execute the AWS CLI command to create the repository
  aws ecr create-repository --repository-name "$repository_name" --region $region --image-scanning-configuration scanOnPush=true --image-tag-mutability IMMUTABLE

  # Check the exit status of the AWS CLI command
  if [ $? -eq 0 ]; then
    echo "Repository '$repository_name' created successfully."
  else
    echo "Failed to create repository '$repository_name'."
  fi
done
¡