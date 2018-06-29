from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class DisplayPage(BaseAction):
    display_button=By.XPATH,"//*[contains(@text,'显示')]"
    search_button=By.ID,"com.android.settings:id/search"
    input_text_button=By.ID,"android:id/search_src_text"
    back_button=By.CLASS_NAME,"android.widget.ImageButton"

    def click_display(self):
        self.click(self.display_button)

    def click_search(self):
        self.click(self.search_button)

    def input_text(self,content):
        self.input(self.search_button,content)

    def click_back(self):
        self.click(self.back_button)

