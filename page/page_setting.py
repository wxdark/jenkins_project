import allure

import page
from base.base import Base


class PageSetting(Base):
    # 点击搜索按钮
    @allure.step(title="点击搜索")
    def page_click_search_btn(self):
        self.base_click_element(page.setting_search)
