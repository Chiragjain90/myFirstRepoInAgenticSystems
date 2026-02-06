# Secure Transaction Validator

balance = int(input("Enter account balance: "))
withdrawal_amount = int(input("Enter withdrawal amount: "))
verified_input = input("Are you verified (True/False): ")

verified = verified_input.strip().lower() == "true"

if verified and withdrawal_amount <= balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")