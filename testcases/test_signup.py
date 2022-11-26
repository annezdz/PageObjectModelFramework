import pytest

from pages.RegistrationPage import RegistrationPage
from testcases.BaseTest import BaseTest
from utilities.dataProvider import get_data

import logging
from utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_SignUp(BaseTest):

    @pytest.mark.parametrize(
        "name, phone_number, email, country, city, username, password",
        get_data('LoginTest'))
    def test_do_signup(self, name, phone_number, email, country, city,
                       username, password):
        log.logger.info('Test do sign started')
        reg_page = RegistrationPage(self.driver)
        reg_page.fill_form(name, phone_number, email, country, city, username,
                           password)
        log.logger.info('Test do sign successfully executed')

