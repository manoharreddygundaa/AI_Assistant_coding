import random
import datetime

# Function to validate user inputs
def validate_inputs(amount, currency, payment_method):
    # Check if amount is a positive number
    try:
        amount = float(amount)
        if amount <= 0:
            return False, "Amount must be greater than 0"
    except ValueError:
        return False, "Amount must be a valid number"

    # Check if currency is valid (simple check for common currencies)
    valid_currencies = ['USD', 'EUR', 'GBP', 'CAD', 'AUD']
    if currency.upper() not in valid_currencies:
        return False, "Invalid currency. Supported: USD, EUR, GBP, CAD, AUD"

    # Check if payment method is not empty
    if not payment_method.strip():
        return False, "Payment method cannot be empty"

    return True, ""

# Function to simulate payment processing
def process_payment(amount, currency, payment_method):
    # Simulate random success/failure (80% success rate)
    success = random.random() < 0.8

    if success:
        return True, "Payment successful"
    else:
        # Random failure reasons
        reasons = ["Insufficient funds", "Card declined", "Network error", "Invalid card details"]
        reason = random.choice(reasons)
        return False, f"Payment failed: {reason}"

# Function to log failed transactions
def log_failed_transaction(amount, currency, payment_method, reason):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | Amount: {amount} {currency} | Method: {payment_method} | Reason: {reason}\n"

    with open("failed_transactions.txt", "a") as file:
        file.write(log_entry)

# Main function
def main():
    print("Welcome to the Payment Gateway Simulator")

    # Get user inputs
    amount = input("Enter payment amount: ")
    currency = input("Enter currency (USD, EUR, GBP, CAD, AUD): ")
    payment_method = input("Enter payment method (e.g., Credit Card, PayPal): ")

    # Validate inputs
    is_valid, error_message = validate_inputs(amount, currency, payment_method)
    if not is_valid:
        print(f"Error: {error_message}")
        return

    # Convert amount to float after validation
    amount = float(amount)

    # Process payment
    success, message = process_payment(amount, currency, payment_method)

    # Display result
    print(message)

    # Log failed transactions
    if not success:
        log_failed_transaction(amount, currency, payment_method, message)

if __name__ == "__main__":
    main()