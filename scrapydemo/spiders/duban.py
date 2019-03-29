# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
# -*- coding: utf-8 -*-
import scrapy
from scrapydemo.items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        # print(response.text)
        li_list = response.xpath("//div[@id='content']//ol[@class='grid_view']/li")
        for li in li_list:
            douban_item = DoubanItem()
            num = li.xpath(".//div[@class='pic']/em/text()").extract_first()
            douban_item['num'] = num
            name = li.xpath(".//div[@class='info']//span[@class='title'][1]/text()").extract_first()
            douban_item['movie_name'] = name
            list = li.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            person = ''.join(list[0].split())
            douban_item["movie_person"] = person
            a = ''.join(list[1].split()).split("/")
            douban_item["movie_year"] = a[0]
            del a[0]
            douban_item["movie_type"] = "-".join(a)
            star = li.xpath(".//div[@class='info']//div[@class='star']/span[@class='rating_num']/text()").extract_first()
            douban_item["movie_star"] = star
            remark = li.xpath(".//div[@class='info']//p[@class='quote']/span[@class='inq']/text()").extract_first()
            douban_item["movie_remark"] = remark
            print(douban_item)
            # 需要将数据yield到pipelines里面去
            yield douban_item

        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            # ,dont_filter=True
            # yield scrapy.Request("https://movie.douban.com/top250" + next_link[0],callback=self.parse)
            yield scrapy.Request(response.urljoin(next_link[0]),callback=self.parse)




