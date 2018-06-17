# -*- coding: utf-8 -*-
import scrapy
from onepiece.items import OnepieceItem
from scrapy import Request


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['http://sakuramanga.net/truyen-tranh-tieng-nhat-japanese-manga/one-piece-truyen-tranh-tieng-nhat/']

    def parse(self, response):
        list = response.xpath('//*[@id="blog-wrapper"]/article/header/div/a/@href').extract()

        for url in list:
            print(url)
            yield Request(url, callback=self.parse_item, dont_filter=True)

    def parse_item(self, response):
        print("---------parse item----------")
        titles = response.xpath('//*[@class="entry-content"]/p/img/@src').extract()
        imgs = response.xpath('//*[@class="entry-content"]/img/@src').extract()

        chapter = response.xpath('//*[@class="entry-title"]/text()').extract()
        c = ''.join(chapter)
        c = c.strip()
        print(c)
        item = OnepieceItem()
        item['chapter'] = c
        item['image_urls'] = imgs + titles

        return item
