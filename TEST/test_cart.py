from selenium import webdriver

from PAGES.Login_page import LoginPage
from PAGES.inventory_page import InventoryPage
from PAGES.cart_page import CartPage

from utils.reader import read_productos_json

from utils.logger import logger



def test_cart(driver):
    try: 

     logger.info("Iniciando prueba de carrito")
     login_page = LoginPage(driver)
     inventory_page = InventoryPage(driver)
     cart_page = CartPage(driver)


     logger.info("Ingresando a la pagina web")
     driver.get("https://www.saucedemo.com/")


     logger.info("Realizando login")
     login_page.login("standard_user", "secret_sauce")
     logger.info("Login realizado con éxito")


     logger.info("Leyendo el primer producto del JSON")
     producto = read_productos_json()[0] #Leer primer producto json

     logger.info("Agregando producto del JSON")
     inventory_page.agregar_producto(producto["nombre"]) #Agregar producto json

     
     assert inventory_page.obtener_contador_carrito() == "1"
     logger.info("Validando contador del carrito")


     logger.info("Ir a ls pagina del carrito") 
     inventory_page.ir_al_carrito()


     assert cart_page.obtener_nombre_producto() == producto["nombre"]
     logger.info("Prueba nombre contra el JSON validada")
 

     assert cart_page.obtener_precio_producto() == producto["precio"]
     logger.info("Prueba precio contra el JSON validada")   


    except Exception:
        logger.exception("Error durante prueba de carrito")
        raise 

