<--scraper.py-->

Simple and effective web scraper utilizing the BeautifulSoup Python library aimed at scraping sites like Zillow and Craigslist, or even local real estate listings, returning title, price, and contact

    - This allows for automaition of real estate prospecting by gathering FSBO data


<--database.py-->

Using SQLite for simplicity and proof of concept, we connect to the database and create the necessary fields to store our data. The functions "create_database" and "save_listings" provide all the functionality that is needed here

With the "filter_listings" function we take max and min price as parameters to target a specific price range to return


<--outreach.py-->

Using the smtplib library, we automate the proccess of sending prospecting emails. The "send_email" function takes parameters of email address, subject and message to automate the sending proccess, while the "send_prospecting_emails" functions establishes the email framework