from Base.base import Base
from Page.pageElements import PageElements
import allure, logging


class PersonPage(Base):

    def __init__(self):
        super().__init__()

    @allure.step("个人中心获取用户名")
    def get_user_name(self):
        """获取用户名"""
        name = self.search_ele(PageElements.person_user_name_id).text
        logging.info("获取用户名:{}".format(name))
        return name

    @allure.step("个人中心点击设置")
    def click_setting_btn(self):
        """点击设置按钮"""
        logging.info("个人中心页面点击设置按钮")
        self.click_ele(PageElements.person_setting_btn_id)
