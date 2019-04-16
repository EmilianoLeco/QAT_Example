from time import sleep
from behave import *


# Tiempo seteado general
time = 2


@When('Ingreso mi correo electronico:"{MAIL}" y contraseña:"{PASSWORD}"')
def step_impl(context, MAIL, PASSWORD):
    context.home_page.fill_By_ID(MAIL, ('email'))
    context.home_page.fill_By_ID(PASSWORD, ('passwd'))
    context.home_page.click_element_By_ID('SubmitLogin')
    sleep(time)


