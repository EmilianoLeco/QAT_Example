import os
from os.path import dirname
from time import sleep
from behave import *
from nose.tools import assert_equal
from selenium.webdriver.common.by import By
from Tools.read_csv import read_csv
from Tools.months import months

# Directorio al archivo de datos
dirpath = os.path.abspath(os.path.dirname(__file__))
dirname(dirpath)
camino_csv = (dirname(dirname(dirpath))) + "\\features\Datos_Registro.csv"

# Datos que necesita el caso
datos_registro = read_csv(camino_csv)[0]  # Cargo la primera linea

# Tiempo seteado general
time = 2


@given('Navego a la página de "{URL}"')
def step_impl(context, URL):
    context.home_page.navigate('{}'.format(URL))
    assert_equal(context.home_page.get_page_title(), "My Store", msg="Error al acceder a la pagina")
    sleep(1 + time)

@step('Realizo Click en "Sign in"')
def step_impl(context):
    context.home_page.click_element(By.XPATH, "//a[@class='login']")
    sleep(time)

@step('Me "{SELECT}" con mi correo electronico "{MAIL}"')
def step_impl(context, MAIL, SELECT):
    context.home_page.search(MAIL, SELECT)
    sleep(time)

@when('ingreso mis datos para registrarme')
def step_impl(context):
    # YOUR PERSONAL INFORMATION
    # Title
    if datos_registro[0] == 'Mr':
        context.home_page.click_element_By_ID('id_gender1')
    else:
        context.home_page.click_element_By_ID('id_gender2')
    # First name
    context.home_page.fill_By_ID(datos_registro[1], ('customer_firstname'))
    sleep(time)
    # Last name
    context.home_page.fill_By_ID(datos_registro[2], ('customer_lastname'))
    # Password
    context.home_page.fill_By_ID(datos_registro[3], ('passwd'))
    # Date of Birth
    fecha = datos_registro[4].split("\\")
    mes = months(fecha[1])
    context.home_page.select_element_By_ID(fecha[0], ('days'))
    context.home_page.select_element_By_ID(mes, ('months'))
    context.home_page.select_element_By_ID(fecha[2], ('years'))

    # YOUR ADDRESS
    # First name
    #context.home_page.fill_By_ID(datos_registro[1], ('firstname'))
    # Last name
    #context.home_page.fill_By_ID(datos_registro[2], ('lastname'))
    # Address
    context.home_page.fill_By_ID(datos_registro[5], ('address1'))
    # City
    context.home_page.fill_By_ID(datos_registro[6], ('city'))
    # State
    context.home_page.select_element_By_ID(datos_registro[7], ('id_state'))
    # Zip/Postal Code
    context.home_page.fill_By_ID(datos_registro[8], ('postcode'))
    # Mobile phone
    context.home_page.fill_By_ID(datos_registro[9], ('phone_mobile'))
    # Alias
    context.home_page.fill_By_ID(datos_registro[10], ('alias'))
    sleep(time)
    # submitAccount
    context.home_page.click_element_By_ID('submitAccount')
    sleep(time+5)


@then('Verifico el "{SELECCION}" correcto')
def step_impl(context, SELECCION):
    texto = context.search_results.get_text(By.XPATH, '//*[@id="center_column"]/p')
    texto_ok = "Welcome to your account. Here you can manage all of your personal information and orders."
    assert_equal(texto, texto_ok, msg="El registro no fue correcto")
    sleep(time)
