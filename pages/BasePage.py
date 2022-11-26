from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities import configReader
import logging
from utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith('_XPATH'):
            self.driver.find_element(By.XPATH, configReader.read_config
            ("locators", locator)).click()
        elif str(locator).endswith('_CSS'):
            self.driver.find_element(By.CSS_SELECTOR, configReader.read_config
            ("locators", locator)).click()
        elif str(locator).endswith('_ID'):
            self.driver.find_element(By.ID, configReader.read_config
            ("locators", locator)).click()
        log.logger.info("Clicking on an element: " + str(locator))

    def type(self, locator, value):
        if str(locator).endswith('_XPATH'):
            self.driver.find_element(By.XPATH, configReader.read_config
            ("locators", locator)).send_keys(value)
        elif str(locator).endswith('_CSS'):
            self.driver.find_element(By.CSS_SELECTOR, configReader.read_config
            ("locators", locator)).send_keys(value)
        elif str(locator).endswith('_ID'):
            self.driver.find_element(By.ID, configReader.read_config
            ("locators", locator)).send_keys(value)
        log.logger.info("Typing on an element: " + str(locator) +
                        " value entered as: " + str(value))

    def select(self, locator, value):
        global dropdown
        if str(locator).endswith('_XPATH'):
            dropdown = self.driver.find_element(By.XPATH,
                                                configReader.read_config
                                                ("locators", locator))
        elif str(locator).endswith('_CSS'):
            dropdown = self.driver.find_element(By.CSS_SELECTOR,
                                                configReader.read_config
                                                ("locators", locator))
        elif str(locator).endswith('_ID'):
            dropdown = self.driver.find_element(By.ID, configReader.read_config
            ("locators", locator))
        select = Select(dropdown)
        select.select_by_visible_text(value)
        log.logger.info("Selecting on an element: " + str(locator) +
                        " and select value " + str(value))

    def moveTo(self, locator):
        global element
        if str(locator).endswith('_XPATH'):
            element = self.driver.find_element(By.XPATH,
                                               configReader.read_config
                                               ("locators", locator))
        elif str(locator).endswith('_CSS'):
            element = self.driver.find_element(By.CSS_SELECTOR,
                                               configReader.read_config
                                               ("locators", locator))
        elif str(locator).endswith('_ID'):
            element = self.driver.find_element(By.ID, configReader.read_config
            ("locators", locator))

        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        log.logger.info("Moving to an element: " + str(locator))
