# Conjunto de importações
import requests
from bs4 import BeautifulSoup
import csv

url = "http://exame.abril.com.br/carreira/as-100-melhores-universidades-da-america-latina/"
resp = requests.get(url)

# Apresenta todo o conteúdo da página recuperada pelo Web crawler
pagina_bs = BeautifulSoup(resp.text)
tabela = pagina_bs.find('table')

# Cria o arquivo dados_tabela.csv no modo append
arquivo_csv = open('dados_tabela.csv', mode='a', encoding='utf-8')
writer = csv.writer(arquivo_csv)

# Escreve o cabeçalho no arquivo
writer.writerow(['Ranking', 'Universidade', 'Pais', 'Nota'])

# Percorre a tabela
for linha in tabela.findAll("tr"):
    celula = linha.findAll('td')
    if len(celula) == 4:
        # Recupera o conteúdo de cada célula da linha
        ranking = celula[0].find(text=True).strip('\t\r\nº')
        universidade = celula[1].find(text=True).strip('\t\r\n')
        pais = celula[2].find(text=True).strip('\t\r\n')
        nota = celula[3].find(text=True).strip('\t\r\n')

        # Escreve os valores recuperados no arquivo
        writer.writerow([ranking, universidade, pais, nota])

# Fecha o arquivo
arquivo_csv.close()
