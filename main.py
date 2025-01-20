from dotenv import load_dotenv
import requests

import json
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Load environment variables from .env file
load_dotenv()

def get_github_credentials():
    """Fetch GitHub credentials from environment variables."""
    username = os.getenv('GITHUB_USERNAME')
    repository = os.getenv('GITHUB_REPOSITORY')
    token = os.getenv('GITHUB_TOKEN')  # Optional, for higher rate limits

    if not username or not repository:
        missing_vars = []
        if not username:
            missing_vars.append('GITHUB_USERNAME')
        if not repository:
            missing_vars.append('GITHUB_REPOSITORY')
        raise KeyError(f"Missing environment variables: {', '.join(missing_vars)}")

    return {
        "username": username,
        "repository": repository,
        "token": token
    }

# Fetch GitHub credentials
try:
    credentials = get_github_credentials()
except KeyError as e:
    logging.error(e)
    exit(1)

# GitHub API endpoint for listing issues
url = f"https://api.github.com/repos/{credentials['username']}/{credentials['repository']}/issues"

# Optional: If you want to include closed issues as well
params = {
    "state": "all",  # Possible values: open, closed, all
    "per_page": 100,  # Max number of issues per page
    "page": 1
}

# Headers for authentication (if token is provided)
headers = {}
if credentials["token"]:
    headers['Authorization'] = f'token {credentials["token"]}'

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
            logging.error(f"Error: {response.status_code} - {response.text}")
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
