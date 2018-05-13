# -*- coding: utf-8 -*-
import scrapy

from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from ..items import NewsItem
import json
import time
import requests
import Queue
from lxml import etree
import threading

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class News_society_spider(RedisCrawlSpider):


	name = "society"
	redis_key = 'siannews:society_urls'

	
	def parse(self,response):

		items = NewsItem()
		jdict = json.loads(response.body)
		result = jdict['result']
		data = result['data']
		for e in data:

			items['title'] = e['title']
			items['url']   =  e['url']
			items['time']  = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(float(e['createtime'])))
			items['bankuai'] = 'Society'
			items['wangzhan'] = 'sina'
			response = requests.get(e['url'])
			response.encoding = 'utf-8'
			tree=etree.HTML(response.text)
			p = tree.xpath("//p/text()")
			j = 0 
			content = ""
			while j < (len(p)-7):
				content = content + p[j]
				j = j + 1
			items['content'] = content
			yield items
