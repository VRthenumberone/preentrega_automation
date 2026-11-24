from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_pagina(self):
        self.driver.get("https://www.saucedemo.com/")

    def ingresar_usuario(self, username="standard_user"):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def ingresar_contraseña(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def hacer_click_en_login(self):
        self.driver.find_element(By.ID, "login-button").click()

    def obtener_mensaje_de_error(self):
       texto_error = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".error > h3")))
       return texto_error.text
    

    def login(self, username, password):
        self.ingresar_usuario(username)
        self.ingresar_contraseña(password)
        self.hacer_click_en_login()
