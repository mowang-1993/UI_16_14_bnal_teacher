from Base.base import Base
from Page.pageElements import PageElements
import allure, logging


class LoginPage(Base):

    def __init__(self):
        super().__init__()

    @allure.step("关闭登陆页面")
    def close_login_page(self):
        """关闭登陆页面"""
        logging.info("关闭登陆页面")
        self.click_ele(PageElements.login_close_page_btn_id)

    @allure.step("登录操作")
    def login(self, account, password):
        """
        登录
        :param account: 账号
        :param password: 密码
        :return:
        """
        logging.info("登录用户名:{} 密码:{}".format(account, password))
        # 输入账号
        self.send_ele(PageElements.login_account_id, account)
        # 输入密码
        self.send_ele(PageElements.login_password_id, password)
        # 点击登录按钮
        self.click_ele(PageElements.login_btn_id)
