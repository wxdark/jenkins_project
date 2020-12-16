from time import sleep

import allure
import pytest
from base.base_analyze import data_analyze
from base.base_driver import get_driver
from page.page import Page


class TestSearch:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    # 添加严重级别
    """
    BLOCKER = 'blocker'  最严重
    CRITICAL = 'critical' 严重
    NORMAL = 'normal'     普通
    MINOR = 'minor'     不严重
    TRIVIAL = 'trivial'  最不严重
    """

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("args", data_analyze("search_data.yaml", "test_search"))
    def test_search(self, args):
        # 点击搜索按钮
        self.page.setting.page_click_search_btn()
        # 输入搜索内容
        self.page.search.page_input_key_word(args["content"])
        # 点击返回按钮
        self.page.search.page_click_back_btn()

    def test_search01(self):
        assert 0
