from pages.BasePage import BasePage


class NewCarsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def select_model(self, model):
        self.moveTo(model)
        self.click(model)

    def select_hyundai(self):
        self.moveTo('hyundai_XPATH')
        self.click('hyundai_XPATH')

    def select_bmw(self):
        self.moveTo('Bmw_XPATH')
        self.click('Bmw_XPATH')

    def select_honda(self):
        self.moveTo('honda_XPATH')
        self.click('honda_XPATH')
