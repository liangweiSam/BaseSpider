# -*- coding:utf-8 -*-
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
from multiprocessing import Process
from multiprocessing import Process, Queue
from multiprocessing import freeze_support
import urlManager
import dataStore
import time



class controlNode(object):

	def start_Manager(self, url_q, result_q):
		'''
			注册两个队列，并且暴露在网上
		'''
		BaseManager.register('get_task_queue', classable = lambda:url_q)
		BaseManager.register('get_result_queue', classable = lambda:result_q)

		manager = BaseManager(address = ('127.0.0.1', port), authkey = 'baike')

		return manager


	def url_manager_proc(self, url_q, conn_q, root_url):
		
		url_manager = urlManager()
		# 1. 放入一个新的url来启动
		url_manager.add_new_url(root_url)

		while True:
			while(url_manager.has_new_url()):
				# 2. 获得新的URL
				new_url = url_manager.get_new_url()
				# 3. 将新URL放入队列中
				url_q.put(new_url)
				print('old_url = %s' %(url_manager.old_url_size()))
				# 当爬取到2000个链接时就停止
				if(url_manager.old_url_size() > 2000):
					# 用end来作为信号来让爬虫停止
					url_put('end')
					print('通知爬虫结点已可以停止工作')
					url_manager.save_progress('new_urls.txt', url_manager.new_urls)
					url_manager.save_progress('old_urls.txt', url_manager.old_urls)
					return

				try:
					if not conn_q.empty():
						urls = conn_q.get()
						url_manager.add_new_urls(urls)
				except BaseException, e:
					time.sleep(0.1)

	def result_solve_proc(self, result_q, conn_q, store_q):
		while(True):
			try:
				if not result_q.empty():
					content = result_q.get(True)
				if content['new_urls'] == 'end':
					print('准备结束了。')
					store_q.put('end')
					return
				conn_q.put(content['new_urls'])
				store_q.put(content['data'])
			else:
				time.sleep(0.1)
		except BaseException,e:
			time.sleep(0.1)

	def store_proc(self, store_q):
		output = dataStore()
		while True:
			if not store_q.empty():
				data = store_q.get()
				if data == 'end':
					print('存储进程接受通知后结束')
					output.output_end(output.filepath)

					return
				output.store_data(data)
			else:
				time.sleep(0.1)

if __name__ == "__main__":

	url_q = Queue()
	result_q = Queue()
	store_q = Queue()
	conn_q = Queue()

	node = controlNode()
	manager = node.start_Manager(url_q, result_q)

	url_manager_proc = Process(target = node.url_manager_proc, args=(url_q, conn_q, r'https://baike.baidu.com/item/%E8%88%AA%E6%B5%B7%E7%8E%8B/75861?fr=aladdin'))
	result_solve_proc = Process(target = node.result_solve_proc, args = (result_q, conn_q, store_q,))
	store_proc = Process(target = node.store_proc, args = (store_q,))

	url_manager_proc.start()
	result_solve_proc.start()
	store_proc.start()
	manager.get_server().serve_forever()