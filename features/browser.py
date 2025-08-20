from selenium import webdriver
from os.path import dirname
import os

dirpath = os.path.abspath(os.path.dirname(__file__))
chromedriver_path = os.path.join(dirname(dirpath), "chromedriver.exe")


class Browser(object):
    def __init__(self):
        self.driver = webdriver.Chrome(chromedriver_path)
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()
