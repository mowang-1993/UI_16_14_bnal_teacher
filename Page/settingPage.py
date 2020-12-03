from Base.base import Base
from Page.pageElements import PageElements
import allure,logging


class SettingPage(Base):

    def __init__(self):
        super().__init__()

    @allure.step("设置页面点击退出")
    def logout(self, tag=1):
        """
        退出
        :param tag: 1:退出 0：取消
        :return:
        """
        logging.info("退出操作")
        # 向上滑动页面
        self.swipe_app()
        # 点击退出
        self.click_ele(PageElements.setting_logout_btn_id)
        if tag == 1:
            # 退出
            self.click_ele(PageElements.setting_logout_acc_btn_id)
        if tag == 0:
            # 取消
            self.click_ele(PageElements.setting_logout_dis_btn_id)
