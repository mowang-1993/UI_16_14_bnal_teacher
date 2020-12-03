from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Base.driver import Driver
import time, allure, logging


class Base:

    def __init__(self):
        # 声明app driver对象
        self.driver = Driver.get_app_driver()

    def search_ele(self, loc, timeout=5, poll=1.0):
        """
        定位单个元素
        :param loc: 元组 (By.ID,属性值)....
        :param timeout: 超时时间
        :param poll: 搜索间隔
        :return: 定位对象
        """
        logging.info("定位单个元素:{}".format(loc))
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def search_eles(self, loc, timeout=5, poll=1.0):
        """
        定位一组元素
        :param loc: 元组 (By.ID,属性值)....
        :param timeout: 超时时间
        :param poll: 搜索间隔
        :return: 定位对象列表
        """

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll=1.0):
        """
        点击元素
        :param loc: 元组 (By.ID,属性值)....
        :param timeout: 超时时间
        :param poll: 搜索间隔
        :return:
        """
        logging.info("点击元素")
        self.search_ele(loc, timeout, poll).click()

    def send_ele(self, loc, text, timeout=5, poll=1.0):
        """
        输入内容
        :param loc: 元组 (By.ID,属性值)....
        :param text: 输入文本
        :param timeout: 超时时间
        :param poll: 搜索间隔
        :return:
        """
        logging.info("输入操作，输入文本:{}".format(text))
        # 定位
        input_text = self.search_ele(loc, timeout, poll)
        # 清空
        input_text.clear()
        # 输入
        input_text.send_keys(text)

    def swipe_app(self, tag=1):
        """
        App滑动页面
        :param tag: 1:上 2:下 3:左 4:右
        :return:
        """
        # 获取屏幕分辨率
        size = self.driver.get_window_size()
        # 宽
        width = size.get("width")
        # 高
        height = size.get("height")
        # 等待
        time.sleep(1.5)
        # 判断滑动
        # 水平 宽80%和宽20% 高50% 垂直 高80%和高20% 宽50%
        if tag == 1:
            logging.info("向上滑动页面")
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 1000)
        if tag == 2:
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, 1000)
        if tag == 3:
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, 1000)
        if tag == 4:
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, 1000)

    def get_app_toast(self, mess):
        """
        获取手机toast消息
        :param mess: 拼接xpath语句关键文本内容
        :return:
        """
        mess_xpath = (By.XPATH, "//*[contains(@text,'{}')]".format(mess))

        toast_mess = self.search_ele(mess_xpath, timeout=3, poll=0.3).text
        logging.info("获取的toast消息:{}".format(toast_mess))
        return toast_mess

    def screenshot(self, name="截图"):
        """截图方法"""
        logging.info("截图操作")
        allure.attach(self.driver.get_screenshot_as_png(), name,
                      allure.attachment_type.PNG)
