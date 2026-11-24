from PAGES.Login_page import LoginPage
from PAGES.inventory_page import InventoryPage
from utils.logger import logger


def test_inventory(driver):
    try:

             
     logger.info("Inicializando la prueba de inventario")
     Login_page = LoginPage(driver)
     inventory_page = InventoryPage(driver)


     logger.info("Igresando a la pagina web")
     driver.get("https://www.saucedemo.com/")

     logger.info("Ingresando credenciales de usuario")
     Login_page.login("standard_user", "secret_sauce")
     logger.info("Credenciales ingresadas correctamente")


     productos = inventory_page.obtener_productos() 
     logger.info("Productos obtenidos")


     assert len(productos) > 0
     logger.info("Se encontraron productos en el inventario")

     assert inventory_page.obtener_primer_producto() == "Sauce Labs Backpack"
     assert inventory_page.obtener_precio_primer_producto() == "$29.99"  
     logger.info("Prueba de integridadde lainformacion de productos validada")


     assert inventory_page.menu_visible()
     logger.info("Prueba de visibilidad del menú en la pagina validada")

     assert inventory_page.filtro_visible()    
     logger.info("Prueba de visibilidad del filtro en la pagina validada")


    except Exception:
        logger.exception("Error durante prueba de inventario")
        raise          
