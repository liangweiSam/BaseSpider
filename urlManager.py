# -*- coding:utf-8 -*-
import pickle
import hashlib

class urlManager(object):

	def __init__(self):
		self.new_urls = set()
		self.old_urls = set()


	def has_new_url(self):
		'''
			是否有新的url
		'''
		return has_new_url() > 0


	def new_Urls_size(self):
		'''
			新url的数量
		'''
		return len(self.new_urls)


	def old_Uels_size(self):
		'''
			已用过的url的数量
		'''
		return len(self.old_urls)

	def get_new_url(self):
		'''
			用过的url就要放入old_url中
		'''
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url

	def add_new_url(self, url):
		'''
			此处为去重，排除url在new_urls和old_urls中
		'''
		if url is None:
			return
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)

	def add_new_urls(self, urls):
		'''
			此处要判定urls的合法性
		'''
		if urls is None or len(urls) == 0:
			return
		for url in urls:
			add_new_url(url)

	def save_progress(self, path, data):

		with open(path, 'wb') as f:
			pickle.dump(data, f)


	def load_progress(self, path):

		print('[+] 从文件加载进度：%s' %path)
		try:
			with open(path, 'rb') as f:
				tmp = pickle.load(f)
				return tmp
		except:
			print('[!] 无进度文件， 创建：%s' %path)
		# 这一块是当有异常时会执行，except，并且执行return set()
		return set()