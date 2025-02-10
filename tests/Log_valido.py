from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def log_valido(browser):
    """Realiza login válido no site."""
    browser.get("http://www.automationpractice.pl/index.php")
    
    # Clica no botão de login
    BtnLogin = browser.find_element(By.XPATH, "/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a")
    BtnLogin.click()
    
    # Preenche o email
    email = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/div[1]/input")
    email.send_keys("HellBiscoito3@gmail.com")
    
    # Preenche a senha
    senha = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/div[2]/input")
    senha.send_keys("123456")
    
    # Confirma o login
    submit = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/p[2]/button")
    submit.click()

    # Aguarda para garantir que o login foi bem-sucedido
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/header/div[2]/div/div/nav/div[2]/a"))
    )
    
    print("Login realizado com sucesso!")
