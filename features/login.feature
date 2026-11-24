Feature: Inicio de sesion

   Background:
      Given que el usuario se encuentre en la pagina del login
 
   Scenario: Inicio de sesion exitoso
      When ingresa en los campos de datos "standard_user" y "secret_sauce"
      And hace click en el boton de login
      Then deberia ingresar al inventario

   Scenario: Login ivalido con contraseña incorrecta
      When ingresa en los campos de datos "standard_user" y "1234"
      And hace click en el boton de login
      Then deberia mostrarse el mensaje error "Epic sadface: Username and password do not match any user in yhis service"

   Scenario Outline: Login invalido con diferentes credenciales
      When ingresa en los campos de datos "<usuario>" y "<password>"
      And hace click en el boton de login
      Then deberia mostrarse el mensaje error "<mensaje>"

      Examples:
        |usuario|password|mensaje|
        |standard_user|1234|Epic sadface: Username and password do not match any user in yhis service|
        |standart_user|secret_sauce|Epic sadface: Username and password do not match any user in yhis service|
        |VACIO|secret_sauce|Epic sadface: Username is required|
        |standard_user|VACIO|Epic sadface: Password is required|
