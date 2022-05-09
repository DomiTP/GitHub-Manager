from git import Repo


def get_repo_info(repo_path):
    """
    Obtain information about the repository.
    :return: A tuple containing the following information: (username, project_name, full_repo_name)
    """

    repo = Repo(repo_path)

    repo_name = repo.remotes.origin.url.split('.git')[0].split('/')[-1]
    repo_user = repo.remotes.origin.url.split('.git')[0].split('/')[-2]
    if ":" in repo_user:
        repo_user = repo_user.split(':')[-1]
    full_repo_name = f'{repo_user}/{repo_name}'

    return repo_user, repo_name, full_repo_name
