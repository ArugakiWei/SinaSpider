# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy import log
import MySQLdb
from scrapy.conf import settings


class NewsPipeline(object):
    
    def process_item(self, item, spider):


        host = settings['MYSQL_SERVER']
        user = settings['MYSQL_USER']
        psd = settings['MYSQL_PASSWD']
        db = settings['MYSQL_DB']
        c = settings['CHARSET']
        port = settings['MYSQL_PORT']

        con = MySQLdb.connect(host=host,user=user,passwd=psd,db=db,charset=c,port=port)
        cur=con.cursor()
        sql=("insert into news(time,bankuai,title,url,content,wangzhan) "
             "values(%s,%s,%s,%s,%s,%s)")
        lis=[item['time'],item['bankuai'],item['title'],item['url'],item['content'],item['wangzhan']]

        if cur.execute('select url from new where url="%s";' % item['url']) == 0L:

        	try:
        		cur.execute(sql,lis)
        	except Exception,e:
        		print ('Insert error',e)
        		con.rollback()

        	else:
        		con.commit()

        cur.close()
        con.close()
        return item