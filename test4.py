from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuração do ChromeDriver
driver = webdriver.Chrome()

# Acessar um site (por exemplo, Google)
driver.get("google.com")

# Esperar alguns segundos para a página carregar
time.sleep(2)

# Fechar o navegador
driver.quit()
