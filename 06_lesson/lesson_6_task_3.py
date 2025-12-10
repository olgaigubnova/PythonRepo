from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    wait = WebDriverWait(driver, 20)

    # Ждём появления 4 картинок 
    wait.until(lambda d: len(d.find_elements(By.TAG_NAME, "img")) == 4)
    # Получаем список картинок
    images = driver.find_elements(By.TAG_NAME, "img")
    # Ждём загрузки всех картинок
    for img in images:
        wait.until(
            lambda d, image=img: d.execute_script(
                "return arguments[0].complete && arguments[0].naturalWidth > 0", image
            )
        )

    third_visual_img = images[3]
    third_src = third_visual_img.get_attribute("src")

    print(third_src)

finally:
    driver.quit()
    