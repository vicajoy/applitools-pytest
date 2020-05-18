class ExpensesPage:

    __show_data_for_next_year_btn = "#addDataset"

    def __init__(self, driver):
        self.driver = driver

    def show_data_for_next_year(self):
        self.driver.find_element_by_css_selector(ExpensesPage.__show_data_for_next_year_btn).click()

