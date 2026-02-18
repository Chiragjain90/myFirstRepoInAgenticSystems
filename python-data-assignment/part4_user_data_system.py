# User Data Processing System

# Function to calculate average score
def calculate_average(scores):
    return sum(scores) / len(scores)


# Function to check admin access
def has_admin_access(roles):
    return "admin" in roles


def main():
    users = [
        {
            "name": "Alice",
            "scores": [80, 85, 90],
            "roles": {"admin", "editor"}
        },
        {
            "name": "Bob",
            "scores": [70, 75, 80],
            "roles": {"viewer"}
        },
        {
            "name": "Charlie",
            "scores": [88, 92, 84],
            "roles": {"editor", "viewer"}
        }
    ]

    for user in users:
        avg_score = calculate_average(user["scores"])
        admin_access = has_admin_access(user["roles"])

        print("\nName:", user["name"])
        print("Average Score:", round(avg_score, 2))
        print("Admin Access:", admin_access)


# Run program
main()