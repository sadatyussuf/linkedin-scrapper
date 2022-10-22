from linkedin import LinkedInScrapper

with LinkedInScrapper() as bot:
    bot.landing_page()
    bot.jobs_page()
    bot.select_jobs_or_companies('web developer')
    bot.search_locations('Ghana')
