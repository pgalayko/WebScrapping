import scrapy


# Перед началом, создаем необходимые для scrapy файлы путем команды scrapy startproject book(название)
# Далее, создаем паука, используя команду scrapy genspider books_crawl <необходимая ссылка> без s в http и до домена
# В созданном файле паука, дописываем необходимую нам логику по обработке страницы
# Для запуска работы scrapy используем команду scrapy crawl < название паука>
# Для сохранения полученных после парсинга данных используем -o с указанием названия и типа файла (json, csv) books.csv
# Задача: получить название, картинку и цену книг с первой страницы
class BooksCrawlSpider(scrapy.Spider):
    name = "books_crawl"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        books = response.xpath('//ol[@class="row"]/li')
        for book in books:
            yield {
                'image': book.xpath(".//div[@class='image_container']/a/img/@src").get(),
                'title': book.xpath(".//h3/a/@title").get(),
                'price': book.xpath(".//p[@class='price_color']/text()").get()
            }

