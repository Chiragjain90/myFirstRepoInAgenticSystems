import json

# Step 1: Store JSON-formatted API response
api_response = '''
{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
'''

# Step 2: Parse JSON string into Python dictionary
parsed_response = json.loads(api_response)

# Step 3: Extract required values
request_id = parsed_response.get("id")
status = parsed_response.get("status")

result_data = parsed_response.get("result", {})
text_result = result_data.get("text")
confidence_score = result_data.get("confidence")

# Step 4: Print extracted values
print("Request ID:", request_id)
print("Status:", status)
print("Text Result:", text_result)
print("Confidence Score:", confidence_score)

# Step 5: Check confidence score
if confidence_score is not None and confidence_score < 0.9:
    print("Warning: Confidence score is below acceptable threshold!")

# Step 6: Create a follow-up result dictionary
follow_up_result = {
    "request_id": request_id,
    "status": "processed",
    "message": text_result,
    "confidence_score": confidence_score
}

# Step 7: Convert dictionary to JSON
follow_up_json = json.dumps(follow_up_result, indent=4)

# Step 8: Write JSON output to a file
with open("response.json", "w") as file:
    file.write(follow_up_json)

print("\nFollow-up JSON has been written to response.json")