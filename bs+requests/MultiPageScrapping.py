import requests
from bs4 import BeautifulSoup as bs

get_html = requests.get('https://books.toscrape.com/')

if get_html.status_code == 200:
    soup = bs(get_html.content, 'html.parser')
    next_page = 'https://books.toscrape.com/' + soup.find('li', attrs={'class': 'next'}).find('a')['href']

    get_next_html = requests.get(next_page)


def get_books(content):
    page_soup = bs(content, 'html.parser')
    ol = page_soup.find('ol', attrs={'class': 'row'})
    list_of_books = ol.select('li')

    books_data = list()
    for book in list_of_books:
        image = 'https://books.toscrape.com/' + book.find('div', attrs={'class': 'image_container'}).find('img')['src']
        title = book.find('h3').find('a')['title']
        price = book.find('p', attrs={'class': 'price_color'}).text

        book_dict = {
            'image': image,
            'title': title,
            'price': price
        }
        books_data.append(book_dict)
    return books_data


def get_next_page(content):
    page_soup = bs(content, 'html.parser')
    try:
        next_page_url = 'https://books.toscrape.com/catalogue/' + page_soup.find('li', attrs={'class': 'next'}).find('a')['href']
        return next_page_url
    except:
        pass


final_data = list()
page_number = 1
url = 'https://books.toscrape.com/catalogue/page-1.html'
get_html = requests.get(url)
if get_html.status_code == 200:
    while True:
        books = get_books(get_html.content)
        print(f"Получено {len(books)} с {page_number} страницы")
        final_data += books

        next_page = get_next_page(get_html.content)
        if next_page:
            page_number += 1
            get_html = requests.get(next_page)
            if get_html.status_code == 200:
                print(f'Переходим к странице {page_number}')
        else:
            break
print(f'Получены данные: обработано {page_number} страниц, {len(final_data)} книг')
