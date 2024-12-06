#!/usr/bin/env python3

import subprocess
import sys

MAIN_BRANCH_NAME = "main"

def run_command(command):
    """Run a shell command and handle errors."""
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing: {' '.join(command)}")
        print(f"Error message: {e}")
        sys.exit(1)  # Exit the script with an error code

def clean_git_repo():
    TMP_ORPHAN_BRANCH_NAME = "latest_branch"
    # Step 1: Create a new orphan branch
    run_command(["git", "checkout", "--orphan", TMP_ORPHAN_BRANCH_NAME])

    # Step 2: Add all files to the new branch
    run_command(["git", "add", "-A"])

    # Step 3: Commit the changes
    run_command(["git", "commit", "-m", "refresh repo"])

    # Step 4: Delete the old branch
    run_command(["git", "branch", "-D", MAIN_BRANCH_NAME])

    # Step 5: Rename the new branch to the old branch name
    run_command(["git", "branch", "-m", MAIN_BRANCH_NAME])

    # Step 6: Clean up unused objects
    run_command(["git", "gc", "--prune=now"])

if __name__ == "__main__":
    if input("!!!WARNING!!! this script will remove all git history to reduce git repo size, continue? yes/[no]: ").lower().strip() != 'yes':
        print(f"Exit")
        sys.exit(0)

    clean_git_repo()

