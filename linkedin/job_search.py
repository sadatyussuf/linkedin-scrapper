import os
from selenium import webdriver

import linkedin.constants as const
from linkedin.job_report import JobResults

class LinkedInScrapper(webdriver.Chrome):
    def __init__(self, drive_path=r"C:\SeleniumDrivers", closed=False):
        self.drive_path = drive_path
        self.closed = closed
        os.environ['PATH'] += self.drive_path
        super(LinkedInScrapper, self).__init__()
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

    def select_jobs_or_companies(self, job_name):
        search_jobs_element = self.find_element(
            by='css selector',
            value='input[name="keywords"]'
        )
        search_jobs_element.send_keys(job_name)

    def search_locations(self, location_name):
        search_location_element = self.find_element(
            by='css selector',
            value='input[name="location"]'
        )
        search_location_element.clear()
        search_location_element.send_keys(location_name)

    def search_submit(self):
        search_submit_element = self.find_element(
            by='css selector',
            value='button[data-tracking-control-name="public_jobs_jobs-search-bar_base-search-bar-search-submit"]'
        )
        search_submit_element.click()

    def select_experience_level(self, *experiece_levels):

        # first, clicks the Experience_Level to bring up the pop-up for the experience_type
        click_experience_element = self.find_element(
            by='css selector',
            value='button[data-tracking-control-name="public_jobs_f_E"]'
        )
        click_experience_element.click()
        # selects the sibling element with the pop-up values in them
        select_experiece_level_element = self.find_element(
            by='css selector',
            value='button[data-tracking-control-name="public_jobs_f_E"] + div'
        )
        # selects all the Experience values
        select_values = select_experiece_level_element.find_elements(
            by='css selector',
            value='.filter-values-container__filter-value'
        )
        # loops through all the user input experience_levels
        for experiece_level in experiece_levels:
            for select_value in select_values:
                label_element = select_value.find_element(
                    by='css selector',
                    value='label'
                )
                if experiece_level.lower() in str(label_element.get_attribute('innerHTML')).lower():
                    select_value.click()
        submit_element = select_experiece_level_element.find_element(
            by='css selector',
            value='button[data-tracking-control-name="public_jobs_f_E"]'
        )
        submit_element.click()

    def job_results(self, results_num:int=20):
        results_container = self.find_element(
            by='css selector',
            value='#main-content'
        )

        results = JobResults(results_container,results_num)
        results.get_results()
