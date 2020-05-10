class HomePage:
    __logo = "//div[@class='logo-label'][contains(text(), 'ACME')]"
    __amount_header = "#amount"
    __table_amounts = "//td[@class='text-right bolder nowrap']/span"

    def __init__(self, driver):
        self.driver = driver

    def is_logo_visible(self):
        if self.driver.find_element_by_xpath(HomePage.__logo):
            return True
        else:
            return False

    def sorted_list_of_table_items(self):
        """"Gets the amounts of the unsorted table and sorts them"""
        unsorted_table_elements = self.driver.find_elements_by_xpath(HomePage.__table_amounts)
        sorted_list = []
        for i in unsorted_table_elements:
            sorted_list.append(i.text)
        sorted_list.sort(reverse=True)
        return sorted_list

    def sort_table_items(self):
        """Sorts the amounts of the table and gets the values"""
        self.driver.find_element_by_css_selector(HomePage.__amount_header).click()
        sorted_table_elements = self.driver.find_elements_by_xpath(HomePage.__table_amounts)
        sorted_table_items = []
        for i in sorted_table_elements:
            sorted_table_items.append(i.text)
        return sorted_table_items

    def are_amounts_equal(self):
        sorted_list = HomePage.sorted_list_of_table_items(self)
        sorted_table_items = HomePage.sort_table_items(self)
        are_amounts_equal = False
        for i, item in enumerate(sorted_list):
            if sorted_list[i] == sorted_table_items[i]:
                are_amounts_equal = True
        return are_amounts_equal

