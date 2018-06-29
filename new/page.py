from page.display_page import DisplayPage
from page.network_page import NetworkPage

class Page:
    def display_page(self):

    def click_display(self):
        self.click(self.display_button)

    def click_search(self):
        self.click(self.search_button)

    def input_text(self, content):
        self.input(self.search_button, content)

    def click_back(self):
        self.click(self.back_button)



