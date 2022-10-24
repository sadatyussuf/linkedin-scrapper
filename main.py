from linkedin import LinkedInScrapper

with LinkedInScrapper() as bot:
    bot.landing_page()
    bot.jobs_page()
    bot.select_jobs_or_companies('web developer')
    bot.search_locations('Ghana')
    bot.search_submit()
    bot.select_experience_level('Internship','Entry')
    bot.refresh()
    # takes a number of the results you want
    bot.job_results()
