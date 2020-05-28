from selenium.webdriver.common.by import By


class HomePage:

    __logo = (By.XPATH, "//div[@class='logo-label'][contains(text(), 'ACME')]")
    __table = (By.ID, "transactionsTable")
    __amount_header = (By.ID, "amount")
    __table_amounts = (By.XPATH, "//td[@class='text-right bolder nowrap']/span")
    __compare_expenses_btn = (By.ID, "showExpensesChart")

    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self, url):
        return self.driver.get(url)

    def sorted_list_of_table_items(self):
        unsorted_table_elements = self.driver.find_elements(*self.__table_amounts)
        sorted_list = [e.text for e in unsorted_table_elements]
        sorted_list.sort(reverse=True)
        return sorted_list

    def sort_table_items(self):
        self.driver.find_element(*self.__amount_header).click()

    def are_amounts_equal(self):
        sorted_list = self.sorted_list_of_table_items()
        self.sort_table_items()
        sorted_table_elements = self.driver.find_elements(*self.__table_amounts)
        sorted_table_items = [e.text for e in sorted_table_elements]

        are_amounts_equal = False
        for i, item in enumerate(sorted_list):
            if sorted_list[i] == sorted_table_items[i]:
                are_amounts_equal = True
        return are_amounts_equal

    def compare_expenses(self):
        self.driver.find_element(*self.__compare_expenses_btn).click()
