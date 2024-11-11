import random
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import time

driver = webdriver.Chrome()

driver.get("file:///C:/Users/eduar/Documents/tarefa2/sample-exercise.html")
time.sleep(2)

code = driver.find_element(By.ID, "my-value")
input = driver.find_element(By.ID, "input")
input.clear()
input.send_keys(code.text)
test_bnt = driver.find_element(By.NAME, "button")
test_bnt.click()

alert = driver.switch_to.alert
alert.accept()
time.sleep(3)

result = driver.find_element(By.ID, "result")
assert result.text == f"It workls! {code.text}!"

driver.quit()


def generate_code(driver):
    generate = driver.find_element(By.NAME, "generate")
    generate.click()