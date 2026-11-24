from behave import given,when,then
from PAGES.Login_page import LoginPage

@given("que el usuario se encuentre en la pagina del login")
def step_usuario_en_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.abrir_pagina()

@when('ingresa en los campos de datos "{usuario}" y "{password}"')
def step_ingresa_datos(context, usuario,password):
    if usuario == "VACIO":
        usuario = ""

    if password == "VACIO":
        password = ""
        
    context.login_page.ingresar_usuario(usuario)
    context.login_page.ingresar_contraseña(password)

@when("hace click en el boton de login")
def step_hace_click_login(context):
    context.login_page.hacer_click_en_login()   

@then("deberia ingresar al inventario")
def step_deberia_ingresar_inventario(context):
    assert "/inventory.html" in context.driver.current_url

@then('deberia mostrarse el mensaje error "{mensaje}" ')
def step_deberia_mostrar_error(context, mensaje):
    error = context.login_page.obtener_mensaje_error()
    assert mensaje in error, f"Se esperaba '{mensaje}', pero se obtuvo {error}"


    