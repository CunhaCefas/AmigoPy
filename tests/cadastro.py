import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class cadastro:
    def __init__(self, browser):
        self.browser = browser  # Recebe o navegador já inicializado

    # Função para gerar um e-mail aleatório
    def gerar_email_aleatorio(self):
        nome_usuario = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        dominio = ''.join(random.choices(string.ascii_lowercase, k=5))
        return f"{nome_usuario}@{dominio}.com"

    # Função para gerar um nome aleatório
    def gerar_nome_aleatorio(self):
        return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=6))

    # Função para gerar um sobrenome aleatório
    def gerar_sobrenome_aleatorio(self):
        return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))

    # Função para gerar uma senha aleatória com 5 caracteres
    def gerar_senha_aleatoria(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

    # Função para criar uma conta de usuário
    def criar_conta(self):
        # Clicar no botão de login
        self.browser.find_element(By.XPATH, "/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a").click()

        # Preencher o campo de e-mail e clicar em "Criar conta"
        self.browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/div[1]/form/div/div[2]/input").send_keys(self.gerar_email_aleatorio())
        self.browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/div[1]/form/div/div[3]/button/span").click()

        # Esperar a página carregar
        time.sleep(5)

        # Preencher os detalhes do formulário
        self.browser.find_element(By.ID, "id_gender1").click()
        self.browser.find_element(By.ID, "customer_firstname").send_keys(self.gerar_nome_aleatorio())
        self.browser.find_element(By.ID, "customer_lastname").send_keys(self.gerar_sobrenome_aleatorio())
        self.browser.find_element(By.ID, "passwd").send_keys(self.gerar_senha_aleatoria())

        # Selecionar data de nascimento
        Select(self.browser.find_element(By.ID, "days")).select_by_value(random.choice([opcao.get_attribute("value") for opcao in Select(self.browser.find_element(By.ID, "days")).options if opcao.get_attribute("value") != ""]))
        Select(self.browser.find_element(By.ID, "months")).select_by_value("1")
        Select(self.browser.find_element(By.ID, "years")).select_by_value(random.choice([opcao.get_attribute("value") for opcao in Select(self.browser.find_element(By.ID, "years")).options if opcao.get_attribute("value") != ""]))

        # Submeter o formulário
        self.browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/form/div[2]/button/span").click()

        # Esperar o cadastro ser concluído
        time.sleep(5)