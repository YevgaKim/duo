import configparser
import time

from keyboard import wait
from mtranslate import translate
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

config = configparser.ConfigParser()
config.read("config.ini")
phone = config['INFO']['phone']
password = config['INFO']['password']

driver = webdriver.Chrome(
        executable_path="C:\\Users\\ЯкименкоЄвгенійСергі\\source\\repos\\duo\\chromedriver.exe",
        )

try:
    driver.get(url="https://www.duolingo.com/learn")
    main_window = driver.current_window_handle
    
    button1 = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, "WOZnx")))
    button1.click()
    button2 = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, "_3zB0T")))
    button2.click()
    time.sleep(2)
    for handle in driver.window_handles:
        if handle != main_window:
            driver.switch_to.window(handle)
            break

    WebDriverWait(driver, 8).until(EC.url_contains("https://www.facebook.com")) 
    inputs = driver.find_elements(By.CLASS_NAME, "inputtext")
    inputs[0].send_keys(phone)
    inputs[1].send_keys(password)
    time.sleep(1)
    actions = ActionChains(driver)
    login = driver.find_element(By.ID,"loginbutton")
    actions.click(login)
    actions.perform()
    driver.switch_to.window(main_window)
    WebDriverWait(driver, 20).until(EC.url_contains("learn")) 
    time.sleep(5)
    first = driver.find_element(By.CLASS_NAME,"AMXUp")
    actions.click(first)
    second = driver.find_element(By.CLASS_NAME,"AMXUp")
    actions.click(second)
    actions.perform()
    driver.execute_script("window.scrollTo(0, 6500);")
    time.sleep(1)
    all_levels = driver.find_elements(By.CLASS_NAME, "_2PyNj")
    actions.click(all_levels[0]).perform()
    time.sleep(1.5)
    actions.click(driver.find_element(By.CLASS_NAME,"_3HhhB")).perform()
    time.sleep(13)
    actions.click(driver.find_element(By.CLASS_NAME,"_3HhhB")).perform()

    while True:
        #wait("\\")
        try:
            elements = driver.find_elements(By.CLASS_NAME,"_13doy")
            element = driver.find_element(By.CLASS_NAME,"_2EMUT")
            element.clear()
            words = [i.text for i in elements]
            answer = " ".join(words)
            result = translate(answer,"en","ru")
            print(result)
            element.send_keys(result)
            time.sleep(1)
            actions.click(driver.find_element(By.CLASS_NAME,"_3HhhB")).perform()
            time.sleep(0.5)
            actions.click(driver.find_element(By.CLASS_NAME,"_3HhhB")).perform()
            time.sleep(2)
        except:
            actions.click(driver.find_element(By.CLASS_NAME,"_3HhhB")).perform()
            time.sleep(1)
            continue
            

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

