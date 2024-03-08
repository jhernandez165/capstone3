#!/usr/bin/env python3
import requests

# Endpoint for authentication
auth_url = 'http://localhost:8080/authenticate'  # Example URL, replace with actual

# Assuming the API expects a JSON body with the secret key
data = {
    'secretKey': 'ThisIsAGreatSecretKey!!!'
}

# Make the authentication request
response = requests.post(auth_url, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Extract the token from the response
    token = response.json().get('token')
    print("Token obtained:", token)
else:
    print("Failed to authenticate. Status code:", response.status_code, "Response:", response.text)
