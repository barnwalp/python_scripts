import scrapy


class NflSpider(scrapy.Spider):
    name = 'nfl'
    start_urls = [
        'https://www.nfl.com/players/active/a'
    ]
    # To select the selected dropdown in option tag
    # //*[@id='year-dropdown']//option[@selected]//text()
    
    def parse(self, response):
        # checking the response header for ip address
        # print(f'### PRINTING HEADER FROM PARSE METOD ### {response.headers}')
        links = response.css(".d3-o-tabs__list-item a::attr(href)").getall()[1:]
        for link in links:
            next_link = response.urljoin(link)
            yield scrapy.Request(next_link, callback=self.parse_links)

    def parse_links(self, response):
        rows = response.css('.d3-o-table--horizontal-scroll table tbody tr')
        for row in rows:
            yield{
                'player': (row.css("td:nth-of-type(1) a::text").get()).strip(),
                'team': (row.css("td:nth-of-type(2)::text").get()).strip()
            }
        # Xpath selector
        # items = {
        #     'player': row.xpath("//tr//td[1]//div//a//text()").getall(),
        #     'team': row.xpath("//tr//td[2]//text()").getall()
        # }
        next_page = response.css(
            '.nfl-o-table-pagination__buttons a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_links)
