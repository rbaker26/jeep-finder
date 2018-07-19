# -*- coding: utf-8 -*-
import scrapy

class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'https://www.truecar.com/used-cars-for-sale/listings/jeep/location-ladera-ranch-ca/',
    ]

    def parse(self, response):

        cars = response.css("span._176r2bw::text").extract()
        trims = response.css("span.h6._ip7nj36::text").extract()
        prices = response.css("p.price::text").extract()
        #vehicle_info = response.css("ul.vehicle-info.list-unstyled::text").extract()


        for item in zip(cars,trims,prices):
            #create a dictionary to store the scraped info
            scraped_info = {
                'year' : item[0][0:4],
                'car' : item[0][4:],
                'trim' : item[1],
                'price': item[2],
                #'vehicle_info' : item[2],
            }
            yield scraped_info

        # index = 0
        # for car in response.css("div.search-results"):
        #     car = {
        #         'car': car.css("span._176r2bw::text").extract()[index],
        #         'trim': car.css("span.h6._ip7nj36::text").extract()[index],
        #         # 'author': car.css("small.author::text").extract_first(),
        #         # 'tags': car.css("div.tags > a.tag::text").extract()
        #     }
        #     index = index + 1
        #     cars.append(car)

        # return cars

        # nextTHing = response.css("ul.pagination").extract()

        next_page_url = response.css("ul.pagination").css('a::attr(href)').extract()[-2]
        # print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        # print(nextTHing)
        # print('****')
        print(next_page_url)
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
