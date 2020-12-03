from appium import webdriver


class Driver:
    # app driver对象变量
    __app_driver = None

    @classmethod
    def get_app_driver(cls):
        """声明"""
        if cls.__app_driver is None:
            # server 启动参数
            desired_caps = {
                'platformName': "Android",
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.yunmall.lc',
                'appActivity': 'com.yunmall.ymctoc.ui.activity.MainActivity'
            }

            # 声明我们的driver对象
            cls.__app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            # 返回
            return cls.__app_driver
        else:
            return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        """退出"""
        if cls.__app_driver:
            # 退出driver
            cls.__app_driver.quit()
            # 重新置为None
            cls.__app_driver = None
