import requests
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Check if environment variables are set
try:
    GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
    GITHUB_REPOSITORY = os.getenv('GITHUB_REPOSITORY')
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')  # Optional, for higher rate limits
except KeyError as e:
    print(f"Missing environment variable: {e}")
    exit(1)

# GitHub API endpoint for listing issues
url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{GITHUB_REPOSITORY}/issues"

# Optional: If you want to include closed issues as well
params = {
    "state": "all",  # Possible values: open, closed, all
    "per_page": 100,  # Max number of issues per page
    "page": 1
}

# Headers for authentication (if token is provided)
headers = {}
if GITHUB_TOKEN:
    headers['Authorization'] = f'token {GITHUB_TOKEN}'

# Function to fetch issues with pagination
def fetch_issues():
    issues = []
    while True:
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code == 200:
            issues.extend(response.json())
            if 'next' in response.links:
                params['page'] += 1
            else:
                break
        else:
            print(f"Error: {response.status_code} - {response.text}")
            break
    
    return issues

# Fetch all issues
issues = fetch_issues()

# Prepare the output as a list of dictionaries
output = []
for issue in issues:
    issue_data = {
        "number": issue['number'],
        "title": issue['title'],
        "state": issue['state'],
        "created_at": issue['created_at'],
        "body": issue['body'],
        "labels": [label['name'] for label in issue['labels']],
        "comments": issue['comments']
    }
    output.append(issue_data)

# Output the issues as a JSON object
print(json.dumps(output, indent=4))
