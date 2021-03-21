import scrapy


class NflSpider(scrapy.Spider):
    name = 'nfl'
    start_urls = [
        'https://www.nfl.com/players/active/a'
    ]
    """
    To select the selected dropdown in option tag
    //*[@id='year-dropdown']//option[@selected]//text()
    """

    def parse(self, response):
        row = response.css('.d3-o-table--horizontal-scroll table')
        items = {
            'player': row.xpath("//tr//td[1]//div//a//text()").getall(),
            'team': row.xpath("//tr//td[2]//text()").getall()
        }

        # Removing extra white spaces and newline characters from items
        data = dict()
        for key, value in items.items():
            li = []
            for val in value:
                li.append(val.strip())
            data[key] = li
        yield data
        next_page = response.css(
            '.nfl-o-table-pagination__buttons a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
