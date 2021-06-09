import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class FundSpiderSelnium(scrapy.Spider):
    name = 'fund_selenium'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def __init__(self):
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')

        # driver = webdriver.Chrome(options=chrome_options)
        # driver.set_window_size(1920, 1080)
        driver = webdriver.Chrome()
        driver.get('https://www.valueresearchonline.com/funds/selector/primary-category/1/equity/?plan-type=direct&tab=snapshot')
        driver.implicitly_wait(25)

        # here html source is a string object; to pass it to parse method
        # it must be converted to a selector object
        self.html = driver.page_source
        # print(self.html)
        # with open('mutual_fund.html', 'w') as f:
        #     f.write(self.html)

    def parse(self, response):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print(response.request.headers['User-Agent'])
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        resp = Selector(text=self.html)
        for row in resp.css('tbody tr[role="row"]'):
            yield{
                'fund_name': row.css('.text-left a::text').get(),
                'NAV': row.css('td:nth-child(10)::text').get()
            }
