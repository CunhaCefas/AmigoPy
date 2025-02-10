# importando a função de criação de usuário


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from cadastro import cadastro  # Importa a classe de cadastro





browser = webdriver.Chrome()
browser.get("http://www.automationpractice.pl/index.php")

# Cria uma instância da classe de cadastro e realiza o cadastro
cadastro = cadastro(browser)
cadastro.criar_conta()

#clicar no BTN women - pause
women = browser.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[1]/a").click()

#escolhavestido Printed Suumer amarelo
Vest5 = browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div[2]/ul/li[5]/div/div[1]/div/a[1]/img").click()

# Espera até o elemento estar visível e clicável
element = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "color_11"))
)

# Utiliza JavaScript para garantir que o clique seja processado corretamente
browser.execute_script("arguments[0].click();", element)

time.sleep(5)


#tentativa desesperada de clicar no botao preto
bntb = browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/div/div/div[4]/form/div/div[2]/div/fieldset[2]/div/ul/li[1]/a")
bntb.click()


# Espera até o elemento "Adicionar ao Carrinho" estar visível e clicável
add_to_cart_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Add to cart']"))
)

# Clica no botão
add_to_cart_button.click()



# Espera até o link "Proceed to checkout" estar visível e clicável
checkout_link = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-default button button-medium' and @title='Proceed to checkout']"))
)

# Clica no link
checkout_link.click()



# Espera até o link "Proceed to checkout" estar visível e clicável
checkout_link = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='button btn btn-default standard-checkout button-medium' and @title='Proceed to checkout']"))
)

# Clica no link
checkout_link.click()


#preenchendo o forms
company =  browser.find_element(By.ID,"company").send_keys("Amigo")

address1 =  browser.find_element(By.ID,"address1").send_keys("Aurora")

city =  browser.find_element(By.ID,"city").send_keys("Recife")


select_element = Select(browser.find_element(By.ID, "id_state"))
select_element.select_by_value("5")

postcode =  browser.find_element(By.ID,"postcode").send_keys("97001")
# Seleciona a opção "United States" pelo valor (no caso, o valor é "21")

select_element = Select(browser.find_element(By.ID, "id_country"))
select_element.select_by_value("21")

phone_mobile =  browser.find_element(By.ID,"phone_mobile").send_keys("81995566332")

alias =  browser.find_element(By.ID,"alias").send_keys("123")

#saveSubmit
savesubmit = browser.find_element(By.ID,"submitAddress").click()


# Espera até o botão "Proceed to checkout" btn verde -  estar visível e clicável
proceed_to_checkout_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button/span[contains(text(), 'Proceed to checkout')]"))
)

# Clica no botão
proceed_to_checkout_button.click()



#click no agree

agree = browser.find_element(By.ID,"cgv").click()

# Espera até o botão estar visível e clicável com base na classe
checkout_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='button btn btn-default standard-checkout button-medium' and @name='processCarrier']"))
)

# Clica no botão
checkout_button.click()


# Espera até o link "Pay by bank wire" estar visível e clicável
bankwire_link = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@title='Pay by bank wire']"))
)

# Clica no link
bankwire_link.click()

# Espera até o botão "I confirm my order" estar visível e clicável
confirm_order_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button/span[contains(text(), 'I confirm my order')]"))
)

# Clica no botão
confirm_order_button.click()

# Espera até o link "View your order history" estar visível e clicável
order_history_link = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@title='Go to your order history page']"))
)

# Clica no link
order_history_link.click()

# Espera até o link com o título "View my customer account" estar visível e clicável
account_link = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@title='View my customer account']"))
)

# Clica no link
account_link.click()

# Espera até o link com o texto "Order history and details" estar visível e clicável
order_history_link = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[span[text()='Order history and details']]"))
)

# Clica no link
order_history_link.click()

# Espera até o elemento com a classe "footable-sorted" (indicando que o cabeçalho foi ordenado) estar visível
status_header_sorted = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//th[@class='item footable-last-column footable-sortable footable-sorted']"))
)

# Você pode então interagir com o elemento, se necessário
status_header_sorted.click()



# Aguardar até que o usuário pressione Enter para fechar
input("Pressione Enter para fechar o navegador...")
browser.quit()
