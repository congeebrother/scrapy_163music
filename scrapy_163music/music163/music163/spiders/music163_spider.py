# -*- coding: utf-8 -*-
import scrapy


class Music163Spider(scrapy.Spider):
    name = "music163_spider"
    allowed_domains = ["music.163.com"]
    start_urls = (
        'http://www.music.163.com/',
    )

    def parse(self, response):
        pass
