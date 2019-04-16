from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from features.browser import Browser

class HomePageLocator(object):
    # Home Page Locators

    HEADER_TEXT = (By.XPATH, "//h1")
    SEARCH_FIELD = (By.ID, "email_create")
    SUBMIT_BUTTON = (By.ID, "SubmitCreate")
    SELECTION = (By.ID, "id_gender1")


class HomePage(Browser):
    # Home Page Actions
    def click_element_By_ID(self, *locator):
        self.driver.find_element_by_id(*locator).click()


    def fill_By_ID(self, text, *locator):
        self.driver.find_element_by_id(*locator).clear()
        self.driver.find_element_by_id(*locator).send_keys(text)

    def select_element_By_ID(self,select, *locator):
        list_select = Select(self.driver.find_element_by_id(*locator))
        if locator[0] == 'days' or locator[0] == 'years':
            list_select.select_by_visible_text('{}  '.format(select))
        else:
            list_select.select_by_visible_text(select)

    def click_checkbox(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.SPACE)

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def select_element(self,select, *locator):
        Select(self.driver.find_element(*locator).click()).select_by_visible_text(select)

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def search(self, search_term, selection, *locator):
        if selection == 'Registro':
            self.fill(search_term, *HomePageLocator.SEARCH_FIELD)
            self.click_element(*HomePageLocator.SUBMIT_BUTTON)
        else:
            self.fill_By_ID(search_term, *locator)
            self.click_element_By_ID(*locator)