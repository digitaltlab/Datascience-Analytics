import requests
import json

# API endpoint
api_url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=325bba89a7e8104ddd1d3b6650f442fb"

# Send a GET request to the API
response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=London&appid=325bba89a7e8104ddd1d3b6650f442fb")

# Handle different HTTP status codes
if response.status_code == 200:
    # 200 OK: The request was successful, and the server returned the requested data.
    data = response.json()
    print("Request successful! Here is the data:")
    print(json.dumps(data, indent=4))

elif response.status_code == 201:
    # 201 Created: The request was successful, and a resource was created.
    print("Resource created successfully.")

elif response.status_code == 400:
    # 400 Bad Request: The request was malformed or invalid.
    print("Bad request. Please check your request syntax or parameters.")

elif response.status_code == 401:
    # 401 Unauthorized: Authentication is required or has failed.
    print("Unauthorized. Please check your API key or credentials.")

elif response.status_code == 403:
    # 403 Forbidden: The server understood the request but refuses to authorize it.
    print("Forbidden. You don't have permission to access this resource.")

elif response.status_code == 404:
    # 404 Not Found: The requested resource could not be found.
    print("Resource not found. Please check the API endpoint URL.")

elif response.status_code == 500:
    # 500 Internal Server Error: The server encountered an error and could not complete the request.
    print("Internal server error. Please try again later.")

else:
    # If none of the above conditions match, print an unexpected status code
    print(f"Unexpected status code: {response.status_code}. Please check the API documentation.")
