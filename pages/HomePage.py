from pages.BasePage import BasePage
from pages.NewCarsPage import NewCarsPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_new_cars(self):
        self.moveTo('newCar_XPATH')
        self.click('findNewCars_XPATH')
        return NewCarsPage(self.driver)

    def go_to_compare_cars(self):
        pass

    def go_to_used_cars(self):
        pass
