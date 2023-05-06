# Amazon_Web_Scraper
This code is for web scraping the price and title of a particular Amazon product using Beautiful Soup.
It stores the data in a CSV file and creates a new row each time the program is run.
The code runs on an infinite loop with a sleep time of 24 hours to update the data daily.
There is also an option to send an email notification if the price falls below a certain level, which is commented out for the user's reference.
The code reads the data from the CSV file and displaying it as a pandas dataframe.
