from dotenv import load_dotenv
import os
from linkedin import LinkedInScrapper

load_dotenv()

my_username = os.environ.get("MY_USERNAME")
my_password = os.environ.get("MY_PASSWORD")

with LinkedInScrapper() as bot:
    bot.landing_page()
    bot.login_parameters(my_username,my_password)
    bot.refresh()
    # bot.jobs_page()
    # bot.select_jobs_or_companies('web developer')
    # bot.search_locations('Ghana')
    # bot.search_submit()
    # bot.select_experience_level('Internship','Entry')
    # takes a number of the results you want
    # bot.job_results()

