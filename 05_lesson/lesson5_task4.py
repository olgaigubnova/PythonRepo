from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Запуск Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

# Открыть страницу логина
driver.get("http://the-internet.herokuapp.com/login")

# Ввести username
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

#Ввести password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

# Нажать кнопку Login
login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()

# Получить текст зелёной плашки
message = driver.find_element(By.ID, "flash").text
print(message)

sleep(5)

# Закрыть браузер
driver.quit()