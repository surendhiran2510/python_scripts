import git

def clone_repository(repo_url, destination_path):
    try:
        git.Repo.clone_from(repo_url, destination_path)
        print(f"Repository cloned to {destination_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
repository_url = 'https://github.com/surendhiran2510/my-repo.git'
destination_folder = 'destination_folder'

clone_repository(repository_url, destination_folder)
