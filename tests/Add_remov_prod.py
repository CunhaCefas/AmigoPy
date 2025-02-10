import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def log_valido(browser):
    """Função para realizar login válido"""
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
    
    print("Login realizado com sucesso!")


# Inicializa o navegador
browser = webdriver.Chrome()

# Chama a função de login antes de adicionar/remover itens do carrinho
log_valido(browser)


# Clicar no botão "Women"
browser.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[1]/a").click()

# Escolher vestido "Printed Summer" amarelo
browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/ul/li[5]/div/div[1]/div/a[1]/img").click()

# Espera até o elemento estar visível e clicável
element = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "color_11"))
)
browser.execute_script("arguments[0].click();", element)

time.sleep(2)

# Tentar clicar no botão preto
bntb = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/div/div[4]/form/div/div[2]/div/fieldset[2]/div/ul/li[1]/a")
bntb.click()

# Espera até o botão "Add to cart" estar visível e clicável
add_to_cart_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Add to cart']"))
)
add_to_cart_button.click()

time.sleep(2)

# Espera até o botão "Continue shopping" estar visível e clicável
continue_shopping_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "span.continue[title='Continue shopping']"))
)
continue_shopping_button.click()

# Espera até o link "Cart" estar visível e clicável
cart_link = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[b[text()='Cart']]"))
)
cart_link.click()

# Espera até o botão "Delete" estar visível e clicável
delete_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@title='Delete' and @class='cart_quantity_delete']"))
)
delete_button.click()

# Verifica se o carrinho está vazio
empty_cart_message = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "//p[@class='alert alert-warning' and contains(text(), 'Your shopping cart is empty.')]"))
)

assert "Your shopping cart is empty." in empty_cart_message.text
print("Teste de adicionar e remover do carrinho executado com sucesso!")

# logout para integrar com a proxima pagina.
logout_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "logout"))
)

# Clica no botão de logout
logout_button.click()

time.sleep(2)
input("Pressione Enter para fechar o navegador...")
browser.quit()
