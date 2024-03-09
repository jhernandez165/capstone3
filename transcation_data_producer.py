#!/usr/bin/env python3
import requests
import os
from faker import Faker
import random

# Initialize Faker
faker = Faker()

# Predefined descriptions for each transaction type
transaction_descriptions = {
    "DEPOSIT": ["Deposit to savings account", "Monthly savings deposit", "Initial deposit"],
    "WITHDRAWAL": ["ATM cash withdrawal", "Online purchase refund", "Withdrawal for rent payment"],
    "TRANSFER": ["Transfer to checking account", "Payment to friend", "Rent payment"],
    "PURCHASE": ["Online purchase", "Grocery shopping", "Restaurant bill"]
}

# Configuration
BASE_URL = 'http://localhost:8072'
bear_token = os.getenv('BEARER_TOKEN')
TRANSACTION_ENDPOINT = f"{BASE_URL}/transactions"
HEADERS = {'Authorization': f'{bear_token}'}


def create_transaction(account_number, transaction_type, amount):
    """Create a transaction with a predefined description and merchant details."""
    description = random.choice(transaction_descriptions[transaction_type.upper()])
    
    transaction_data = {
        "type": transaction_type.upper(),
        "method": "ACH",
        "date": faker.date_time_between(start_date="-30d", end_date="now").isoformat(),
        "amount": amount,
        "merchantCode": faker.bothify(text='??#####'),
        "merchantName": faker.company(),
        "description": description,
        "accountNumber": account_number,
        "hold": False  
    }

    response = requests.post(TRANSACTION_ENDPOINT, json=transaction_data, headers=HEADERS)
    if response.status_code in [200, 201]:
        print("Transaction processed successfully:", response.json())
    else:
        print(f"Failed to process transaction. Status code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    account_number = input("Enter the account number for the transaction: ")
    transaction_type = input("Enter the transaction type (DEPOSIT, WITHDRAWAL, TRANSFER, PURCHASE): ")
    amount = int(input("Enter the amount for the transaction: "))

    create_transaction(account_number, transaction_type, amount)
