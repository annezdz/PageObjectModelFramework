import logging
import time

import pytest

from pages.CarBase import CarBase
from pages.HomePage import HomePage
from testcases.BaseTest import BaseTest
from utilities import dataProvider
from utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_Carwalle(BaseTest):

    @pytest.mark.skip
    def test_go_to_new_car(self):
        log.logger.info('*** Inside New Car Test ***')
        home = HomePage(self.driver)
        home.go_to_new_cars()
        time.sleep(3)

    @pytest.mark.skip
    @pytest.mark.parametrize('car_brand, car_title',
                             dataProvider.get_data('CarTest'))
    def test_select_cars(self, car_brand, car_title):
        log.logger.info('*** Inside Select Cars Test ***')
        home = HomePage(self.driver)

        car = CarBase(self.driver)
        print('Car brand is ', car_brand)
        if car_brand == 'Hyundai':
            home.go_to_new_cars().select_hyundai()
            title = car.get_car_title()
            assert title == car_title, 'Not on the correct page as title is ' \
                                       'not matching '
        elif car_brand == 'BMW':
            home.go_to_new_cars().select_bmw()
            title = car.get_car_title()
            assert title == car_title, 'Not on the correct page as title is ' \
                                       'not matching '
        elif car_brand == 'Honda':
            home.go_to_new_cars().select_honda()
            title = car.get_car_title()
            assert title == car_title, 'Not on the correct page as title is ' \
                                       'not matching '
        time.sleep(3)

    @pytest.mark.parametrize('car_brand, car_title',
                             dataProvider.get_data('CarTest'))
    def test_print_car_names(self, car_brand, car_title):
        log.logger.info('*** Inside Car Names Test ***')
        home = HomePage(self.driver)

        car = CarBase(self.driver)
        print('Car brand is ', car_brand)
        if car_brand == 'Hyundai':
            home.go_to_new_cars().select_hyundai()
            title = car.get_car_title()
            assert title == car_title, 'Not on the correct page as title is ' \
                                       'not matching '
            car.get_car_name()
        elif car_brand == 'BMW':
            home.go_to_new_cars().select_bmw()
            title = car.get_car_title()
            assert title == car_title, 'Not on the correct page as title is ' \
                                       'not matching '
            car.get_car_name()
        elif car_brand == 'Honda':
            home.go_to_new_cars().select_honda()
            title = car.get_car_title()
            assert title == car_title, 'Not on the correct page as title is ' \
                                       'not matching '
            car.get_car_name()

        time.sleep(3)
