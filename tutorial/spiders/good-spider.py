import scrapy


class WildSpider(scrapy.Spider):
    name = 'good'

    # start_urls = ['https://www.wildberries.ru/catalog/8558114/detail.aspx']
    start_urls = ['https://www.wildberries.ru/catalog/8558114/detail.aspx?targetUrl=SG']
    # start_urls = ['https://www.wildberries.ru/catalog/8558114']

    def parse(self, response):
        self.logger.info('===============START PARSE GOOD======================')
        # articles = response.css('div.article')
        # for article in articles:
        #     yield {
        #         'article': article.css('.span.j-article::text)').get(),
        #     }

        yield {
            'article': response.css('span.j-article::text').get(),
        }
        self.logger.info('===============END PARSE GOOD======================')
