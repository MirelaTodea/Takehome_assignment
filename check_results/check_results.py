# This file includes CheckResults class with methods to verify if the results match
# the search criteria

from selenium import webdriver
import os
import check_results.constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

delay = 10

class CheckResults(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\TestEnv3\selenium browser drivers",
                 teardown=False):  # teardown=True to quit the page
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        # instantiate the class CheckResults
        # instantiate an instance of the webriver.chorme class
        super(CheckResults, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        # method to open the web page
        self.get(const.BASE_URL)

    def select_location(self, searched_location, desired_location):
        # method to search the desired location
        search_field = self.find_element_by_class_name('_6a3a3de9')
        search_field.click()
        search_field.clear()
        search_field.send_keys(searched_location)
        self.implicitly_wait(5)

        result_list = WebDriverWait(self, delay).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "'+desired_location+'")]'))
        )
        self.implicitly_wait(5)
        result_list.click()

    def properties_for_sale(self):
        # method to select properties 'For Sale'
        purpose_field = self. find_element_by_class_name("e7c6503c")
        purpose_field.click()
        select_buy = WebDriverWait(self, delay).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Buy"]'))
        )
        select_buy.click()

    def find_properties_with_all_attributes(self):
        # method to search properties
        hit_find_button = self.find_element_by_css_selector(
            'a[aria-label="Find button"]'
        )
        hit_find_button.click()

    def verify_location(self, desired_location):
        # method to verify the location
        verify_location_list = self.find_elements_by_css_selector(
            'div[aria-label="Location"]'
        )
        for i in range(len(verify_location_list)):
            if desired_location in str(verify_location_list[i].get_attribute('innerHTML')):
                print(f"Property {verify_location_list[i].text} contain the selected location.")
            else:
                print(f"Property {verify_location_list[i].text} does not contain the selected location.")
