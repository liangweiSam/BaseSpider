# -*- coding:utf-8 -*-
from lxml import etree
from bs4 import BeautifulSoup
import urllib


class htmlParser(object):

	def parse(self, page_url,response_text):

		result = etree.HTML(response_text)

		
	def _get_new_urls(self, page_url, result):
		'''
			需要原url， 因为现在很多网页都采用相对url
			这边的编写需要根据要采取的网页来修改
		'''
		new_urls = set()
		links = result.xpath('//a/@href')
		for link in links:
			if 'item' in link:
				new_full_url = urllib.parse.urljoin(page_url, link)
				new_urls.add(new_full_url)

		return new_urls

	def _get_new_data(self, page_url, result):
		'''
			beautifulSoup.get_text() 可以获取名下标签的text
		'''
		soup = BeautifulSoup(result, 'lxml')

		data = {}
		data['url'] = page_url

		title = soup.find('dd', class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
		data['title'] = title.get_text()

		summary = soup.find('div', class_ = 'lemma-summary')
		data['summary'] = summary.get_text()

		return data


