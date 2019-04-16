Feature: Registro

  Scenario: Registro en Pagina
     Given Navego a la página de "http://automationpractice.com/index.php"
     And Realizo Click en "Sign in"
     And Me "Registro" con mi correo electronico "automation_7@selenium.com"
     When ingreso mis datos para registrarme
     Then Verifico el "registro" correcto