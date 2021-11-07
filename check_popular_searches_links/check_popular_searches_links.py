# This file includes methods to verify if Popular Searches links
# work correctly

from selenium import webdriver
import os
import check_popular_searches_links.constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class CheckPopularSearches(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\TestEnv3\selenium browser drivers",
                 teardown=False):  # teardown = True to quit the page
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        # instantiate the class CheckPopularSearches
        # instantiate an instance of the webriver.chorme class
        super(CheckPopularSearches, self).__init__()
        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        # method to open the web page
        self.get(const.BASE_URL)

    def scroll_down_to_popular_searches(self):
        # method to scroll the page until the expected element is visible
        popular_searches_flag = self.find_element_by_class_name('fa2044b7')
        self.execute_script("arguments[0].scrollIntoView();", popular_searches_flag)

        # method to scroll the page until the expected element is in center of the page
        # desired_y = (popular_searches_flag.size['height']/2) + popular_searches_flag.location['y']
        # current_y = (self.execute_script('return window.innerHeight')/2) +
        #              self.execute_script(('return window.pageYOffset'))
        # scroll_y_by = desired_y - current_y
        # self.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

    def select_popular_searches_to_rent(self):
        # method to select the tab 'To Rent'
        popular_searches_to_rent_element = self.find_elements_by_class_name('d8530318')
        for i in range(len(popular_searches_to_rent_element)):
            if str(popular_searches_to_rent_element[i].get_attribute('innerHTML')) == 'To Rent':
                popular_searches_to_rent_element[i].click()
                break

    def validate_visible_links(self):
        # method to check if visible links are functioning correctly
        delay = 10
        visible_links = [
            ("/to-rent/apartments/dubai/dubai-marina/",
             'Apartments for rent in Dubai Marina'),
            ("/to-rent/apartments/dubai/jumeirah-village-circle-jvc/",
             'Apartments for rent in Jumeirah Village Circle (JVC)'),
            ("/to-rent/apartments/dubai/jumeirah-lake-towers-jlt/",
             'Apartments for rent in Jumeirah Lake Towers (JLT)'),
            ("/to-rent/apartments/dubai/downtown-dubai/",
             'Apartments for rent in Downtown Dubai'),
            ("/to-rent/apartments/dubai/business-bay/",
             'Apartments for rent in Business Bay')
                ]

        for url, text in visible_links:
            check_link = WebDriverWait(self, delay).until(
                EC.presence_of_element_located((By.XPATH, '//a[@href="'+url+'"]'))
            )  # explicit wait
            check_link.click()

            try:
                my_elem = WebDriverWait(self, delay).until(
                    EC.presence_of_element_located((By.CLASS_NAME, '_2aa3d08d')))
                if str(my_elem.get_attribute('innerHTML')) == text:
                    print(f"The search page for {text} is loaded correctly!")
                else:
                    print(f"The search page for {text} is not the expected one!")

            except TimeoutException:
                print(f"Loading page for {text} took too much time!")

            self.back()
            self.implicitly_wait(delay)
            self.select_popular_searches_to_rent()

    def view_all_links(self):
        # method to make all links visible
        view_all_element = self.find_elements_by_class_name('_29dd7f18')
        view_all_element[2].click()

    def validate_hidden_links(self):
        # method to check if hidden links are functioning correctly
        delay = 10
        invisible_links = [
            ("/to-rent/apartments/dubai/palm-jumeirah/",
             'Apartments for rent in Palm Jumeirah'),
            ("/to-rent/apartments/dubai/dubai-sports-city/",
             'Apartments for rent in Dubai Sports City'),
            ("/to-rent/apartments/dubai/jumeirah-beach-residence-jbr/",
             'Apartments for rent in Jumeirah Beach Residence (JBR)'),
            ("/to-rent/apartments/dubai/the-greens/",
             'Apartments for rent in The Greens'),
            ("/to-rent/apartments/dubai/dubai-silicon-oasis/",
             'Apartments for rent in Dubai Silicon Oasis'),
            ("/to-rent/apartments/dubai/motor-city/",
             'Apartments for rent in Motor City'),
            ("/to-rent/apartments/dubai/green-community/",
             'Apartments for rent in Green Community'),
            ("/to-rent/apartments/dubai/dubai-production-city-impz/",
             'Apartments for rent in Dubai Production City (IMPZ)'),
        ]

        for url, text in invisible_links:
            check_link = WebDriverWait(self, delay).until(
                EC.presence_of_element_located((By.XPATH, '//a[@href="'+url+'"]'))
            )  # explicit wait
            check_link.click()

            try:
                my_elem = WebDriverWait(self, delay).until(
                    EC.presence_of_element_located((By.CLASS_NAME, '_2aa3d08d')))
                if str(my_elem.get_attribute('innerHTML')) == text:
                    print(f"The search page for {text} is loaded correctly!")
                else:
                    print(f"The search page for {text} is not the expected one!")

            except TimeoutException:
                print(f"Loading page for {text} took too much time!")

            self.back()
            self.implicitly_wait(delay)
            self.select_popular_searches_to_rent()
            self.view_all_links()