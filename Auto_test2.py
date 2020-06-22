# @Time    : ${DATE} ${TIME}
# @Author  : ToddCombs
from selenium import webdriver

b = webdriver.chrome()
b.get("https://www.baidu.com")
print(b.title)
check1 = 'bai' in b.current_url
print(check1)
b.find_element_by_name('wd').send_keys('pycharm')
b.quit()
