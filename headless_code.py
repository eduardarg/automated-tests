from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service("/home/eduarda/.cache/selenium/chromedriver/linux64/130.0.6723.69/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.selenium.dev")
print(driver.title)

driver.quit()
