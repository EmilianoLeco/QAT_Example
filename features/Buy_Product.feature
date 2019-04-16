Feature: Login y Compra de producto

  Scenario: Login en la Pagina
     Given Navego a la página de "http://automationpractice.com/index.php"
       And Realizo Click en "Sign in"
      When Ingreso mi correo electronico:"automation_7@selenium.com" y contraseña:"12345678"
      Then Verifico el "ingreso" correcto


  Scenario: Compra de producto
     Given Navego a la página de "http://automationpractice.com/index.php"
      When Busco "Dress"
       And Selecciono producto
       And Añadir a la cesta
       And Finalizo la compra
      Then Valido compra exitosa