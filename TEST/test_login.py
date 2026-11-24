from PAGES.Login_page import LoginPage
import pytest
from utils.reader import read_users_csv

from utils.logger import logger

@pytest.mark.flaky(reruns=2, reruns_delay=5)
@pytest.mark.parametrize("data", read_users_csv())


def test_login(driver,data):
    try:
         logger.info("Iniciando prueba de Login")
         login_page = LoginPage(driver)
        
         driver.get("https://www.saucedemo.com/")
         logger.info("Pagina abierta correctamente")
        
         login_page.login(data["username"], data["password"])
         logger.info("Credenciales ingresadas correctamente")
        
         if data["tipo_usuario"] == "correcto":
                assert "inventory.html" in driver.current_url
                logger.info("Login exitoso")
        
         elif data["tipo_usuario"] == "incorrecto":
                error = login_page.obtener_mensaje_de_error()
                assert "Epic sadface" in error
                logger.info("Prueba de mensaje de error correcta")

    except Exception:
        logger.exception("Error durante prueba de Login")
        raise
    

   



    


