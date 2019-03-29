# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
# -*- coding: utf-8 -*-
import scrapy
# from scrapy import Request


class Douban_spider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com/']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        print(response.text)