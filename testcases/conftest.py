import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities import configReader


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(params=['chrome', 'edge'], scope='function')
def get_browser(request):
    global driver
    if request.param == 'chrome':
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install())
    elif request.param == 'firefox':
        driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install())
    elif request.param == 'edge':
        driver = webdriver.Edge(
            executable_path=EdgeChromiumDriverManager().install())
    request.cls.driver = driver
    driver.get(configReader.read_config('basic info', 'testsiteurl'))
    driver.implicitly_wait(15)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def log_on_failure(request, get_browser):
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name='do_login',
                      attachment_type=AttachmentType.PNG)
