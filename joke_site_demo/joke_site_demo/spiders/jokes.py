from scrapy import Spider, Request
from scrapy.loader import ItemLoader
from joke_site_demo.items import JokeItem


class JokesSpider(Spider):
    name = "jokes"
    start_urls = ["http://www.laughfactory.com/jokes/science-jokes"]

    def parse(self, response):
        for joke in response.xpath("//div[@class='jokes']"):
            l = ItemLoader(item=JokeItem(), selector=joke)
            l.add_xpath("joke_text", ".//div[@class='joke-text']/p")
            yield l.load_item()
            #yield {
            #    "joke_text": joke.xpath(".//div[@class='joke-text']/p").extract_first()
            #}

        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_page is not None:
            yield response.follow(url=next_page, callback=self.parse)
