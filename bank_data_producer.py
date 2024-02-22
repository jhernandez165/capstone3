#!/usr/bin/env python3
"""
bank_data_producer.py

This script uses the requests library to interact with a banking API.

Modules:
    requests: Used to send HTTP requests to the banking API.
"""

import requests
from faker import Faker

# Initialize Faker
faker = Faker()

# Configuration
BASE_URL = 'http://localhost:8073'
HEADERS = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbmlzdHJhdG9yIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTcwNzY5NTYyNSwiZXhwIjoxNzA4OTA1MjI1fQ.ebVLchXN7ixbo5BXBGMzNvhCXhRqKj3F9RvlE6MrbnY'}

def create_bank():
    """Create a dummy bank."""
    bank_data = {
        "routingNumber": faker.bothify(text='#########'),
        "address": faker.street_address(),
        "city": faker.city(),
        "state": faker.state_abbr(),
        "zipcode": faker.zipcode()
    }
    response = requests.post(f"{BASE_URL}/banks", json=bank_data, headers=HEADERS, timeout=10)
    if response.status_code == 201:
        print("Bank created successfully:", response.json())
        return response.json()['id']
    print("Failed to create bank. Status code:", response.status_code, "Response:", response.text)
    return None

def create_branch(bank_id):
    """Create a dummy branch for a given bank ID."""
    if bank_id is None:
        print("Bank ID is None. Skipping branch creation.")
        return
    branch_data = {
        "name": faker.company(),
        "address": faker.street_address(),
        "city": faker.city(),
        "state": faker.state_abbr(),
        "zipcode": faker.zipcode(),
        "phone": faker.phone_number(),
        "bankID": bank_id
    }
    response = requests.post(f"{BASE_URL}/branches", json=branch_data, headers=HEADERS, timeout=10)
    if response.status_code == 201:
        print("Branch created successfully:", response.json())
    else:
        print("Failed to create branch. Status code:", response.status_code, "Response:", response.text)

def main():
    """
    Main function to create banks and branches based on user input.
    """
    # Ask the user for the number of banks and branches per bank to create
    num_banks = int(input("Enter the number of banks to create: "))
    branches_per_bank = int(input("Enter the number of branches per bank to create: "))

    for _ in range(num_banks):
        bank_id = create_bank()
        for _ in range(branches_per_bank):
            create_branch(bank_id)

if __name__ == "__main__":
    main()
