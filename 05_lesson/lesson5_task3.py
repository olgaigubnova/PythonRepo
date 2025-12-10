from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Найти поле ввода
input_field = driver.find_element(By.TAG_NAME, "input")

# Ввести Sky
input_field.send_keys("Sky")
sleep(5)

# Очистить поле
input_field.clear()
sleep(5)

# Ввести Pro
input_field.send_keys("Pro")
sleep(5)

# Закрыть браузер
driver.quit()
    