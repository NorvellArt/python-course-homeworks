import requests
from bs4 import BeautifulSoup
import re
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def nbsp_delete(string):
    res = re.sub(r'\xa0', ' ', string)
    return res


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    products = soup.find_all('div', class_='product_data__gtm-js')
    for product in products:
        smartphone_name = product.find('a', class_='ProductCardHorizontal__title').text
        print(smartphone_name)
        smartphone_code = product.find('div', class_='ProductCardHorizontal__vendor-code').text.strip()
        print(smartphone_code)
        print('=' * 50)
        data = {'name': smartphone_name, 'code': nbsp_delete(smartphone_code)}
        write_csv(data)


def write_csv(data):
    with open('smartphones.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator='\r')
        writer.writerow((data['name'], data['code']))


def main():
    url = 'https://www.citilink.ru/catalog/smartfony/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
