#!/usr/bin/env python3

"""

This script uses the Faker library to generate fake data for a new application.
The generated data is then sent to a specified endpoint using the requests library.

Modules:
    requests: Used to send HTTP requests.
    faker: Used to generate fake data for the application.
"""

import requests
from faker import Faker

faker = Faker()

# Configuration
BASE_URL = 'http://localhost:8071'
APPLICATION_ENDPOINT = f"{BASE_URL}/applications"
HEADERS = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbmlzdHJhdG9yIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTcwNzY5NTYyNSwiZXhwIjoxNzA4OTA1MjI1fQ.ebVLchXN7ixbo5BXBGMzNvhCXhRqKj3F9RvlE6MrbnY'}

def generate_application_data():
    """Generate fake data for a new application."""
    applicant = {
        "firstName": faker.first_name(),
        "middleName": faker.first_name(),
        "lastName": faker.last_name(),
        "dateOfBirth": str(faker.date_of_birth(minimum_age=18, maximum_age=65)),
        "gender": faker.random_element(elements=('MALE', 'FEMALE', 'OTHER')),
        "email": faker.email(),
        "phone": faker.numerify('(###) ###-####'),
        "socialSecurity": faker.ssn(),
        "driversLicense": faker.bothify(text='?###??##', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
        "income": faker.random_int(min=15000000, max=30000000),
        "address": faker.street_address(),
        "city": faker.city(),
        "state": faker.state_abbr(),
        "zipcode": faker.zipcode(),
        "mailingAddress": faker.street_address(),
        "mailingCity": faker.city(),
        "mailingState": faker.state_abbr(),
        "mailingZipcode": faker.zipcode()
    }

    application_data = {
        "applicationType": faker.random_element(elements=('CHECKING', 'SAVINGS', 'LOAN')),
        "noNewApplicants": False,
        "applicantIds": [],
        "applicants": [applicant],
        "applicationAmount": 0,
        "cardOfferId": 0,
        "depositAccountNumber": ""
    }

    return application_data

def submit_application(application_data):
    """Submit the application data to the underwriter microservice."""
    response = requests.post(APPLICATION_ENDPOINT, json=application_data,
                             headers=HEADERS, timeout=10)
    if response.status_code == 201:
        application_response = response.json()
        print("Application submitted successfully:", application_response)
        # Check if the application was approved and return True if so
        return application_response.get('status') == 'APPROVED'
    
    return False


def main():
    """
    Main function that orchestrates the process of generating and submitting application data.

    This function generates application data by calling the `generate_application_data` function.
    The generated data is then submitted by calling the `submit_application` function.
    If a response is received, it is printed to the console.
    """
    total_applications = int(input("Enter the number of applications to submit: "))
    approved_applications = 0

    for _ in range(total_applications):
        application_data = generate_application_data()
        if submit_application(application_data):
            approved_applications += 1

    print(f"\n\n\nApproved {approved_applications} out of {total_applications} applications.")

if __name__ == "__main__":
    main()
