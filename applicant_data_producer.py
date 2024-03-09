#!/usr/bin/env python3
import os
import requests
from faker import Faker

# Initialize Faker
faker = Faker()

# Configuration
bear_token = os.getenv('BEARER_TOKEN')
BASE_URL = 'http://localhost:8071'
APPLICANTS_ENDPOINT = f"{BASE_URL}/applicants"
HEADERS = {'Authorization': f'{bear_token}'}


# Your JWT token (ensure to replace with a valid token if needed)
jwt_token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbmlzdHJhdG9yIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTcwNzY5NTYyNSwiZXhwIjoxNzA4OTA1MjI1fQ.ebVLchXN7ixbo5BXBGMzNvhCXhRqKj3F9RvlE6MrbnY"

def generate_applicant_data():
    """Generate fake data for a new applicant."""
    return {
        "firstName": faker.first_name(),
        "middleName": faker.first_name(),
        "lastName": faker.last_name(),
        "dateOfBirth": str(faker.date_of_birth(minimum_age=18, maximum_age=65)),
        "gender": faker.random_element(elements=('MALE', 'FEMALE', 'OTHER')),
        "email": faker.email(),
        "phone": faker.numerify('(###) ###-####'),
        "socialSecurity": faker.ssn(),
        "driversLicense": faker.bothify(text='?###??##', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
        "income": faker.random_int(min=10000, max=100000),
        "address": faker.street_address(),
        "city": faker.city(),
        "state": faker.state_abbr(),
        "zipcode": faker.zipcode(),
        "mailingAddress": faker.street_address(),
        "mailingCity": faker.city(),
        "mailingState": faker.state_abbr(),
        "mailingZipcode": faker.zipcode()
    }

def create_applicant():
    applicant_data = generate_applicant_data()
    
    headers = {
        'Authorization': f'Bearer {jwt_token}'
    }

    response = requests.post(APPLICANTS_ENDPOINT, json=applicant_data, headers=headers, timeout=10)

    if response.status_code == 201:
        print(f"Applicant created successfully: {response.json()}")
    else:
        print(f"Failed to create applicant. Status code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    create_applicant()
