from src.applications.ui.github_ui import GithubUi


def test_unsuccesful_login(GithubUi):
    """Summary: Test unsuccesful login attempt
    Steps:
    1. Navigate to login page
    2. Enter wrong credentials
    3. Click login / signin button

    Expected result:
    Error "BLA" appeared
    """
    # 1. Navigate to login page
    GithubUi.open()  # Webdriver method - BAD
    GithubUi.login_page.navigate_to()

    # 2. Enter wrong crdentials and 3. Click login / signin button
    GithubUi.try_login(username="abrakadabra", password="hokuspokusplplplpksdofdg")

    # Expected results
    assert GithubUi.login_page.check_wrong_credentials_message()

    # Cleanup
    GithubUi.close()  # Webdriver method - BAD
