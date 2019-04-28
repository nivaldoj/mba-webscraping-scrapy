import scrapy

class MercadoLivreProdutosSpider(scrapy.Spider):

    # scrapy runspider MercadoLivreProdutosSpider.py -a product="Caixa de Som"
    name = "mercado-livre"

    # https://blog.scrapinghub.com/2016/08/25/how-to-crawl-the-web-politely-with-scrapy
    custom_settings = {
        "AUTOTHROTTLE_ENABLED": True,
        "HTTPCACHE_ENABLED": True,
    }

    # https://stackoverflow.com/questions/15611605/how-to-pass-a-user-defined-argument-in-scrapy-spider
    def __init__(self, product="", *args, **kwargs):
        self.start_urls = ["https://lista.mercadolivre.com.br/{}".format(product)]
        super(MercadoLivreProdutosSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        for product in response.css(".item__info-container > div"):
            product_name = product.css(".main-title::text").extract_first().strip()
            product_price = " ".join(product.css(".item__price > span::text").extract())

            yield {
                "nome" : product_name,
                "preco" : product_price
            }

        pagination = response.xpath("//ul[@role]/li[last()]/a")

        if pagination.css("span::text").extract_first() == "Próxima":
            yield scrapy.Request(url=pagination.xpath("@href").extract_first(), 
                                 callback=self.parse)
