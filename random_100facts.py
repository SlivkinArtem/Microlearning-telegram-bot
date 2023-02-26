import requests
from bs4 import BeautifulSoup
from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.add_argument('headless')
browser = webdriver.Chrome(options=opt,  # executable_path=r'F:\Тёма\Проект микрообучение\chromedriver.exe')
                           executable_path=r'C:\Users\КВАНТОРИАНЕЦ\Desktop\Проект микрообучение\chromedriver.exe')


def get_html(url):
    html_code = requests.get(url)
    return html_code.text


def parse(html_code):
    soup = BeautifulSoup(html_code, 'lxml')
    facts = soup.find('div', class_='entry-content cf').find_all('p')

    for fact in facts[1:]:
        print(fact.text)


if __name__ == '__main__':
    html = get_html('https://100-faktov.ru/100-interesnyx-faktov-o-kosmose/')
    parse(html)
