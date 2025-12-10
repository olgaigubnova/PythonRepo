from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запускаем браузер
driver = webdriver.Chrome()

try:
    # Переход на страницу
    driver.get("http://uitestingplayground.com/ajax")

    # Нажимаем синюю кнопку
    button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
    button.click()

    # Ждём, пока появится зелёный блок
    wait = WebDriverWait(driver, 15)
    green_box = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )

    # Получаем текст и выводим
    print(green_box.text)

finally:
    driver.quit()
