#Conjunto de importações
import requests
from bs4 import BeautifulSoup
import re

#Função para o Web crawler
def web_crawler(url_partida, limite_links):
    #Expressão regular para definir endereço de URL
    regex_href = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    #Adiciona a URL na lista de links
    lista_links.append(url_partida)

    #Para cada url armazenada na lista
    for url in lista_links:
        #Recupera o código fonte da URL
        fonte = requests.get(url)
        fonte_bs = BeautifulSoup(fonte.text)
        #Para o componente com a classe widget-news-list recupere todas as tags 'a' cujo conteúdo 'href' seja um endereço http válido
        links_coletados = fonte_bs.find('ul', class_='widget-news-list').find_all('a', href = re.compile(regex_href))

        #Para cada link recuperado
        for link in links_coletados:
            #Adiciona o conteúdo href na lista de links
            lista_links.append(link.get('href'))

        #Verifica se o total de links na lista atingiu o limite
        if len(lista_links) >= limite_links:
            break

#Função para o Web scraper
def web_scraper():
    #Para cada link armazenado na lista de links
    for link in lista_links:
        #Recupera o código fonte
        fonte = requests.get(link)
        fonte_bs = BeautifulSoup(fonte.text)
        #Faz a raspagem das imagens
        imagens = fonte_bs.find_all('img')

        #Para cada imagem coletada do link
        for imagem in imagens:
            #Apresenta o código da imagem raspado
            print(imagem)
            print("\n")
        print("\n")

#Inicia a lista_links
lista_links = []
#Define que o limite será de 10 links coletados
limite_links = 10
#Define a URL de partida
url_partida = 'http://exame.abril.com.br/carreira/as-100-melhores-universidades-da-america-latina/'

#Chamada para a função do Web crawler
web_crawler(url_partida, limite_links)
#Chamada para a função do Web scraper
web_scraper()
