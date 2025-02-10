from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait



browser =  webdriver.Chrome()
browser.get("http://www.automationpractice.pl/index.php")


# Faz o login e logout com senhas pre-cadastradas. -  Login válido
BtnLogin = browser.find_element(By.XPATH,"/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a")
BtnLogin.click()
#email 
email  =  browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/div[1]/input")
email.click()
email.send_keys("HellBiscoito3@gmail.com")

#senha
senha = browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/div[2]/input")
senha.click()
senha.send_keys("123456")

#botão confirmação
submit = browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/p[2]/button")
submit.click()

# Após o login ou redirecionamento para a página do usuário
page_heading = browser.find_element(By.XPATH, "//h1[@class='page-heading']")

# Verifica se o texto "My account" está presente no elemento
assert "My account" in page_heading.text, "A página da conta do usuário não foi carregada corretamente."



input("Pressione Enter para fechar o navegador...")
browser.quit()


#falta o asset.