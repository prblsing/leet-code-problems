import os
import sys
import re
import tempfile
from git import Repo
from github import Github

def parse_issue_body(issue_body):
    path_regex = r'Code Component Path: (.+)\n'
    repo_regex = r'Target Repository: (.+)\n'
    branch_regex = r'Branch Name: (.+)\n'

    code_path = re.search(path_regex, issue_body).group(1)
    target_repo = re.search(repo_regex, issue_body).group(1)
    branch_name = re.search(branch_regex, issue_body).group(1)

    return code_path, target_repo, branch_name

def move_code_component(github_token, code_path, target_repo, branch_name):
    # Create a GitHub instance using the provided token
    github = Github(github_token)

    # Get the source and target repositories
    source_repo = github.get_repo("your-github-username/svn2git-master")
    target_repo = github.get_repo(f"your-github-username/{target_repo}")

    # Download the source code component
    file_content = source_repo.get_contents(code_path).decoded_content

    # Create a new branch in the target repository
    base_ref = target_repo.get_git_ref("heads/main")
    new_branch_ref = target_repo.create_git_ref(f"refs/heads/{branch_name}", base_ref.object.sha)

    # Upload the code component to the target repository
    target_path = os.path.basename(code_path)
    target_repo.create_file(target_path, f"Add {target_path} from svn2git-master", file_content, branch=branch_name)

if __name__ == "__main__":
    issue_body = sys.argv[1]
    code_path, target_repo, branch_name = parse_issue_body(issue_body)

    github_token = os.environ["PAT"]
    move_code_component(github_token, code_path, target_repo, branch_name)
