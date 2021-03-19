
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
        for quote in response.css('.row .col-md-8 .quote'):
            yield{
                'post': quote.css('span.text::text').get(),
                'author': quote.css('.author::text').get(),
                'tags': quote.css('.keywords').attrib['content']
            }
        next_page = response.css('.pager a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
