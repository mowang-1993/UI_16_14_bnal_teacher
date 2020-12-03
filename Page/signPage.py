from Base.base import Base
from Page.pageElements import PageElements
import allure,logging


class SignPage(Base):

    def __init__(self):
        super().__init__()

    @allure.step("注册页面点击已有账号去登陆")
    def click_exits_account(self):
        """已有账号去登录"""
        logging.info("注册页面点击已有账号去登陆")
        self.click_ele(PageElements.sign_exits_account_login_id)
