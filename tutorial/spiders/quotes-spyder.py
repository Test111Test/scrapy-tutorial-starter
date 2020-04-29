import scrapy
from tutorial.items import QuoteItem
from scrapy.loader import ItemLoader


class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        self.logger.info('hello this my first spider')
        quotes = response.css('div.quote')

        # Version 1.0
        # for quote in quotes:
        #     yield {
        #         'text': quote.css('.text::text').get(),
        #         'author': quote.css('.author::text').get(),
        #         'tags': quote.css('.tag::text').getall(),       # change get() to getall()
        #     }

        # Version 1.1
        # quote_item = QuoteItem()
        # for quote in quotes:
        #     quote_item['quote_content'] = quote.css('.text::text').get()
        #     quote_item['tags'] = quote.css('.tag::text').getall()

        # Version 1.2
        for quote in quotes:
            loader = ItemLoader(item=QuoteItem(), selector=quote)
            loader.add_css('quote_content', '.text::text')
            loader.add_css('tags', '.tag::text')
            quote_item = loader.load_item()

            author_url = quote.css('.author + a::attr(href)').get()
            self.logger.info('get author page url')
            # go to author page
            yield response.follow(author_url, callback=self.parse_author)

        # Version 2.1
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
        #
        # Version 2.2
        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)

    def parse_author(self, response):
        yield {
            'author_name': response.css('.author-title::text').get(),
            'author_birthday': response.css('.author-born-date::text').get(),
            'author_bornlocation': response.css('.author-born-location::text').get(),
            'author_bio': response.css('.author-description::text').get(),
        }





