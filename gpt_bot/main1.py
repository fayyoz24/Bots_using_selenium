import requests

data = {"auth": {"reactivate": False, "username": "alb@gmail.com", "password": "12345678"},
        "session_app": "dashboard"}

response = requests.post("https://api.crystalknows.com/v3/user_token", json=data)

token = response.json()["data"]["token"]
import requests
import json

# Define the GraphQL query and variables
query = '''
    query GetProfile($linkedinUrl: String!) {
        profile(
            linkedin_url: $linkedinUrl
            photo_url: ""
            contributor_app_name: "dashboard"
        ) {
            id
            first_name
            last_name
            job_title
            company_name
            linkedin_url
            personality {
                archetype
                degrees
                disc_type
                four_percentages {
                    d
                    i
                    s
                    c
                    __typename
                }
                intensity
                updated_by
                __typename
            }
            photo_url
            qualities
            sources
            verified
            editable
            accessible
            __typename
        }
    }
'''
import time
time.sleep(2)
variables = {
    "linkedinUrl": "https://nl.linkedin.com/in/max-van-gorkum-545910197"
}
print(token)
# Define the API endpoint and headers
url = "https://api.crystalknows.com/graphql"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}
time.sleep(2)
# Define the request payload
payload = {
    "query": query,
    "variables": variables
}

# Send the request and print the response
response = requests.post(url, headers=headers, json=payload, timeout=10)
time.sleep(2)
if response.status_code == 200:
    json_data = json.loads(response.text)
    print(json_data)
else:
    print("Error:", response.status_code)
