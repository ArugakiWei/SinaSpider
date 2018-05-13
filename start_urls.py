# -*- coding: utf-8 -*-

import os
import sys


def main():

	for i in range(10):

		os.system('redis-cli lpush siannews:china_urls  "http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page="' + str(i+1))
		os.system('redis-cli lpush siannews:society_urls  "http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=shxw&cat_2==zqsk||=qwys||=shwx||=fz-shyf&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page="' + str(i+1))
		os.system('redis-cli lpush siannews:entertainment_urls  "http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=95&spec=&type=&ch=01&k=&offset_page=0&offset_num=0&num=60&asc=&page="' + str(i+1))
		os.system('redis-cli lpush siannews:sport_urls  "http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=94&spec=&type=&ch=01&k=&offset_page=0&offset_num=0&num=60&asc=&page="' + str(i+1))
		os.system('redis-cli lpush siannews:technology_urls  "http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=96&spec=&type=&ch=01&k=&offset_page=0&offset_num=0&num=60&asc=&page="' + str(i+1))
		os.system('redis-cli lpush siannews:finace_urls  "http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=97&spec=&type=&ch=01&k=&offset_page=0&offset_num=0&num=60&asc=&page="' + str(i+1))
		os.system('redis-cli lpush siannews:foreign_urls  "http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gjxw&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page="' + str(i+1))
		os.system('redis-cli lpush siannews:war_urls "http://roll.mil.news.sina.com.cn/col/zgjq/index_%s.shtml"' % str(i+1) )

main()