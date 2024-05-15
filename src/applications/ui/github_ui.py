from src.applications.ui.pages.login_page import LoginPage
from src.applications.ui.pages.signup_page import SignupPage


class GithubUi:

    def __init__(self) -> None:
        self.login_page = LoginPage()
        self.signup_page = SignupPage()

    def try_login(self, username: str, password: str):
        return self.login_page.try_login(username, password)

    def logout(self):
        pass

    def create_user(self):
        pass
