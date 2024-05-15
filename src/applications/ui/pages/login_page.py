class LoginPage:
    # URL of the page
    URL = "https://github.com/login"
    # Elements of the page
    LOGIN_FIELD = '//*[@id="login_field"]'
    PASSWORD_FIELD = '//*[@id="password"]'
    SIGNIN_BUTTON = '//*[@id="login"]/div[4]/form/div/input[13]'

    # User methods
    def navigate_to(self):
        pass

    def try_login(self, username: str, password: str):
        pass

    # Check functions
    def check_wrong_credentials_message(self):
        # Find error message
        # Chceck if error message text is "BLA"
        return False

    def check_documentation_link(self):
        pass
