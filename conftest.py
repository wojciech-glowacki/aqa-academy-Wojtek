import pytest
from src.applications.ui.github_ui import GithubUi
from selenium import webdriver


@pytest.fixture
def github_ui_app():
    driver = webdriver.Chrome()
    # 1. Prestep - navigate to Github application
    githubui_app = GithubUi(browser=driver)
    githubui_app.open()
    yield githubui_app
    # 2. Poststep - close the application
    githubui_app.close()
