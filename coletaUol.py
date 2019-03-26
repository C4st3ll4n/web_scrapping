import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re

url = 'https://educacao.uol.com.br/colunas/' \
      'maria-alice-setubal/2017/04/25/o-medo-da-prova-revela-que-precisamos-rever-nossas-avaliacoes.htm'

wd = webdriver.Firefox(executable_path="D:\Download\gdriver\geckodriver.exe")
wd.get(url)

fonte_pagina = wd.page_source
wd.quit()

arquivo_csv = open('comentarios_uol.csv', mode='a', encoding='utf-8')
writer = csv.writer(arquivo_csv)
writer.writerow(["Comentários"])
soup = BeautifulSoup(fonte_pagina, 'lxml')
comentarios = soup.findAll('p', class_='content')

for comentario in comentarios:
    writer.writerow(comentario)


def web_cwr(url_partida, limite_links):
    regex_href = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    lista_links.append(url_partida)

    for urll in lista_links:
        web = requests.get(urll)
        webs = BeautifulSoup(web.text)
        new_link = webs.find('ul').find_all('a', href=re.compile(regex_href))

        writer.writerow(["Links"])
        for link in new_link:
            writer.writerow([link.get('href')])
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
url_partida = url

web_cwr(url_partida, limite_links)
web_scraper()

print(lista_links)
arquivo_csv.close()
