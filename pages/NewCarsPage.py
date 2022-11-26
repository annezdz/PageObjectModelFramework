from pages.BasePage import BasePage


class NewCarsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def select_Model(self, model):
        self.moveTo(model)
        self.click(model)