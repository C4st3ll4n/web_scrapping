from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup

#Definição da url
url = 'http://g1.globo.com/educacao/noticia/ministro-diz-que-alunos-nao-serao-prejudicados-por-dificuldade-em-sistemas-do-mec.ghtml'

#Classes para os WebDrivers disponíveis.
#Descomente a linha referente ao seu navegador.
wd = webdriver.Firefox(executable_path="D:\Download\gdriver\geckodriver.exe")
#wd = webdriver.Chrome()
#wd = webdriver.Safari()
#wd = webdriver.Edge()

#Carrega a página definida no url
wd.get(url)

WebDriverWait(wd, 100).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="glbComentarios-conteudo-interno"]')))

#Recupera o código-fonte da página
fonte_pagina = wd.page_source
#Encerra a instância aberta do navegador
wd.quit()

#Realiza a raspagem dos dados
soup = BeautifulSoup(fonte_pagina, 'lxml')
comentarios = soup.findAll('p', class_='glbComentarios-texto-comentario')
print(comentarios)