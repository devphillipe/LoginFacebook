from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Cria as opções do ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument("--incognito")

# Cria uma instância do navegador Chrome com as opções
browser = webdriver.Chrome(options=options)

# 1 criar um navegador webdriver
browser = webdriver.Chrome()
# 2 navegar ate um site
browser.get('https://www.facebook.com/')
# 3 Encontrar elemento email
campo_email= browser.find_element(By.NAME, 'email')

# 4 Interagir com eles digitando ou clicando
# Clicar
campo_email.click()
# Digitar
campo_email.send_keys('seuemail')
# Aguarda a página carregar

#Encontrar elemento senha
campo_senha = browser.find_element(By.NAME, 'pass')
campo_senha.click()
campo_senha.send_keys('sua senha')
# Aguarda a página carregar

# Econtrar botão entrar
botao_enviar = browser.find_element(By.NAME, 'login')
botao_enviar.click()

# Aguarda a página carregar
time.sleep(20)
