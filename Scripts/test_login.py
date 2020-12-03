from Base.page import Page
from Base.getData import GetData
from Base.driver import Driver
import pytest, allure,logging


def get_login_data():
    # 空列表存储数据
    login_list = []
    # 读取json数据
    data = GetData.get_json_data("login.json")
    # 遍历
    for i in data:
        # 添加数据到列表
        login_list.append((i.get("desc"),
                           i.get("account"),
                           i.get("password"),
                           i.get("toast"),
                           i.get("exp")
                           ))
    return login_list


class TestLogin:

    def setup_class(self):
        """首页点击关闭"""
        Page.get_home().close_update_btn()

    def setup(self):
        """
        点击我的 -已有账号去登陆
        :return:
        """
        # 我
        Page.get_home().click_my_btn()
        # 已有账号去登陆
        Page.get_sign().click_exits_account()

    def teardown_class(self):
        """退出driver"""
        Driver.quit_app_driver()

    @pytest.mark.parametrize("desc, account, password, toast, exp", get_login_data())
    def test_login(self, desc, account, password, toast, exp):
        """
        登录测试方法
        :param desc: 用例描述
        :param account: 账号
        :param password: 密码
        :param toast: 获取toast拼接关键文本
        :param exp: 预期结果
        :return:
        """
        logging.info("用例类型:{}".format(desc))
        # 登录
        Page.get_login().login(account, password)
        if toast:
            # 逆向数据
            # 获取toast消息
            message = Page.get_login().get_app_toast(toast)
            try:
                # 断言
                assert message == exp
            except AssertionError as e:  # 断言失败异常AssertionError
                # 截图
                Page.get_setting().screenshot()
                # 抛出异常
                raise e
            finally:
                # 关闭登陆页面
                Page.get_login().close_login_page()

        else:
            # 正向数据
            # 获取用户名
            user_name = Page.get_person().get_user_name()
            try:
                # 断言
                assert user_name == exp
            except AssertionError as e:  # 捕获断言失败异常
                # 截图
                Page.get_setting().screenshot()
                # 抛出异常
                raise e
            finally:
                # 点击设置
                Page.get_person().click_setting_btn()
                # 退出
                Page.get_setting().logout()
