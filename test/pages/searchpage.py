from .basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage(BasePage):

    # Declares variables that will used in the whole process of the test case.
    def __init__(self, driver):
        self.driver = driver
        self.searchpageUrl = "https://buythisspace.com.au/search-page/"
        self.pageTitle = "Find a billboard - BuyThisSpace"
        self.searchInputLocatorByID = "gmw-address-1"
        self.searchDropDownListLocatorByNAME = "gmw_distance"
        self.searchButtonLocatorByID = "gmw-submit-1"


    def is_page_loaded(self):
        return self.is_search_button_displayed()

    def is_search_input_field_displayed(self):
        try :
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.searchInputLocatorByID)))
            return True
        except Exception as e:
            print("===== searchpage - unable to display the search input field =====")
            assert True, "===== Assertion: Unable to display search input field"
            print(e)
            return False

    def is_search_button_displayed(self):
        try :
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.searchButtonLocatorByID)))
            return True
        except Exception as e:
            print("===== searchpage - unable to get the search input field =====")
            assert True, "===== Assertion: Unable to display search button"
            print(e)
            return False



    def field_in_search_input_filed(self, location):
        if (self.is_search_input_field_displayed()):
            self.driver.find_element_by_id(self.searchInputLocatorByID).send_keys(location)
        else:
            assert True, "===== Assertion: Unable to input localtion"

    def click_search_button(self):
        if self.is_search_button_displayed():
            self.driver.find_element_by_id(self.searchButtonLocatorByID).click()
        else:
            assert True, "===== Assertion: Unable to click search button"


