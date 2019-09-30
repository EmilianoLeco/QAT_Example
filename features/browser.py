from selenium import webdriver
from os.path import dirname
import os

dirpath = os.path.abspath(os.path.dirname(__file__))
dirname(dirpath)
chromedriver_path = (dirname(dirpath)) + "\\chromedriver.exe"

print(chromedriver_path)

class Browser(object):
    driver = webdriver.Chrome(chromedriver_path)
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.quit()