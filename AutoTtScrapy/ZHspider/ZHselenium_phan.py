# -*- coding:utf- 8 -*-
from selenium import webdriver
from lxml import etree
import time






class ZHs_p(object):

	def __init__(self):
		self.browser = webdriver.Chrome(executable_path = 'webdriver/chromedriver.exe')

	def start_url(self):
		start_url = 'https://www.zhihu.com/signup?next=%2F'
		self.browser.maximize_window()
		self.browser.get(start_url)
		print(self.browser.get_log('browser'))
		print(self.browser.get_cookies())

		time.sleep(1)
		checkout = self.browser.find_element_by_xpath('.//span[@data-reactid="94"]')
		checkout.click()
		print(self.browser.get_cookies())


	def login(self):
		username =  self.browser.find_element_by_xpath('.//input[@name="username"]')
		password = self.browser.find_element_by_xpath('.//input[@name="password"]')
		submit = self.browser.find_element_by_xpath('.//button[@type="submit"]')

		username.send_keys('13242311433')
		password.send_keys('xieyueying1')
		time.sleep(1)
		submit.click()

		print(self.browser.get_cookies())

if __name__ == '__main__':
	ZH = ZHs_p()
	ZH.start_url()
	# ZH.login()











	# [{'value': 'ZFBIUArMej3iy2zABeQe29519a24dd7a', 'expiry': 1623283199.612156, 'httpOnly': False, 'path': '/', 'domain': 'www.zhihu.com', 'secure': False, 'name': '__DAYU_PP'}, {'value': '"ADAszE6lUQ2PTvI7CCslX3exT1KAR8HYEQU=|1521597451"', 'httpOnly': False, 'path': '/', 'domain': '.zhihu.com', 'secure': False, 'name': 'd_c0'}, {'value': '9434306e-4760-44e9-b2e7-057203962aa2', 'httpOnly': False, 'path': '/', 'domain': '.zhihu.com', 'secure': False, 'name': '_xsrf'}, {'value': '92c0557c8331402bbea743a60da52255|1521597451000|1521597451000', 'expiry': 1616205451.612256, 'httpOnly': True, 'path': '/', 'domain': '.zhihu.com', 'secure': False, 'name': 'q_c1'}]