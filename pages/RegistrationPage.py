from pages.BasePage import BasePage


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_form(self, name, phone_number, email, country, city, username,
                  password):
        self.type("name_XPATH", name)
        self.type("phone_XPATH", phone_number)
        self.type("email_XPATH", email)
        self.select("country_XPATH", country)
        self.type("city_XPATH", city)
        self.type("username_XPATH", username)
        self.type("password_XPATH", password)
        self.click("submit_XPATH")



