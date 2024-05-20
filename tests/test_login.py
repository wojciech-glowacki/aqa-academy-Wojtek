from src.applications.ui.github_ui import GithubUi


def test_unsuccesful_login(github_ui_app):
    """Summary: Test unsuccesful login attempt
    Steps:
    1. Navigate to login page
    2. Enter wrong credentials
    3. Click login / signin button

    Expected result:
    Error "BLA" appeared
    """
    # 1. Navigate to login page
    github_ui_app.login_page.navigate_to()

    # 2. Enter wrong crdentials and 3. Click login / signin button
    github_ui_app.try_login(username="abrakadabra", password="hokuspokusplplplpksdofdg")

    # Expected results
    assert github_ui_app.login_page.check_wrong_credentials_message()
