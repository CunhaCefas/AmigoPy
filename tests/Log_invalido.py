from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time



browser =  webdriver.Chrome()
browser.get("http://www.automationpractice.pl/index.php")


# Faz o login  senha e usuário incorreto
BtnLogin = browser.find_element(By.XPATH,"/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a")
BtnLogin.click()
#email 
email  =  browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/div[1]/input")
email.click()
email.send_keys("HellBiscoito37@gmail.com")

#senha
senha = browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/div[2]/input")
senha.click()
senha.send_keys("1234556")

#botão confirmação
submit = browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/p[2]/button")
submit.click()

try:
    # Procurando pelo elemento que contém a mensagem de erro
    error_message = browser.find_element(By.XPATH, "//li[text()='Authentication failed.']")

    # Verifica se o texto do erro é o esperado
    assert error_message.text == "Authentication failed.", "A mensagem de erro não é a esperada!"
    print("Autenticação falhou, teste passou!")

except Exception as e:
    print("Erro de autenticação não encontrado ou outro erro ocorreu:", str(e))
    
input("Pressione Enter para fechar o navegador...")
browser.quit()
