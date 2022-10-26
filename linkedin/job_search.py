import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

    def login_parameters(self, username, password):

        sign_in_element = self.find_element(
            by='css selector',
            value='a[data-tracking-control-name="guest_homepage-basic_nav-header-signin"]'
        )
        sign_in_element.click()

        username_element = self.find_element(
            by='css selector',
            value='#username'
        )
        password_element = self.find_element(
            by='css selector',
            value='#password'
        )

        username_element.send_keys(username)
        password_element.send_keys(password)

        submit_element = self.find_element(
            by='css selector',
            value='button[data-litms-control-urn="login-submit"]'
        )
        submit_element.click()

    def set_jobs_page(self):
        search_element = self.find_element(
            by='css selector',
            value='.search-global-typeahead__input'
        )
        search_element.send_keys(Keys.ENTER)
        get_all_filters = self.find_elements(
            by='css selector',
            value='.search-reusables__primary-filter'
        )
        for job_filter_pill in get_all_filters:
            button_element = job_filter_pill.find_element(
                by='css selector',
                value="button"
            )
            button_text = str(button_element.get_attribute('innerHTML')).strip().lower()
            if button_text == 'jobs':
                job_filter_pill.click()

    def jobs_page(self):
        jobs_element = self.find_element(
            by='css selector',
            value='a[data-tracking-control-name="guest_homepage-basic_guest_nav_menu_jobs"]')
        jobs_element.click()

    def select_jobs_or_companies(self, job_name):
        search_jobs_element = self.find_element(
            by='css selector',
            value='.jobs-search-box__text-input'
            # value='input[name="keywords"]'
        )
        search_jobs_element.send_keys(job_name)
        search_jobs_element.send_keys(Keys.ENTER)

    def search_locations(self, location_name):
        search_location_element = self.find_element(
            by='css selector',
            # value='#jobs-search-box-location-id-ember299'
            value='input[aria-label*="City"]'
        )
        search_location_element.clear()
        search_location_element.send_keys(location_name)
        search_location_element.send_keys(Keys.ENTER)

    def search_submit(self):
        search_submit_element = self.find_element(
            by='css selector',
            value='.jobs-search-box__submit-button'
            # value='button[data-tracking-control-name="public_jobs_jobs-search-bar_base-search-bar-search-submit"]'
        )
        search_submit_element.click()

    def select_experience_level(self, *experiece_levels):
        get_all_filters = self.find_elements(
            by='css selector',
            value='.search-reusables__primary-filter'
        )
        print(len(get_all_filters))
        for experience_filter_pill in get_all_filters:
            button_element = experience_filter_pill.find_element(
                by='css selector',
                value="button"
            )
            print(f'button_element: \n {button_element}')
            button_text = str(button_element.get_attribute('innerHTML')).strip().lower()
            print()
            print(f'button_text: \n {button_text}')
            if 'experience ' in button_text:
                print('======================= If statement =========================================')
                print(f'button_text: \n {button_text}')
                experience_filter_pill.click()
        # selects the sibling element with the pop-up values in them

                select_experiece_level_element =  experience_filter_pill.find_element(
                    by='css selector',
                    value='form'
                    # value='button[data-tracking-control-name="public_jobs_f_E"] + div'
                )
                # selects all the Experience values
                select_values = select_experiece_level_element.find_elements(
                    by='css selector',
                    value='.search-reusables__collection-values-item'
                    # value='.filter-values-container__filter-value'
                )
                # loops through all the user input experience_levels
                for experiece_level in experiece_levels:
                    for select_value in select_values:
                        label_element = select_value.find_element(
                            by='css selector',
                            value='.t-14 t-black--light t-normal'
                            # value='label'
                        )
                        if experiece_level.lower() in str(label_element.get_attribute('innerHTML')).lower():
                            select_value.click()
                submit_element = select_experiece_level_element.find_element(
                    by='css selector',
                    value='button[data-control-name="filter_show_results"]'
                    # value='button[data-tracking-control-name="public_jobs_f_E"]'
                )
                submit_element.click()

    def job_results(self, results_num: int = 20):
        results_container = self.find_element(
            by='css selector',
            value='#main-content'
        )

        results = JobResults(results_container, results_num)
        results.get_results()
