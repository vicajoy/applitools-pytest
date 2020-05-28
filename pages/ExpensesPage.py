from selenium.webdriver.common.by import By


class ExpensesPage:

    __show_data_for_next_year_btn = (By.ID, "addDataset")

    def __init__(self, driver):
        self.driver = driver

    def show_data_for_next_year(self):
        self.driver.find_element(*self.__show_data_for_next_year_btn).click()
