from selenium import webdriver
from selenium.webdriver.common.by import By

def open_and_find():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')

    username = driver.find_element(By.ID, 'user-name')
    password = driver.find_element(By.ID, 'password')
    submit = driver.find_element(By.ID, 'user-name')

    if username and password and submit:
        print('Элементы найдены')
    else:
        print('Элементы не найдены')

open_and_find()




