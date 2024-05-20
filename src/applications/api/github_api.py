import requests


class GithubApiClient:
    def __init__(self) -> None:
        pass

    def search_repositories(self, repository_name):
        response = requests.get(
            url=f"https://api.github.com/search/repositories?q={repository_name}"
        )
        response_data = response.json()

        return response_data["total_count"], response
