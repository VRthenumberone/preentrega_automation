

import pytest
from selenium import webdriver

import pytest_html
import pathlib
import base64


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture
def base_url():
    return "https://reqres.in/api" # La pagina de donde sacamos la API


@pytest.fixture
def headers():
    return {"x-api-key": "pro_4231c8f84eaf67e9613b6501847fa8bb648105e6bd44eec0ba60529810b8610a"}
# La llave que nos dá la pagina de la API (KEY)

# HERRAMIENTA PARA SACAR CAPTURA DE UN ERROR Y AGREGARLO AL REPORTE HTML

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            carpeta = pathlib.Path("reports/screenshots")
            carpeta.mkdir(parents=True, exist_ok=True)
            archivo = carpeta / f"{item.name}.png"

            driver.save_screenshot(str(archivo))

            imagen = base64.b64encode(archivo.read_bytes()).decode("utf-8")
            report.extras = [pytest_html.extras.png(imagen, name="Screenshot")]


