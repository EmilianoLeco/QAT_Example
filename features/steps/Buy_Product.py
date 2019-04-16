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

@when('Busco "{PRODUCTO}"')
def step_impl(context, PRODUCTO):
    context.home_page.fill_By_ID(PRODUCTO,('search_query_top'))
    context.home_page.click_element(By.XPATH, '//*[@id="searchbox"]/button')
    sleep(time+2)


@step('Selecciono producto')
def step_impl(context):
    context.home_page.click_element(By.XPATH, '//li[1]//div[2]/h5/a')
    sleep(time+5)

@step('Añadir a la cesta')
def step_impl(context):
    context.home_page.click_element_By_ID('add_to_cart')
    sleep(time+3)
    texto = context.search_results.get_text(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[1]/h2')
    print(texto.strip())
    assert_equal(texto.strip(), "Product successfully added to your shopping cart", msg="Error al añadir a la cesta")

@step('Finalizo la compra')
def step_impl(context):
    # Checkout
    context.home_page.click_element(By.XPATH, "//a[@class='btn btn-default button button-medium']/span")
    sleep(time+3)
    # 01. Summary
    context.home_page.click_element(By.XPATH, "//a[@class='button btn btn-default standard-checkout button-medium']/span")
    sleep(time)
    print("a")
    # 03. Address
    context.home_page.click_element(By.XPATH, "//*[@id='center_column']/form/p/button/span")
    sleep(time)
    print("b")
    # 04. Shipping
    # Checkbox
    context.home_page.click_checkbox(By.XPATH, '//*[@id="cgv"]')
    sleep(time)
    context.home_page.click_element(By.XPATH, "//*[@id='form']/p/button/span")
    sleep(time)
    # 05. Payment
    # Selecciono forma de pago
    context.home_page.click_element(By.XPATH, "//*[@id='HOOK_PAYMENT']/div[1]/div/p")
    sleep(time)
    # Valido Resumen de compra antes de Confirmar
    texto = context.search_results.get_text(By.XPATH, '//*[@id="center_column"]/form/div/p[1]/strong')
    assert_equal(texto.strip(), "You have chosen to pay by bank wire. Here is a short summary of your order:", msg="Error al ver resumen")
    sleep(time)
    # Finalizo compra
    context.home_page.click_element(By.XPATH, "//*[@id='cart_navigation']/button")

@then('Valido compra exitosa')
def step_impl(context):
    # Valido Compra exitosa!!
    texto = context.search_results.get_text(By.XPATH, '//*[@id="center_column"]/div/p/strong')
    assert_equal(texto.strip(), "Your order on My Store is complete.", msg="Error en la compra")
    sleep(time)