# secure_api_request.py

import os
import requests

# -------------------------------
# 1. Retrieve API Key securely
# -------------------------------
api_key = os.getenv("API_KEY")

if not api_key:
    print("Error: API_KEY not found in environment variables.")
    exit()

# -------------------------------
# 2. Define API endpoint
# -------------------------------
url = "https://jsonplaceholder.typicode.com/posts"

# -------------------------------
# 3. Set headers with Bearer Token
# -------------------------------
headers = {
    "Authorization": f"Bearer {api_key}"
}

# -------------------------------
# 4. Send GET request
# -------------------------------
try:
    response = requests.get(url, headers=headers)

    # -------------------------------
    # 5. Handle status codes
    # -------------------------------
    if response.status_code == 200:
        print("Success! Response Data:\n")
        print(response.json())

        # Observation:
        # Successfully fetched data using secure API key

    elif response.status_code == 429:
        print("Rate limit reached. Try again later.")

        # Observation:
        # API rate limit exceeded

    else:
        print(f"Request failed with status code: {response.status_code}")

        # Observation:
        # Some other error occurred (e.g., 401, 500)

except requests.exceptions.RequestException as e:
    print("An error occurred while making the request:")
    print(e)

    # Observation:
    # Network or connection-related issue