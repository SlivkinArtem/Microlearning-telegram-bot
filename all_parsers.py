import os
import random
from random import choice

import requests
from bs4 import BeautifulSoup
from loguru import logger
from selenium import webdriver


def parse_indicator():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    browser = webdriver.Chrome(options=opt, executable_path=r'drivers\chromedriver.exe')

    if not os.path.exists('indicator'):
        os.mkdir('indicator')
        os.mkdir('indicator/pictures')

    def big_articles(url):
        browser.get(url)
        code = browser.page_source
        soup = BeautifulSoup(code, 'lxml')
        big_articles = ['https://indicator.ru' + elem.find('a').get('href') for elem in
                        soup.find_all('div', class_='jsx-3628860864 hero _2TUd5iHO')]
        random_article = choice(big_articles)
        logger.debug(f'Ссылка на случайную статью: {random_article}')
        browser.get(random_article)
        return browser.page_source

    def big_article_text(kek):
        soup = BeautifulSoup(kek, 'lxml')
        head = soup.find('h1',
                         class_='jsx-1660569506 jsx-598863799 heading').text
        paragraphs = soup.find_all('p', class_='jsx-4247481572')
        logger.debug(head)

        with open('indicator/article_text.txt', 'w') as txt:
            data = [paragr.text for paragr in paragraphs]
            txt.write('\n'.join(data))

        link = 'https://indicator.ru/' + soup.find('img', class_='_3vBDgiAM').get('src')

        response = requests.get(link)
        with open(f'indicator/pictures/indicator_pic_{random.randint(0, 100000)}.jpg', 'wb') as Indic_pic_file:
            Indic_pic_file.write(response.content)

    def small_articles(url):
        browser.get(url)
        code = browser.page_source
        soup = BeautifulSoup(code, 'lxml')
        lil_articles = ['https://indicator.ru' + elem.find('a').get('href') for elem in
                        soup.find_all('div', class_='jsx-2819128655 card2 _2dGEmCvc desktop')]
        random_article = choice(lil_articles)
        logger.debug(f'Ссылка на случайную статью: {random_article}')
        browser.get(random_article)
        return browser.page_source

    def small_article_text(cards):
        soup = BeautifulSoup(cards, 'lxml')
        head = soup.find('h1',
                         class_='jsx-1660569506 jsx-598863799 heading').text
        logger.debug(head)
        paragraphs = soup.find_all('p', class_='jsx-4247481572')

        with open('indicator/article_text.txt', 'w') as txt:
            data = [paragr.text for paragr in paragraphs]
            txt.write('\n'.join(data))

        link = 'https://indicator.ru/' + soup.find('img', class_='_3vBDgiAM').get('src')

        response = requests.get(link)

        with open(f'indicator/pictures/indicator_pic_{random.randint(0, 10000)}.jpg', 'wb') as Indic_pic_file:
            Indic_pic_file.write(response.content)

    link = 'https://indicator.ru/astronomy'
    a = random.randint(0, 1)

    if a == 0:
        html_random_big_article = big_articles(link)
        big_article_text(html_random_big_article)

    elif a == 1:
        html_random_small_article = small_articles(link)
        small_article_text(html_random_small_article)


def parse_hubble():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    browser = webdriver.Chrome(options=opt, executable_path=r'drivers\chromedriver.exe')

    def get_html_selenium(url):
        browser.get(url)  # переход по ссылке
        articles = browser.find_elements_by_tag_name("article")  # поиск всех элементов у которых html-тэг это article
        random_article = choice(articles)  # выбираем случайную статью
        random_article.find_element_by_class_name('np-archive-more').click()  # нажимаем читать далее
        browser.find_element_by_class_name('entry-title')
        return browser.page_source

    def Hubble_parse(Html):
        soup = BeautifulSoup(Html, 'lxml')
        articles = soup.find('div', class_="entry-content").find_all('p')
        imgs = soup.find_all('figure')

        if not os.path.exists('hubble'):
            os.mkdir('hubble')
            os.mkdir('hubble/pictures')

        with open('hubble/article_text.txt', 'a') as txt:
            data = [p.text for p in articles]
            txt.write('\n'.join(data))

        try:
            for image in imgs:
                link = image.find('a').get('href')
                responce = requests.get(link)

                with open(f'hubble/pictures/hubble_pic_{random.randint(0, 10000)}.jpg', 'wb') as hub_pic_file:
                    hub_pic_file.write(responce.content)

        except Exception as e:
            print(e)

    html = get_html_selenium('https://universemagazine.com/news/astronomy/')
    Hubble_parse(html)


def parse_100_facts():
    def get_html(url):
        html_code = requests.get(url)
        return html_code.text

    def parse(html_code):
        soup = BeautifulSoup(html_code, 'lxml')
        facts = soup.find('div', class_='entry-content cf').find_all('p')
        r = random.choice(facts[1:])
        return r.text

    html = get_html('https://100-faktov.ru/100-interesnyx-faktov-o-kosmose/')
    return parse(html)


__all__ = [parse_hubble, parse_100_facts, parse_indicator]

if __name__ == '__main__':
    print(parse_100_facts())
