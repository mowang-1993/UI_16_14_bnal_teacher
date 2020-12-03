from selenium.webdriver.common.by import By

from Base.page import Page

# 首页关闭更新
Page.get_home().close_update_btn()

# 首页 点击 我
Page.get_home().click_my_btn()

# 注册 点击 已有账号去登陆
Page.get_sign().click_exits_account()

# 登陆
Page.get_login().login("sadsad222", "159357li")

# 打印提示toast消息

print("toast消息:{}".format(Page.get_login().get_app_toast("不存在")))

# 关闭登录页面
Page.get_login().close_login_page()

# # 个人中心- 打印用户名
# print("用户名:{}".format(Page.get_person().get_user_name()))
#
# # 个人中心 -点击设置
# Page.get_person().click_setting_btn()
#
# # 设置页面 - 点击退出
# Page.get_setting().logout()
