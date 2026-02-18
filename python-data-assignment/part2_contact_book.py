# Simple Contact Book

contacts = {
    "Ravi": "9876543210",
    "Anita": "9123456780",
    "Suresh": "9988776655"
}

# Print all contacts
print("Contact List:")
for name, number in contacts.items():
    print(name, ":", number)

# User input
search_name = input("\nEnter name to search: ")

# Dictionary lookup
if search_name in contacts:
    print("Phone Number:", contacts[search_name])
else:
    print("Contact not found")