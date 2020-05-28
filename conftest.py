import os

import pytest
from applitools.common import BatchInfo, MatchLevel, StitchMode
from applitools.selenium import ClassicRunner, Eyes
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption("--url", action="store", default="https://demo.applitools.com/hackathon.html",
                     help="Choose version of the application")


@pytest.fixture
def browser(request):
    """Initiates the browser."""
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path='drivers/chromedriver')
        driver.get(url)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path='drivers/geckodriver')
        driver.get(url)
    elif browser == "headless chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options, executable_path='drivers/chromedriver')
        driver.get(url)
    else:
        raise Exception(f"{request.param} is not supported.")
    yield driver
    driver.quit()


@pytest.fixture
def url(request):
    url = request.config.getoption("--url")
    return url


@pytest.fixture(scope="module")
def batch_info():
    """Use one BatchInfo for all tests inside module."""
    return BatchInfo("Applitools Demo Visual Tests")


@pytest.fixture(name="runner", scope="session")
def runner_setup():
    """One test runner for all tests. Print test results in the end of execution."""
    runner = ClassicRunner()
    yield runner


@pytest.fixture(name="eyes", scope="function")
def eyes_setup(runner, batch_info, request):
    """Basic Eyes setup. It'll abort test if wasn't closed properly."""
    eyes = Eyes(runner)
    eyes.api_key = os.getenv("APPLITOOLS_API_KEY")
    eyes.configure.batch = batch_info
    eyes.configure.match_level = MatchLevel.STRICT
    eyes.configure.set_stitch_mode(StitchMode.CSS)
    yield eyes
