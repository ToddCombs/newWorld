# Author:ToddCombs
# 测试firefox浏览器是否可以正常被调起
from selenium import webdriver
import time


def auto_tester():
    wd = webdriver.Firefox()  # 引入Firefox浏览器驱动模块
    wd.get('https://www.12306.cn/index/')  # 访问的网址12306购票网站
    wd.maximize_window()  # 浏览器全屏
    url_test = '12306' in wd.current_url  # 检查12306的url是否正确
    time.sleep(5)  # 暂停5秒（时间）
    wd.quit()  # 关闭浏览器窗口
    print(url_test)  # 输出url校验结果是否为真


auto_tester()
