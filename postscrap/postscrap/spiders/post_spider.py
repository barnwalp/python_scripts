import scrapy


class PostSpider(scrapy.Spider):
    # name is a string to identify spider
    name = 'posts'

    start_urls = [
        'https://blog.scrapinghub.com/page/1/',
        'https://blog.scrapinghub.com/page/2/'
    ]
    # default callback to process donwload responses when their
    # request dont specifies callback

    def parse(self, response):
        page = response.url.split('/')[-1]
        filename = 'posts-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
