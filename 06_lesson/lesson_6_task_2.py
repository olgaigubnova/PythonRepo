from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Перейти на страницу
    driver.get("http://uitestingplayground.com/textinput")

    # Ввести текст "SkyPro"
    input_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )
    input_field.send_keys("SkyPro")

    # Нажать синюю кнопку
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    # Дождаться изменения текста кнопки
    WebDriverWait(driver, 5).until(
        lambda d: button.text == "SkyPro"
    )

    print(button.text)

finally:
    driver.quit()