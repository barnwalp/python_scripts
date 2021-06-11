from scrapy.selector import Selector
from selenium import webdriver


class FundScrapper:
    def __init__(self):
        driver = webdriver.Chrome()
        driver.get('https://www.valueresearchonline.com/funds/selector/primary-category/1/equity/?plan-type=direct&tab=snapshot')
        driver.implicitly_wait(25)
        self.html = driver.page_source

    # This is a generator not a method
    def parse(self):
        resp = Selector(text=self.html)
        for row in resp.css('tbody tr[role="row"]'):
            yield{
                'fund_name': row.css('.text-left a::text').get(),
                'NAV': row.css('td:nth-child(10)::text').get()
            }

if __name__ == '__main__':
    spider = FundScrapper()
    for val in spider.parse():
        print(val)
