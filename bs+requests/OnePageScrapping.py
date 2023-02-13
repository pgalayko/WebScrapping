import requests
from bs4 import BeautifulSoup as bs

# Получения информации о книгах с одной страницы

get_html = requests.get('https://books.toscrape.com/')
html_soup = bs(get_html.content, 'html.parser')

# Определили, в каком разделе находится информация о книгах на странице и получаем нужную информацию для
# дальнейшего сбора книг
sections = html_soup.select('section')
section = sections[0]

# Получение книг. Определили в каком тэге и в каком классе находится необходимая информация
books_block = section.select_one('ol[class=row]')
books = books_block.select('li')

books_data = list()
for book in books:
    image = 'https://books.toscrape.com/' + book.find('div', attrs={'class': 'image_container'}).find('img')['src']
    title = book.find('h3').find('a')['title']
    price = book.find('p', attrs={'class': 'price_color'}).text

    book_dict = {
        'image': image,
        'title': title,
        'price': price
    }
    books_data.append(book_dict)

print(books_data)
