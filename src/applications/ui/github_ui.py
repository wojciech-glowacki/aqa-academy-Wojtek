from src.applications.ui.base_app import BaseApp
from src.applications.ui.pages.main_page import MainPage
from src.applications.ui.pages.login_page import LoginPage
from src.applications.ui.pages.signup_page import SignupPage


class GithubUi(BaseApp):

    def __init__(self, browser) -> None:
        super().__init__(browser)
        self.login_page = LoginPage(self)
        self.signup_page = SignupPage(self)
        self.main_page = MainPage(self)

    def open(self):
        self.main_page.navigate_to()

    def close(self):
        self.close_browser()

    def try_login(self, username: str, password: str):
        return self.login_page.try_login(username, password)

    def logout(self):
        self.wait_and_click(logoutbuttonlocatorTODO)

    def create_user(self):
        pass
