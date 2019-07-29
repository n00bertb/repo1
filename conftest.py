import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time



def pytest_addoption(parser):

    parser.addoption("--language", action="store", default="None",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")
    print("\nstart browser for test..")
    chrome_options = webdriver.ChromeOptions()
    #опция ниже запускает браузер с нужной локалью
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language})
    #без этих опшенсов ниже не запускается браузер в debian9 в windows можно их не включать
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    ###
    browser = webdriver.Chrome(chrome_options=chrome_options)
    yield browser
    print("\nquit browser..")
    browser.quit()

