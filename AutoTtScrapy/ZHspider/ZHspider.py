# -*- coding:utf-8 -*-
import requests
from lxml import etree
import re
import time
import sys, io
import hmac
import json
from hashlib import sha1

class ZHspider(object):

	def __init__(self):
		self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
						'authorization':'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}
		# self.headers = {
		# 				'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36',
		# 				'authorization' : 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'
		# 				}

	def start_url(self, session):
		response = session.get('https://www.zhihu.com/signup', headers = self.headers)
		response2 = session.get('https://www.zhihu.com/api/v3/oauth/captcha?lang=cn',  headers = self.headers)
		return response, response2, session

	def get_signature(self, clientId, grantType, timestamp, source):
		hm = hmac.new(b'd1b964811afb40118a12068ff74a12f4', None, sha1)
		hm.update(str.encode(grantType))
		hm.update(str.encode(clientId))
		hm.update(str.encode(source))
		hm.update(str.encode(timestamp))

		return str(hm.hexdigest())

	def login(self, xsrftoken, d_c0, session):
		headers = {
				'User-Agent' : r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36',
				'Referer' : r'https://www.zhihu.com/signup?next=%2F',
				'accept': 'application/json, text/plain, */*', 
				'Accept-Encoding' : 'gzip, deflate, br', 
				'Accept-Language' : 'zh-CN,zh;q=0.8', 
				'x-xsrftoken' : xsrftoken, 
				'Origin' : 'https://www.zhihu.com', 
				'authorization' : 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'
				}

	
		if d_c0 is not None and d_c0 is not '':
			headers['x-udid'] = d_c0

		clientId = 'c3cef7c66a1843f8b3a9e6a1e3160e20'
		timestamp = str(int(time.time()*1000))
		grantType = 'password'
		source = 'com.zhihu.web'

		data = {
				'client_id' : clientId,
				'grant_type' : grantType,
				'timestamp' : timestamp,
				'source' : source,
				'signature' : self.get_signature(clientId, grantType, timestamp, source),
				'lang' : 'cn', 
				'ref_source' : 'other_',  
				'utm_source' : 'baidu', 
				'username' : '13242311433',
				'password' : 'xieyueying1', 
				'captcha' : None,
		}

		print('%s ' %(data))


		response = session.post('https://www.zhihu.com/api/v3/oauth/sign_in', data, headers=self.headers)
		print(response)
		response1 = session.get('https://www.zhihu.com/', headers=self.headers)
		print(response1.content.decode('utf-8', 'ignore'))

if __name__ == '__main__':
	sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
	session = requests.Session()

	zhS = ZHspider()
	response, response2, sessiona = zhS.start_url(session)
	cookies = response.cookies
	xsrftoken = cookies.get('_xsrf')
	d_c0 = ''
	if cookies.get('d_c0') is not None:
		d_c0_group = re.search(r'"(.+=)|', cookies.get('d_c0'))
		if d_c0_group is not None:
			# print('提取d_c0..%s' %(d_c0_group.group(1)))
			d_c0 = d_c0_group.group(1)


	if json.loads(response2.text)['show_captcha'] is False:
		zhS.login(xsrftoken, d_c0, sessiona)
	else:
		print(json.loads(response2.text)['show_captcha'])






	# headers = response.headers
	# middle = headers['Set-Cookie'].split(';')
	# xsrftoken = ''
	# for i in middle:
	# 	xsrftoken_group = re.search('_xsrf=(.*)', i)
	# 	if xsrftoken_group is not None:
	# 		print('提取xsrf字符 %s..' %(xsrftoken_group.group(1)))
	# 		xsrftoken = xsrftoken_group.group(1)

	# zhS.login(xsrftoken)
	






'''
	{'X-DAYU-UUID': 'D7PR299A6643274F4FE0A8180514EA5D82F9', 
	'Set-Cookie': '__DAYU_PP=FVVqeFvAerZ6FJIfz77a29519bc7a1f3; Expires=Wed, 09 Jun 2021 23:59:59 GMT; Path=/, _xsrf=fa65cdaf-061f-483c-ad87-6fb5337a5a75; path=/; domain=.zhihu.com, q_c1=1c14f589156a461abb0cf616ccc7a698|1521426454000|1521426454000; path=/; expires=Thu, 18 Mar 2021 02:27:34 GMT; domain=zhihu.com; httponly', 
	'Content-Encoding': 'gzip', 'Connection': 'keep-alive', 
	'X-Req-SSL': 'proto=TLSv1.2,sni=api.zhihu.com,cipher=ECDHE-RSA-AES256-GCM-SHA384',
	 'Date': 'Mon, 19 Mar 2018 02:27:34 GMT', 
	 'Cache-Control': 'private,no-store,max-age=0,no-cache,must-revalidate,post-check=0,pre-check=0', 
	 'Content-Security-Policy': "default-src * blob:;img-src * data: blob:;frame-src 'self' *.zhihu.com getpocket.com note.youdao.com safari-extension://com.evernote.safari.clipper-Q79WDW8YH9 weixin: zhihujs: v.qq.com v.youku.com www.bilibili.com *.vzuu.com;script-src 'self' *.zhihu.com *.google-analytics.com zhstatic.zhihu.com res.wx.qq.com 'unsafe-eval' unpkg.zhimg.com unicom.zhimg.com blob:;style-src 'self' *.zhihu.com unicom.zhimg.com 'unsafe-inline';connect-src * wss:", 'X-Proxy': 'dayu-proxy', 'Expires': 'Fri, 02 Jan 2000 00:00:00 GMT', 'Vary': 'Accept-Encoding', 'Pragma': 'no-cache', 'Content-Type': 'text/html; charset=utf-8', 'X-Backend-Server': 'heifetz.heifetz.33cdeb45---10.3.30.2:31007[10.3.30.2:31007]', 'Transfer-Encoding': 'chunked', 'X-Frame-Options': 'DENY', 'X-Req-ID': '65813885AAF2016'}

'''