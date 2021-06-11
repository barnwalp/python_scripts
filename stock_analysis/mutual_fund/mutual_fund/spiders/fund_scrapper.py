from scrapy.selector import Selector
from selenium import webdriver


class FundScrapper:
    def __init__(self):
        links = {
            'snapshot': 'https://www.valueresearchonline.com/funds/selector/primary-category/1/equity/?plan-type=direct&tab=snapshot',
            'returns': 'https://www.valueresearchonline.com/funds/selector/primary-category/1/equity/?plan-type=direct&tab=returns-long-term',
            'risk': 'https://www.valueresearchonline.com/funds/selector/primary-category/1/equity/?plan-type=direct&tab=risk-stats',
            'fee': 'https://www.valueresearchonline.com/funds/selector/primary-category/1/equity/?plan-type=direct&tab=fee-details',
        }
        self.links = links

    def parse(self):
        driver = webdriver.Chrome()
        driver.get(self.links['snapshot'])
        driver.implicitly_wait(25)
 
        resp = Selector(text=driver.page_source)
        for row in resp.css('tbody tr[role="row"]'):
            yield{
                'fund_name': row.css('.text-left a::text').get(),
                'NAV': row.css('td:nth-child(10)::text').get()
            }
        driver.close()
        self.parse_returns()
    
    def parse_returns(self):
        driver = webdriver.Chrome()
        driver.get(self.links['returns'])
        driver.implicitly_wait(25)
 
        resp = Selector(text=driver.page_source)
        for row in resp.css('tbody tr[role="row"]'):
            yield{
                'fund_name': row.css('.text-left a::text').get(),
                '3_year_return': row.css('td:nth-child(2)::text').get(),
            }
        driver.close()
        self.parse_risk()
    
    def parse_risk(self):
        driver = webdriver.Chrome()
        driver.get(self.links['risk'])
        driver.implicitly_wait(25)
 
        resp = Selector(text=driver.page_source)
        for row in resp.css('tbody tr[role="row"]'):
            yield{
                'fund_name': row.css('.text-left a::text').get(),
                'std_deviation': row.css('td:nth-child(5)::text').get(),
                'sharpe_ratio': row.css('td:nth-child(6)::text').get(),
                'sortino_ratio': row.css('td:nth-child(7)::text').get(),
                'beta': row.css('td:nth-child(8)::text').get(),
                'alpha': row.css('td:nth-child(9)::text').get(),
                'r_squared': row.css('td:nth-child(10)::text').get(),
            }
        driver.close()
        self.parse_fee()

    def parse_fee(self):
        driver = webdriver.Chrome()
        driver.get(self.links['fee'])
        driver.implicitly_wait(25)
 
        resp = Selector(text=driver.page_source)
        for row in resp.css('tbody tr[role="row"]'):
            yield{
                'fund_name': row.css('.text-left a::text').get(),
                'expense_ratio': row.css('td:nth-child(3)::text').get(),
                'exit_load': row.css('td:nth-child(4)::text').get(),
                'fund_manager': row.css('td:nth-child(5)::text').get(),
            }
        driver.close()


if __name__ == '__main__':
    spider = FundScrapper()
    for val in spider.parse():
        print(val)
