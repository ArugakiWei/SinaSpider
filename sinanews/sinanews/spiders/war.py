# -*- coding: utf-8 -*-
import scrapy

from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from ..items import NewsItem
import time
import requests
import Queue
from lxml import etree

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class News_war_spider(RedisCrawlSpider):

	name = "war"
	redis_key = 'siannews:war_urls'

	
	def parse(self,response):

		items = NewsItem()
		items['bankuai'] = 'war'
		items['wangzhan'] = 'sina'
		linknews = response.xpath('//div[@class="fixList"]//ul[@class="linkNews"]/li')
		print len(linknews)
		i =0 
		for new in linknews:
			items['title'] = new.xpath('a/text()').extract()[0]
			items['url']  = new.xpath('a/@href').extract()[0]
			items['time'] = new.xpath('//span/text()').extract()[0]
			res = requests.get(items['url'])
			res.encoding = 'utf-8'
			tree=etree.HTML(res.text)
			p = tree.xpath("//p/text()")
			j = 0 
			content = ""
			while j < (len(p)-25):
				content = content + p[j]
				j = j + 1
			items['content'] = content
			yield items

 

