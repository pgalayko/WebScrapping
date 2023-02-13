from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# Создавая данного, указываем название шаблона - scrapy genspider -t crawl pages_crawl http://books.toscrape.com
# Задача: Собрать все 1000 книг, помимо 3 параметров, собрать описание и код UPC
class PagesCrawlSpider(CrawlSpider):
    name = "pages_crawl"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    # В LinkExtractor добавляем xpath до ссылки на конкретную книгу
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//article[@class='product_pod']/h3/a"), callback="parse_item", follow=True),
        # Для получения всех книг, добавляем xpath для ссылки на следующую страницу
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"))
    )

    def parse_item(self, response):
        item = {}
        item["title"] = response.xpath("//div[contains(@class, 'product_main')]/h1/text()").get()
        item["price"] = response.xpath("//div[contains(@class, 'product_main')]/p[@class='price_color']/text()").get()
        # Метод .getall() позваляет получать список элементов
        item["image"] = response.xpath('//div[@id="product_gallery"]/div[@class="thumbnail"]/div['
                                       '@class="carousel-inner"]/div[contains(@class, item)]/img/@src').getall()
        # /.. используется для того, чтобы перейти к следующему элементу
        item["description"] = response.xpath("//div[@id='product_description']/../p/text()").get()
        item["upc"] = response.xpath("//th[contains(text(), 'UPC')]/../td/text()").get()
        return item
