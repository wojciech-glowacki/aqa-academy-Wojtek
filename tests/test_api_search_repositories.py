def test_check_search_repositories(github_api_client):
    """
    1. Send API request to search for repository, which name contains REPOSITIORIES_NAME_TO_SEARCH
    2. Analyse the response

    Expected result:
    Number of found repositories == EXPECTED_REPOSITORIES_NUMBER
    """

    REPOSITORIES_NAME_TO_SEARCH = "wojtek"
    EXPECTED_REPOSITORIES_NUMBER = 418

    # 1. Send API request to search for repository named "woj"
    repositories_count, response = github_api_client.search_repositories(
        REPOSITORIES_NAME_TO_SEARCH
    )

    # 2. Analyse the response
    response.raise_for_status()

    assert repositories_count == EXPECTED_REPOSITORIES_NUMBER
