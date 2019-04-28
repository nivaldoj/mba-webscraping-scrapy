import scrapy 

class UolCotacaoSpider(scrapy.Spider):

    name = "uol-cotacao"
    start_urls = [
        "https://www.uol.com.br/"
    ]

    # scrapy runspider UolCotacaoSpider.py --nolog
    custom_settings = {
        "LOG_ENABLED" : False
    }

    def parse(self, response):
        currency = response.css(".currency_quote__down::text").extract_first()
        print("A cotação atual do dólar é: {}".format(currency))