from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.BasePage import BasePage
from utilities import configReader


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self):
        pass
