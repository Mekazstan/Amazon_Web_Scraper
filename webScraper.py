# Importing necessary libraries
from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib

# Defining function to scrape Amazon product data
def check_price():ls
    # specify the URL of the product page
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

    # # specifying the headers to simulate browser request
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", 
           "Accept-Encoding":"gzip, deflate", 
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
           "DNT":"1",
           "Connection":"close", 
           "Upgrade-Insecure-Requests":"1"} #  "url": "http://httpbin.org/get"   
    
    #  making request to the URL with the headers specified above
    page = requests.get(URL, headers=headers)

    # parsing the HTML content of the page with BeautifulSoup
    soup1 = BeautifulSoup(page.content, "html.parser")

    # prettify the parsed HTML content
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    # extracting the title and price of the product from the parsed HTML content
    title = soup2.find(id="productTitle").get_text()

    price = soup2.find(class_='a-offscreen').get_text()

    # Clean up the data a little bit
    price = price.strip()[1:]
    title = title.strip()

    # Create a Timestamp for your output to track when data was collected
    import datetime

    today = datetime.date.today()
    
    # appending the extracted data to a CSV file
    import csv 

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]
    
    #Now we are appending data to the csv
    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
    
# Automating the whole process to run on Autopilot. It runs check_price after a set time and inputs data into your CSV

while(True):
    check_price()
    time.sleep(86400)
    
    
import pandas as pd
# reading the data from the CSV file into a pandas dataframe
df = pd.read_csv(r'Input file name here')

# printing the dataframe
print(df)



# Defining a function to send an email notification when the price drops below a certain level (for fun)

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('xxxxxxxxxxx','xxxxxxxxxxxxxx')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Dave, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'xxxxxxxxxxxxxx',
        msg
     
    )

