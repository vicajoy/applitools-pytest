class HomePage:

    __logo = "//div[@class='logo-label'][contains(text(), 'ACME')]"
    __table = "#transactionsTable"
    __amount_header = "#amount"
    __table_amounts = "//td[@class='text-right bolder nowrap']/span"
    __compare_expenses_btn = "#showExpensesChart"

    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self, url):
        return self.driver.get(url)

    def is_logo_visible(self):
        if self.driver.find_element_by_xpath(HomePage.__logo):
            return True
        else:
            return False

    def sorted_list_of_table_items(self):
        unsorted_table_elements = self.driver.find_elements_by_xpath(HomePage.__table_amounts)
        sorted_list = list(map(lambda e: e.text, unsorted_table_elements))
        sorted_list.sort(reverse=True)
        return sorted_list

    def sort_table_items(self):
        self.driver.find_element_by_css_selector(HomePage.__amount_header).click()

    def are_amounts_equal(self):
        sorted_list = HomePage.sorted_list_of_table_items(self)
        HomePage.sort_table_items(self)
        sorted_table_elements = self.driver.find_elements_by_xpath(HomePage.__table_amounts)
        sorted_table_items = list(map(lambda e: e.text, sorted_table_elements))

        are_amounts_equal = False
        for i, item in enumerate(sorted_list):
            if sorted_list[i] == sorted_table_items[i]:
                are_amounts_equal = True
        return are_amounts_equal

    def compare_expenses(self):
        self.driver.find_element_by_css_selector(HomePage.__compare_expenses_btn).click()
