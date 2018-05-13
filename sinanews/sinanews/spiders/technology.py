# -*- coding: utf-8 -*-
import scrapy

from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from ..items import NewsItem
import requests
from lxml import etree

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class News_technology_spider(RedisCrawlSpider):

	name = "technology"
	redis_key = 'siannews:technology_urls'


	
	def parse(self,response):

		items = NewsItem()
		items['bankuai'] = 'technology'
		items['wangzhan'] = 'sina'
		title = "title"
		cType = "cType"
		url = "url"
		channel = 'channel'
		pic = "pic"
		time = "time"
		i = 0
		l = eval(response.body.split("list : ")[1].replace("};",""))
		for i in range(len(l)):
			items['url'] = l[i]['url']
			items['title'] = unicode(l[i]['title'],"gbk")
			import time 
			items['time'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(float(l[i]['time'])))
			res = requests.get(items['url'])
			res.encoding = 'utf-8'
			tree=etree.HTML(res.text)
			p = tree.xpath("//p/text()")
			j = 0 
			content = ""
			while j < (len(p)-31):
				content = content + p[j]
				j = j + 1
			items['content'] = content
			yield items
 

