import os


class Config:
    TIMEOUT_UI_ELEMENTS_MS = 1000

    def init(self) -> None:
        if os.getenv("ENV") == "DEV":
            self.BASE_URL = "google.com"
