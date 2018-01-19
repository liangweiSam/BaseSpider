# -*- coding:utf-8 -*-
import time
import codecs

class dataStore(object):

	def __init__(self):
		self.filepath = 'baike_%s.html' %(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))

		self.datas = []


	def store_data(self, data):
		if data is None:
			return
		self.datas.append(data)

	def output_head(self, path):

		with codecs.open(path, 'w', encoding = 'utf-8') as fout:
			fout.write('<html>')
			fout.write('<body>')
			fout.write('<table>')

	def output_html(self, path):
		
		with codecs.open(path, 'a', encoding = 'utf-8') as fout:
			for data in self.datas:
				fout.write('<tr>')
				fout.write('<td>%s</td>' %(data['url']))
				fout.write('<td>%s</td>' %(data['title']))
				fout.write('<td>%s</td>' %(data['summary']))
				fout.write('<tr>')			

				self.datas.remove(data)

	def output_end(self.path):
		with codecs.open(path, 'a', encoding = 'utf-8') as fout:
			fout.write('</table>')
			fout.write('</body>')
			fout.write('</html>')
