# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from logging import log


class MySqlPipeline(object):
    def __init__(self):
        # 初始化数据库连接
        self.connect=pymysql.connect(host='localhost',user='root',password='root',db='test',port=3306)
        self.cursor=self.connect.cursor()

    def process_item(self,item,spider):
        print("hello")
        try:
            # 插入数据
            sql = 'insert into movie (num,name,person,year,type,star,remark) values(%s, %s, %s, %s, %s, %s,%s)'
            self.cursor.execute(sql,
                (item['num'],
                 item['movie_name'],
                 item['movie_person'],
                 item['movie_year'],
                 item['movie_type'],
                 item['movie_star'],
                 item['movie_remark']))

            # 提交sql语句
            self.connect.commit()
        except Exception as error:
            # 出现错误时打印错误日志
            log(error)
        return item

    # 关闭数据库
    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()
