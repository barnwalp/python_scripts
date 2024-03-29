import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
import re
from scrapy.shell import inspect_response



class FundSpider(scrapy.Spider):
    name = 'fund'
    def start_requests(self):
        yield SeleniumRequest(
            url = 'https://www.valueresearchonline.com/funds/selector/primary-category/1/equity/?plan-type=direct&tab=snapshot',
            # url = 'https://quotes.toscrape.com/',
            wait_time = 5,
            screenshot=True,
            callback=self.parse,
        )

    def parse(self, response):
        # view(response)
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print(response.request.headers['User-Agent'])
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        inspect_response(response, self)
        # data = response.css('#selector-tab li a::text').getall()
        # row_list = dict()
        # for index, value in enumerate(data):
        #     row_list[index] = value
        # yield row_list