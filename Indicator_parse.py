import webbrowser
import requests
from bs4 import BeautifulSoup
from random import choice
from selenium import webdriver
from loguru import logger
import random

opt = webdriver.ChromeOptions()
opt.add_argument('headless')
browser = webdriver.Chrome(options=opt, executable_path=r'F:\Тёма\Проект микрообучение\chromedriver.exe')
                           #executable_path=r'C:\Users\КВАНТОРИАНЕЦ\Desktop\Проект микрообучение\chromedriver.exe')


def get_html(url):
    html_code = requests.get(url)
    return html_code.text


# def big_articles(url):
#     browser.get(url)
#     # articles = []
#     # containers = browser.find_elements_by_class_name('jsx-3628860864 container')
#     # print(containers)
#     # for container in containers:
#     #     print(container)
#     #     big_article = container.find_elements_by_class_name('jsx-3628860864 hero _2TUd5iHO')
#     #     articles.append(big_article)
#     # random_article = choice(articles)
#     # random_article.find_element_by_class_name('jsx-554776911 headline').click()
#     # browser.find_element_by_class_name('jsx-4247481572')
#     with open('hren.html', 'w', encoding='utf-8') as file:
#         file.write(browser.page_source)
#     return browser.page_source


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

    for paragraph in paragraphs:
        logger.debug(paragraph.text)      # text + '/n'

    link = 'https://indicator.ru/' + soup.find('img', class_='_3vBDgiAM').get('src')
    #logger.debug(link)
    response = requests.get(link)
    with open('Indicator_pic.jpg', 'wb') as Indic_pic_file:
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

    for paragraph in paragraphs:
        logger.debug(paragraph.text)
    link = 'https://indicator.ru/' + soup.find('img', class_='_3vBDgiAM').get('src')
    # logger.debug(link)
    response = requests.get(link)
    with open('Indicator_pic.jpg', 'wb') as Indic_pic_file:
        Indic_pic_file.write(response.content)



# jsx-2819128655 card2 _2dGEmCvc desktop - маленькие карточки
# jsx-3628860864 hero _2TUd5iHO - большие карточки


if __name__ == '__main__':
    link = 'https://indicator.ru/astronomy'
    a = random.randint(0, 1)
    if a == 0:
        html_random_big_article = big_articles(link)
        big_article_text(html_random_big_article)
    elif a == 1:
        html_random_small_article = small_articles(link)
        small_article_text(html_random_small_article)
    print(a)


    #html_random_big_article = big_articles(link)
    # big_article_text(html_random_big_article)
    #html_random_small_article = small_articles(link)
    #small_article_text(html_random_small_article)