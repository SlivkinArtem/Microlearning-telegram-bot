import webbrowser

import requests
from bs4 import BeautifulSoup
from random import choice
from selenium import webdriver
import time

opt = webdriver.ChromeOptions()
#opt.add_argument('headless')
browser = webdriver.Chrome(options=opt, executable_path=r'C:\Users\КВАНТОРИАНЕЦ\Desktop\bla\drivers\chromedriver.exe')


def get_html(url):
    html_code = requests.get(url)
    return html_code.text


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
    # imgs = soup.find('div', class_='wp-caption aligncenter')
    imgs = soup.find_all('figure')
    # print(imgs)

#    for img in imgs:
#        print(img.get('src'))
#        webbrowser.open(img.get('src'))

    for p in articles:
        print(p.text + '\n')

    for image in imgs:
        link = image.find('a').get('href')
        #link = image.get('href')
        print(link)
        responce = requests.get(link)
        with open('hubble_pic.jpg', 'wb') as hub_pic_file:
            hub_pic_file.write(responce.content)

    #video = soup.find('link', rel_='canonical').get('href')
    try:
        the_url = soup.find("link", {"canonical": "apple-touch-icon"})['href']
        print(the_url)
    except Exception:
        pass
    # if the_url != None:
    #     print(the_url)

#
# def get_imgs(kek):
#     imgs = soup.find('div', class_='wp-caption aligncenter')
#     requests.get(href="https://universemagazine.com/wp-content/uploads/2021/03/iss063e104178_lrg-scaled.jpg")

     #random_article = choice(articles)
     #title = random_article.find('header', class_='entry-header').find('a').text
     #print(title)


if __name__ == '__main__':
    html = get_html_selenium('https://universemagazine.com/news/astronomy/')
    Hubble_parse(html)