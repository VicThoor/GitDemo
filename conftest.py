import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store",default="firefox")


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Firefox(executable_path=r"C:\Users\vcarciu\Desktop\geckodriver-v0.30.0-win64\geckodriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
