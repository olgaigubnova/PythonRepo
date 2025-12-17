from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_buttons():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 10)

    # Ждём появления поля company
    wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

    # Словарь полей для заполнения
    idValueDictionary = {
        'first-name': "Иван",
        'last-name': "Петров",
        'address': "Ленина, 55-3",
        'e-mail': "test@skypro.com",
        'phone': "+7985899998787",
        'zip-code': "",
        'city': "Москва",
        'country': "Россия",
        'job-position': "QA",
        'company': "SkyPro"
    }

    # Заполняем поля
    for key in idValueDictionary.keys():
        input_field = driver.find_element(By.NAME, key)
        input_field.send_keys(idValueDictionary[key])

    # Нажимаем кнопку Submit
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").click()

    # Проверяем zipCode на alert-danger
    zip_code = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code.get_attribute("class")

    # Проверяем остальные поля на alert-success
    for key in idValueDictionary:
        if key != 'zip-code':
            element = driver.find_element(By.ID, key)
            assert "alert-success" in element.get_attribute("class")

    driver.quit()