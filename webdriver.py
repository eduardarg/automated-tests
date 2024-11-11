from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Configurar o WebDriver (certifique-se de que o ChromeDriver está no PATH)
driver = webdriver.Chrome()

# 1. Abrir a página no navegador
driver.get("file:///C:/Users/eduar/OneDrive/Documents/P%C3%93S/TESTES/sample-exercise.html")  # Substitua pela URL correta

# 2. Clicar no botão "generate"
generate_button = driver.find_element(By.ID, "test")  # Substitua pelo ID correto do botão
generate_button.click()

# 3. Capturar o código gerado
time.sleep(5)  # Aguardar a geração do código (tempo ajustável)
code = driver.find_element(By.ID, "my-value").text

# 4. Preencher o campo de texto com o código capturado
input_field = driver.find_element(By.ID, "input")  # Substitua pelo ID correto do campo de texto
input_field.send_keys(code)

# 5. Clicar no botão "test"
test_button = driver.find_element(By.ID, "test-button")  # Substitua pelo ID correto do botão
test_button.click()

# 6. Fechar o alerta "Done!"
alert = Alert(driver)
alert.accept()

# 7. Verificar e imprimir a mensagem "It workls! <código>!"
result_text = driver.find_element(By.ID, "result").text
print(result_text)  # Exibe no terminal

# 8. Fechar o navegador
driver.quit()