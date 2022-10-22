import os
from selenium import webdriver

import linkedin.constants as const

class LinkedInScrapper(webdriver.Chrome):
    def __init__(self,drive_path=r"C:\SeleniumDrivers",closed=False):
        self.drive_path = drive_path
        self.closed = closed
        os.environ['PATH'] += self.drive_path
        super(LinkedInScrapper,self).__init__()
        self.implicitly_wait(15)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.closed:
            self.quit()

    def landing_page(self):
        self.get(const.BASE_URL)

    def jobs_page(self):
        jobs_element = self.find_element(
            by='css selector',
            value='a[data-tracking-control-name="guest_homepage-basic_guest_nav_menu_jobs"]')
        jobs_element.click()

    def select_jobs_or_companies(self,name):
        search_jobs_element = self.find_element(
            by='css selector',
            value='input[name="keywords"]'
        )
        search_jobs_element.send_keys(name)
