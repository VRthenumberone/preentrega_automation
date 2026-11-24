import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_exitoso():
   
   driver = webdriver.Chrome()

   driver.implicitly_wait(10)

   try:
        driver.get("https://www.saucedemo.com/")


        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_boton = driver.find_element(By.ID, "login-button")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_boton.click()

        assert "inventory.html" in driver.current_url


        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs"


        titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
        assert titulo.text == "Products"

   finally:
        driver.quit()




