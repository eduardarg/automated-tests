from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configuração do Chrome em modo headless (opcional)
options = Options()
options.headless = True  # Evita abrir o navegador visualmente

# Conectando ao ChromeDriver que está rodando no Windows na porta 56750
driver = webdriver.Remote(
    command_executor='http://localhost:56750',
    options=options
)

# Acessa uma página de teste
driver.get("https://www.google.com")
print(f"Página aberta com sucesso! Título: {driver.title}")

# Fecha o navegador
driver.quit()