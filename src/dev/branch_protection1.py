from github import Github
import os

AUTH_TOKEN = os.environ["AUTH_TOKEN"]

g= Github(AUTH_TOKEN)

def change_protected_branch_settings():
    for repo in g.get_user().get_repos():
        branch = repo.get_branch("master")
        branch.edit_protection(required_approving_review_count=2, enforce_admins=True)
        print("Edited the branch protection rules for: " + repo.name)

def change_protected_branch_settings_test():
    branch = g.get_repo("mynewexperiments/test123").get_branch("master")
    branch.edit_protection(required_approving_review_count=2, enforce_admins=True)

