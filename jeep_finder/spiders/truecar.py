# -*- coding: utf-8 -*-
import scrapy


class TruecarSpider(scrapy.Spider):
    name = "truecar"
    allowed_domains = ["https://www.truecar.com/"]
    start_urls = (
        'http://www.https://www.truecar.com//',
    )

    def parse(self, response):
        pass
