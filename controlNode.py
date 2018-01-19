# -*- coding:utf-8 -*-
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
import queue



class controlNode(object):

	def start_Manager(self, url_q, result_q):
		'''
			注册两个队列，并且暴露在网上
		'''
		BaseManager.register('get_task_queue', classable = lambda:url_q)
		BaseManager.register('get_result_queue', classable = lambda:result_q)

		manager = QueueManager(address = ('127.0.0.1', port), authkey = key)

		return manager


	def url_manager_proc(self, url_q, conn_q, root_url):
		

