from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service(executable_path=GeckoDriverManager().install())
browser = webdriver.Firefox(service=service)

activation_button = "//mts-tariff-card[@id='4705081']//div[@class='btn universal-card-button'][contains(text(),'Подключить')]"
send_appl = "//button[@class='btn btn_large ng-star-inserted']"
success = "//div[@class='dialog-container ng-star-inserted']"
spec_symbols = "!@#$%^&*()_+=-№[]';/.,\":\\|}{<>?\n"
browser.implicitly_wait(3)

browser.get("https://moskva.mts.ru/personal/mobilnaya-svyaz/tarifi/vse-tarifi/mobile-tv-inet")
browser.find_element(By.XPATH, activation_button).click()
browser.find_element(By.ID, 'username').send_keys(spec_symbols)
browser.find_element(By.ID, 'phone').send_keys('0123456789')
time.sleep(3)
browser.find_element(By.XPATH, send_appl).click()

browser.quit()

