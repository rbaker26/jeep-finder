# -*- coding: utf-8 -*-
import scrapy

class ToScrapeCSSSpider(scrapy.Spider):
    name = "jeep_scrape-css"
    start_urls = [
        'https://www.truecar.com/used-cars-for-sale/listings/jeep/location-ladera-ranch-ca/',
    ]

    def parse(self, response):
        cars = response.css("span._176r2bw::text").extract()
        trims = response.css("span.h6._ip7nj36::text").extract()
        prices = response.css("p.price::text").extract()
        vehicle_info = response.css("ul.vehicle-info.list-unstyled").extract()
        #print(vehicle_info)
        for item in zip(cars,trims,prices):


            scraped_info = {
                'year' : item[0][0:4],
                'model' : item[0][10:],
                'trim' : item[1],
                'price': item[2],
                #'vehicle_info' : item[2],
            }
            yield scraped_info

        next_page_url = response.css("ul.pagination").css('a::attr(href)').extract()[-2]
        print(next_page_url)
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
