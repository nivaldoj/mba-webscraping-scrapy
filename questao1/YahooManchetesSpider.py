import scrapy

class YahooManchetesSpider(scrapy.Spider):

    name = "yahoo-manchetes"
    start_urls = [
        "https://br.yahoo.com/"
    ]

    def parse(self, response):
        #scrapy.utils.response.open_in_browser(response)

        # manchetes (caroussel)
        for item in response.css("img + h3::text").extract():
            yield {"titulo": item}

        # notícias (meio da página)
        for item in response.xpath("//a/span[not(@class)]/text()").extract():
            yield {"titulo": item}
        
        # destaques (lado direito da página)
        for item in response.css("a ~ ul > li > a > div > div::text").extract():
            yield {"titulo": item}
