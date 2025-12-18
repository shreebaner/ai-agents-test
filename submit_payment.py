import requests
import json
from decimal import Decimal

# Define custom rules as helper functions
def is_amount_valid(amount):
    """Rule: Amount must be greater than $0.50."""
    return amount > Decimal('0.50')

def is_currency_supported(currency):
    """Rule: Only EUR, USD, and GBP are supported."""
    supported_currencies = ['EUR', 'USD', 'GBP']
    return currency in supported_currencies

def submit_payment(card_number: str, expiration_date: str, amount: Decimal, currency: str, api_url: str):
    """
    Submits a payment request to an API endpoint after validating against business rules.
    """
    # 1. Apply business rules
    if not is_amount_valid(amount):
        return {"status": "failed", "error": f"Invalid amount: {amount} is below the minimum threshold."}
    
    if not is_currency_supported(currency):
        return {"status": "failed", "error": f"Invalid currency: {currency} not supported."}
    
    # In a real-world scenario, you would also use client-side libraries
    # (like Stripe Elements) to securely collect card information and 
    # generate a 'nonce' or 'token' to avoid handling raw card details 
    # on your server.
    
    # 2. Prepare the payload for the API
    payload = {
        "amount": str(amount),
        "currency": currency,
        "payment_method": {
            "type": "card",
            "fields": {
                "number": card_number,
                "expiration_date": expiration_date
                # CVV and other details would typically be handled via a secure tokenization process
            }
        }
    }
    
    # 3. Simulate the API request (using a mock function here)
    # In a real application, you would use requests.post()
    print(f"Attempting to process payment of {currency} {amount}...")
    try:
        # response = requests.post(api_url, json=payload, timeout=10)
        # response.raise_for_status() # Raise an exception for bad status codes

        # Mock API response for demonstration
        if api_url == "https://api.example.com/pay":
            return {"status": "success", "transaction_id": "tx_12345abc"}
        else:
            return {"status": "failed", "error": "Invalid API endpoint"}

    except requests.exceptions.RequestException as e:
        # Handle connection errors or API issues
        return {"status": "error", "error": str(e)}

# --- Example Usage ---
# Use Decimal for accurate financial calculations
test_amount_valid = Decimal('50.00')
test_amount_invalid = Decimal('0.25')
api_endpoint = "https://api.example.com/pay" # Use a real API URL like those for 
