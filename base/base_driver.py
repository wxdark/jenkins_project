from appium import webdriver


def get_driver():
    desired_cap = dict()
    # 需要连接的手机的平台
    desired_cap['platformName'] = "Android"
    # 需要连接的手机系统版本号
    desired_cap['platformVersion'] = "5.1"
    # 需要连接的手机设备号
    desired_cap['deviceName'] = "192.168.149.101:5555"
    # 需要打开的包名
    desired_cap['appPackage'] = "com.android.settings"
    # 需要打开的界面名
    desired_cap['appActivity'] = ".Settings"
    # 不重置应用
    desired_cap['noReset'] = True

    # 连接appium服务器，获取driver对象
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
    return driver
