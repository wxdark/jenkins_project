from page.page_search import PageSearch
from page.page_setting import PageSetting


# page页统一入口
class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def setting(self):
        return PageSetting(self.driver)

    @property
    def search(self):
        return PageSearch(self.driver)
