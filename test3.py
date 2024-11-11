from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuração do ChromeDriver
driver = webdriver.Chrome()

# Acessar um site (por exemplo, Google)
driver.get("https://www.google.com")

# Esperar alguns segundos para a página carregar
time.sleep(2)

# Encontrar a barra de pesquisa pelo nome e digitar "Selenium Python"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Puc Minas")
search_box.send_keys(Keys.RETURN)

# Esperar alguns segundos para ver os resultados
time.sleep(5)

# Fechar o navegador
driver.quit()