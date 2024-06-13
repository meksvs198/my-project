import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try: # try/finnaly - конструкция для того что бы закрыть окно браузера даже если в середине тест упадет с ошибкой
    link = "https://beta1.umnico.com/ru/"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)  # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.get(link)
    button = browser.find_element(By.ID, "landing-burger-menu-sign-in")
    button.click()
    input1 = browser.find_element(By.CLASS_NAME, "auth-input")
    input1.send_keys("qa+1@umnico.com")
    input2 = browser.find_element(By.CLASS_NAME, "auth-input.password-input__input")
    input2.send_keys("qa12345")
    button = browser.find_element(By.ID, "landing-login-sign-in")
    button.click()

    # Ждем загрузки страницы
    time.sleep(2)

    # Находим и кликаем по кнопке настроек
    button = browser.find_element(By.ID, "global-nav-link-Settings")
    button.click()

    # Находим все пункты настроек и прокликиваем их
    settings_elements = browser.find_elements(By.CLASS_NAME, "sub-nav__link")
    for element in settings_elements:
        element.click()
        time.sleep(1)  # Для наглядности добавляем небольшую задержку

    print("Все пункты настроек успешно прокликаны")
    time.sleep(3)

except Exception as e:
    print("Произошла ошибка:", e)

finally:
    # Закрываем браузер после выполнения теста
    browser.quit()
