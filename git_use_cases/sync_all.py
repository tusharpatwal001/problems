import subprocess


def sync_with_github_remote_all(comment: str, branch_name: str, path: str = ".") -> str:
    commands_list = [
        ["git", "status"],
        ["git", "add", f"{path}"],
        ["git", "status"],
        ["git", "commit", "-m", f"{comment}"],
        ["git", "status"],
        ["git", "push", "origin", f"{branch_name}"],
        ["git", "status"],
    ]
    for command in commands_list:
        subprocess.run(command, shell=True)

    return f"All Files synced to remote github"


sync_with_github_remote_all(
    "testing function for syncing all files - part3", "user/tushar_ca252"
)
