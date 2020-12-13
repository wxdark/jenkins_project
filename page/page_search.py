import allure

import page
from base.base import Base


class PageSearch(Base):
    # 在搜索框输入内容
    # 添加测试步骤
    @allure.step(title="输入关键字")
    def page_input_key_word(self, value):
        # 添加文字描述信息
        allure.attach(value, "关键字", allure.attachment_type.TEXT)
        self.base_input(page.search_input, value)
        # 添加图片描述
        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)
        # allure.attach.file('../report', attachment_type=allure.attachment_type.PNG)

    # 点击返回按钮
    @allure.step(title="点击返回按钮")
    def page_click_back_btn(self):
        self.base_click_element(page.search_back_btn)
