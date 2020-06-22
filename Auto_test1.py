# Author:ToddCombs
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time


def auto_robot_link():     # 遍历一次首页导航栏各链接并检查名称及跳转链接是否正确
    browser = webdriver.Firefox()
    browser.get("http://www.jfinfo.com")
    browser.maximize_window()
    test_case1 = 'jf' in browser.current_url
    home_page = browser.find_element_by_link_text('首页').click()
    jfnc = browser.find_element_by_link_text('巨丰内参').click()
    browser.back()
    gmxy = browser.find_element_by_link_text('股民学院').click()
    browser.back()
    yjy = browser.find_element_by_link_text('研究院').click()
    browser.back()
    tzzjy = browser.find_element_by_link_text('投资者教育').click()
    browser.back()
    ggzx = browser.find_element_by_link_text('港股资讯').click()
    jfcp = browser.find_element_by_link_text('巨丰产品').click()
    gywm = browser.find_element_by_link_text('关于我们').click()

    browser.back()
    # test_case2 = '首页' in browser
    # test_case3 = '巨丰内参' in browser
    # time.sleep(2.0)
    # browser.quit()
    # print(test_case1, test_case2, test_case3)


auto_robot_link()


def auto_search():
    browser = webdriver.Firefox()
    browser.get("http://www.jfinfo.com")
    browser.maximize_window()
    input_id = browser.find_element_by_id('stock_search').send_keys('600519')
    search_css = browser.find_element_by_css_selector('html body div.p-content div.m-contentr.right div form#stock_search_form input#search_stock').click()


auto_search()

# browser.find_element_by_id("query").send_keys("Trump")
# browser.find_element_by_xpath("//input[@id='query']").send_keys(u"梅赛德斯")
# browser.find_element_by_xpath("//input[@id='stb']").click()
# time.sleep(3.0)
# browser.find_element_by_link_text(u"梅赛德斯 - 搜狗百科").click()
# # assert "sogo" in browser.title
# # elem = browser.find_element_by_name("p")
# # elem.send_keys("seleniumhq" + Keys.RETURN)

# try:
#     browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
# except NoSuchElementException:
#     assert 0, "can't find seleniumhq"
