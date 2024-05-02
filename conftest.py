import pytest
import requests
from selenium import webdriver

from data import Urls
from helpers import GenerateTestData


@pytest.fixture(params=['firefox', 'chrome'], scope='function')
def driver(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def new_user():
    test_data = GenerateTestData()
    user_data = test_data.create_register_information()
    response = requests.post(f'{Urls.USER_CREATION_ENDPOINT}',
                             data=user_data)
    token = response.json()['accessToken']
    yield user_data
    headers = {"Content-Type": "application/json", 'authorization': token}
    requests.delete(f'{Urls.USER_ENDPOINT}', headers=headers)