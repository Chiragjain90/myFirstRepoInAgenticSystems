# Employee Role Checker

# Tuple storing employee details
employee = (101, "Rahul", "IT")

# Set storing roles
roles = {"editor", "viewer", "admin"}

# Printing employee info
print("Employee ID:", employee[0])
print("Employee Name:", employee[1])
print("Department:", employee[2])

# Checking admin access
if "admin" in roles:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")