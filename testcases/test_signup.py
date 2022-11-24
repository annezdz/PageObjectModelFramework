import pytest

from pages.RegistrationPage import RegistrationPage
from testcases.BaseTest import BaseTest
from utilities.dataProvider import get_data


class Test_SignUp(BaseTest):

    @pytest.mark.parametrize(
        "name, phone_number, email, country, city, username, password",
        get_data('LoginTest'))
    def test_do_signup(self, name, phone_number, email, country, city,
                       username, password):
        reg_page = RegistrationPage(self.driver)
        reg_page.fill_form(name, phone_number, email, country, city, username,
                           password)
