class LoginPage:
    # URL of the page
    URL = "https://github.com/login"
    # Elements of the page
    LOGIN_FIELD = '//*[@id="login_field"]'
    PASSWORD_FIELD = '//*[@id="password"]'
    SIGNIN_BUTTON = '//*[@id="login"]/div[4]/form/div/input[13]'
    WRONG_CREDENTIALS_TEXTBOX = '//*[@id="js-flash-container"]/div/div/div'

    def __init__(self, app) -> None:
        self.app = app

    # User methods
    def navigate_to(self):
        self.app.navigate_to(self.URL)

    def try_login(self, username: str, password: str):
        self.app.enter_text(self.LOGIN_FIELD, username)
        self.app.enter_text(self.PASSWORD_FIELD, password)
        self.app.wait_and_click(self.SIGNIN_BUTTON)

    # Check functions
    def check_wrong_credentials_message(self):
        # Check if message "Incorrect username or password." appears.
        return self.app.check_text(
            self.WRONG_CREDENTIALS_TEXTBOX, "Incorrect username or password."
        )

    def check_documentation_link(self):
        pass
