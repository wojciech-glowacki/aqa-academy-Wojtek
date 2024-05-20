class MainPage:
    # URL of the page
    URL = "https://github.com/"

    def __init__(self, app) -> None:
        self.app = app

    # User methods
    def navigate_to(self):
        self.app.navigate_to(self.URL)
