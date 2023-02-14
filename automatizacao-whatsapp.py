from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")

time.sleep(30)

search_box = driver.find_element(By.XPATH, '//div[@title="Caixa de texto de pesquisa"]')

search_box.send_keys("NOME DO CONTATO")
search_box.send_keys(Keys.RETURN)

time.sleep(5)

message_box = driver.find_element(By.XPATH, '//div[@spellcheck="true"]')

message_box.send_keys("MENSAGEM A SER ENVIADA")

time.sleep(10)

message_box.send_keys(Keys.RETURN)

time.sleep(15)
