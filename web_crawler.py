import csv
import json
import requests
from bs4 import BeautifulSoup
import re


def web_cwr(url_partida, limite_links):
    regex_href = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    lista_links.append(url_partida)

    for url in lista_links:
        web = requests.get(url)
        webs = BeautifulSoup(web.text)
        new_link = webs.find('ul').find_all('a', href=re.compile(regex_href))

        for link in new_link:
            lista_links.append(link.get('href'))

        if len(lista_links) >= limite_links:
            break


def web_scraper():
    for link in lista_links:
        fonte = requests.get(link)
        fonte_bs = BeautifulSoup(fonte.text)
        imagens = fonte_bs.find_all('img')

        for imagem in imagens:
            print(imagem)
            print("\n")
        print("\n")


lista_links = []
limite_links = 10
url_partida = 'http://exame.abril.com.br/carreira/as-100-melhores-universidades-da-america-latina/'

web_cwr(url_partida, limite_links)
web_scraper()

print(lista_links)
