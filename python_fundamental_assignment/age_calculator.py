# User Age Calculator

CURRENT_YEAR = 2026

birth_year_input = input("Enter your birth year: ")

# explicit type conversion
birth_year = int(birth_year_input)

age = CURRENT_YEAR - birth_year

print(f"You are {age} years old.")