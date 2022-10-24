
from selenium.webdriver.remote.webelement import WebElement

class JobResults:
    def __init__(self,results_container:WebElement,results_num):
        self.results_container = results_container
        self.results_num = results_num
        self.results_values = self.pull_values()

    def pull_values(self):
         return(
             self.find_elements(
            by='css selector',
            value='.jobs-search__results-list'
        )
         )
    def get_results(self):
        print(len(self.results_values))
        # for result in self.results_values
