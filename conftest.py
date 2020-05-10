import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption("--url", action="store", default="https://demo.applitools.com/hackathon.html",
                     help="Choose version of the application")


@pytest.fixture
def browser(request):
    """Initiates the browser"""
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path='drivers/chromedriver')
        driver.get(url)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path='drivers/geckodriver')
        driver.get(url)
    else:
        raise Exception(f"{request.param} is not supported!")
    yield driver
    driver.quit()
