from linkedin import LinkedInScrapper


# bot = LinkedInScrapper()
# bot.landing_page()
with LinkedInScrapper() as bot:
    bot.landing_page()
