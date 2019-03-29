# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 序号
    num = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 参演人员
    movie_person = scrapy.Field()
    # 年份
    movie_year = scrapy.Field()
    # 类型
    movie_type = scrapy.Field()
    # 星
    movie_star = scrapy.Field()
    # 说明
    movie_remark = scrapy.Field()
