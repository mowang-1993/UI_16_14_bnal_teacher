from selenium.webdriver.common.by import By


class PageElements:
    """首页"""
    # 更新 -关闭
    home_update_close_btn_id = (By.ID, "com.yunmall.lc:id/img_close")
    # 我的
    home_my_btn_id = (By.ID, "com.yunmall.lc:id/tab_me")

    """注册页面"""
    # 已有账号去登陆
    sign_exits_account_login_id = (By.ID, "com.yunmall.lc:id/textView1")

    """登录页面"""
    # 账号
    login_account_id = (By.ID, "com.yunmall.lc:id/logon_account_textview")
    # 密码
    login_password_id = (By.ID, "com.yunmall.lc:id/logon_password_textview")
    # 登录按钮
    login_btn_id = (By.ID, "com.yunmall.lc:id/logon_button")
    # 关闭登录页面按钮
    login_close_page_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")

    """个人中心"""
    # 用户名
    person_user_name_id = (By.ID, "com.yunmall.lc:id/tv_user_nikename")
    # 设置
    person_setting_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")

    """设置页面"""
    # 退出
    setting_logout_btn_id = (By.ID, "com.yunmall.lc:id/setting_logout")
    # 确认退出
    setting_logout_acc_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")
    # 取消退出
    setting_logout_dis_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_left_button")
