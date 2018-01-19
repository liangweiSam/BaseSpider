# -*- coding:utf-8 -*-
import requests



class htmlDownloader(object):


	def download(self, url):	
		'''
			下载页面
		'''
		if url is None:
			return None
		headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4033.400 QQBrowser/9.6.12624.400'}
		response = requests.get(url = url, headers = headers)

		if response.status_code == 200:
			response.encoding = 'utf-8'
			return response.text.encode('utf-8').decode('utf-8', 'ignore')
		
		return None


