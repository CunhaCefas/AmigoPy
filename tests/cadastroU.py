import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select




# Função para gerar um e-mail aleatório
def gerar_email_aleatorio():
    nome_usuario = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    dominio = ''.join(random.choices(string.ascii_lowercase, k=5))
    email = f"{nome_usuario}@{dominio}.com"
    return email

# Função para gerar um nome aleatório
def gerar_nome_aleatorio():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=6))

# Função para gerar um sobrenome aleatório
def gerar_sobrenome_aleatorio():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))

# Função para gerar uma senha aleatória com 5 caracteres
def gerar_senha_aleatoria():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

browser = webdriver.Chrome()
browser.get("http://www.automationpractice.pl/index.php")

# Criar usuário aleatório
BtnLogin = browser.find_element(By.XPATH,"/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a")
BtnLogin.click()

# Encontrar o campo de e-mail e preencher com o e-mail gerado
criaremail = browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/div/div[1]/form/div/div[2]/input")
criaremail.click()
criaremail.send_keys(gerar_email_aleatorio())  # Chama a função para gerar o e-mail

# Clicar no botão amarelo "Criar conta"
btncreate = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/div[1]/form/div/div[3]/button/span")
btncreate.click()

# Espera explícita com um tempo maior (5 segundos) para garantir que a página carregue
time.sleep(5)  # Aumente o tempo se necessário

# Selecionar sempre o gênero "MR" (valor 1)
browser.find_element(By.ID, "id_gender1").click()

# Preencher o primeiro nome com valor aleatório
firstname = browser.find_element(By.ID, "customer_firstname")
firstname.click()
firstname.send_keys(gerar_nome_aleatorio())

# Preencher o sobrenome com valor aleatório
lastname = browser.find_element(By.ID, "customer_lastname")
lastname.click()
lastname.send_keys(gerar_sobrenome_aleatorio())





# Preencher a senha com valor aleatório (5 caracteres)
senha = browser.find_element(By.ID, "passwd")
senha.click()
senha.send_keys(gerar_senha_aleatoria())


# Encontrar o elemento select de dias e selecionar um valor aleatório
select_dias = Select(browser.find_element(By.ID, "days"))
opcoes_dias = [opcao.get_attribute("value") for opcao in select_dias.options if opcao.get_attribute("value") != ""]
valor_aleatorio_dia = random.choice(opcoes_dias)
select_dias.select_by_value(valor_aleatorio_dia)

# Encontrar o elemento select de meses e selecionar sempre o primeiro mês (January)
select_meses = Select(browser.find_element(By.ID, "months"))
select_meses.select_by_value("1")  # Janeiro é a primeira opção (valor="1")

# Encontrar o elemento select de anos e selecionar um valor aleatório entre as opções
select_anos = Select(browser.find_element(By.ID, "years"))
opcoes_anos = [opcao.get_attribute("value") for opcao in select_anos.options if opcao.get_attribute("value") != ""]
valor_aleatorio_ano = random.choice(opcoes_anos)
select_anos.select_by_value(valor_aleatorio_ano)

#envia o forms
submit = browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/div/form/div[2]/button/span").click()

time.sleep(5)

#home
homecasinha = browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[1]/a/i").click()


# Aguardar até que o usuário pressione Enter para fechar
input("Pressione Enter para fechar o navegador...")
browser.quit()
