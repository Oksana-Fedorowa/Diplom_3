import pytest
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from helpers import *
import requests
from data import Data



@pytest.fixture(scope='function', params=['Chrome', 'Firefox'])
def driver(request):
    driver = None
    if request.param == 'Chrome':
        chromedriver_autoinstaller.install()
        options = ChromeOptions()
        options.add_argument('--window-size=1280,768')
        driver = webdriver.Chrome(options=options)
    elif request.param == 'Firefox':
        options = FirefoxOptions()
        options.add_argument("--width=1280")
        options.add_argument("--height=768")
        driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def registered_user():

    payload = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_name()
    }
    response = requests.post(Data.REGISTER_URL, data=payload)
    yield payload
    requests.delete(Data.DELETE_USER, headers={'authorization': response.json()["accessToken"]})



