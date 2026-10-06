from selenium import webdriver
from selenium.webdriver.common.by import By


def test_agregar_primer_producto_al_carrito():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_boton = driver.find_element(By.ID, "login-button")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_boton.click()

        
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert contador_carrito.text == "1"

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        productos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(productos_carrito) == 1
        nombre_producto = productos_carrito[0].find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text
        assert nombre_producto == "Sauce Labs Backpack"
    finally:
        driver.quit()