from selenium.webdriver.common.by import By

from utilities import configReader


class CarBase:

    def __init__(self, driver):
        self.driver = driver

    def get_car_title(self):
        return self.driver.find_element(By.XPATH,
                                        configReader.read_config('locators',
                                                                 'carTitle_XPATH')).text

    def get_car_name(self):
        car_names = self.driver.find_elements(By.XPATH,
                                              configReader.read_config(
                                                  'locators',
                                                  'carName_XPATH'))
        for i in range(1, len(car_names)):
            print(car_names[i].text)
