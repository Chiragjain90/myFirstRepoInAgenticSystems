# Import required library
import requests

# API endpoint
url = "https://api.github.com/search/repositories"

# Query parameters
params = {
    "q": "python",        # Search keyword
    "sort": "stars",      # Sort by stars
    "order": "desc",      # Descending order
    "per_page": 5         # Limit to 5 results
}

# Send GET request
response = requests.get(url, params=params)

# Convert response to JSON
data = response.json()

# Extract repository items
repos = data.get("items", [])

# Print required details
print("Top 5 Python Repositories on GitHub:\n")

for repo in repos:
    name = repo.get("name")
    stars = repo.get("stargazers_count")

    print(f"Repository Name: {name}")
    print(f"Stars: {stars}")
    print("-" * 30)
    