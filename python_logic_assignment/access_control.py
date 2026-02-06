# Access Control System

age = int(input("Enter your age: "))
has_id_input = input("Do you have an ID card (True/False): ")

# Handle boolean input safely
has_id = has_id_input.strip().lower() == "true"

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")