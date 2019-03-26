import csv
import json
import requests
from bs4 import BeautifulSoup

url = "https://exame.abril.com.br/carreira/as-100-melhores-universidades-da-america-latina/"
web = requests.get(url)
webs = BeautifulSoup(web.text, "lxml")

arquivo_csv = open('dados_tabela.csv', mode='w', encoding='utf-8')
writer = csv.writer(arquivo_csv)
writer.writerow(['Ranking', 'Universidade', 'Pais', 'Nota'])

dic = []

tabela = webs.find('table')
for linha in tabela.findAll('tr'):
    celula = linha.findAll('td')
    if len(celula) == 4:
        ranking = celula[0].find(text=True).strip('\t\r\nº')
        universidade = celula[1].find(text=True).strip('\t\r\n')
        pais = celula[2].find(text=True).strip('\t\r\n')
        nota = celula[3].find(text=True).strip('\t\r\n')

        dic.append({"Ranking": ranking, "Universidade": universidade, "País": pais, "Nota": nota})

        writer.writerow([ranking, universidade, pais, nota])

arquivo_csv.close()
with open('dados_tabela.json', mode='a') as arquivo_json:
    json.dump(dic, arquivo_json, indent=4)


