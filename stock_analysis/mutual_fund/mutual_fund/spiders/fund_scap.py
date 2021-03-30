
import scrapy


class FundSpider(scrapy.Spider):
    name = 'fund'
    start_urls = [
        'https://www.valueresearchonline.com/funds/selector/primary-category/1/equity/?plan-type=direct&tab=snapshot'
    ]

    """
    Getting the table th data in https://www.w3schools.com/html/html_tables.asp
    response.xpath('//*[@id="customers"]/tr/td/text()').getall()

    Getting the selector of center-block class in value research online site
    response.xpath("//*[contains(concat(' ', normalize-space(@class), ' '), ' center-block ')]").getall()
    """
    def parse(self, response):
        # data = response.css("tbody tr[role='row'] td:first-of-type a::text").getall()
        data = response.css('#selector-tab li a::text').getall()
        # Since data is an list, it can not be returned by scrapy.
        # it can either be request, item or None
        row_list = dict()
        for index, value in enumerate(data):
            row_list[index] = value
        yield row_list

    # scraping dynamic website using javascript