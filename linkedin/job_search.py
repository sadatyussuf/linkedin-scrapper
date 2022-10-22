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
