#!/usr/bin/env python3
import requests
from faker import Faker

# Initialize Faker
fake = Faker()

# Base URL of your User microservice API
BASE_URL = 'http://localhost:8070'

def create_admin_user():
    """
    Create an admin user.

    This function generates user data using the Faker library and assigns the admin role.
    """
    user_data = {
        "username": fake.user_name(),
        "password": "Password123!",
        "role": "admin",
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "phone": fake.numerify(text='(###) ###-####'),
        "enabled": True,
    }

    # API endpoint for user registration
    registration_endpoint = f"{BASE_URL}/users/registration"

    # Make a POST request to the user registration endpoint
    response = requests.post(registration_endpoint, json=user_data, timeout=10)

    # Check if the request was successful
    if response.status_code == 201:
        print(f"Admin user {user_data['username']} registered successfully.")
    else:
        print(f"Failed to register admin user {user_data['username']}. Status code: {response.status_code}, Response: {response.text}")

def main():
    """
    Main function to create a specified number of admin users.

    This function prompts the user to enter the number of admin users to create.
    It then calls the `create_admin_user` function that many times to create the admin users.

    """
    num_admins = int(input("Enter the number of admin users to create: "))
    for _ in range(num_admins):
        create_admin_user()

if __name__ == "__main__":
    main()
