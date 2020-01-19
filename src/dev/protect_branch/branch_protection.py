import requests
import os

repo = 'mynewexperiments/simple_webapp'
branch = 'master'
access_token = os.environ["GITHUB_TOKEN"]

def update_protection():
    r = requests.put(
    'https://api.github.com/repos/{0}/branches/{1}/protection'.format(repo, branch),
    headers = {
        'Accept': 'application/vnd.github.luke-cage-preview+json',
        'Authorization': 'Token {0}'.format(access_token)
    },
    json = {
        "required_status_checks": None,
        "enforce_admins": None,
        "required_pull_request_reviews": None,
        "allow_deletions": False
    }
    )
    return r
    
if __name__ == "__main__":
    update_protection()