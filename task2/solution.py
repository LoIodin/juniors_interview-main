import csv
import requests
from bs4 import BeautifulSoup


def find_all_animals_by_letter(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'xml')
    tag = soup.find_all('div', class_='mw-category mw-category-columns')
    for child in tag[0].children:
        first_letter = child.h3.get_text()
        count = len(child.find_all('a'))
        if first_letter in amount_of_animal:
            amount_of_animal[first_letter] += count
        else:
            amount_of_animal[first_letter] = count

    next_page(soup)


def next_page(soup):
    if soup.find('a', string='Следующая страница'):
        url_next_page = 'https://ru.wikipedia.org/' + soup.find('a', string='Следующая страница').get('href')
        find_all_animals_by_letter(url_next_page)
    else:
        return


amount_of_animal = {}
url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
find_all_animals_by_letter(url)
print(amount_of_animal)

with open('beasts.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    for item in amount_of_animal.items():
        csvwriter.writerow(item)
