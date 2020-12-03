from Base.base import Base
from Page.pageElements import PageElements
from selenium.common.exceptions import TimeoutException
import allure,logging


class HomePage(Base):

    def __init__(self):
        super().__init__()

    @allure.step("首页关闭更新按钮")
    def close_update_btn(self):
        """关闭更新按钮"""
        try:
            logging.info("首页关闭更新按钮")
            # 找到更新关闭按钮 -关闭
            self.click_ele(PageElements.home_update_close_btn_id)
        except TimeoutException:
            # 没有弹出更新提示框
            pass

    @allure.step("首页点击我")
    def click_my_btn(self):
        """点击我"""
        logging.info("首页点击我")
        self.click_ele(PageElements.home_my_btn_id)
