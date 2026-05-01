import requests
import os
from datetime import datetime, timedelta
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Alpha Vantage API Config
ALPHA_VANTAGE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
ALPHA_VANTAGE_URL = 'https://www.alphavantage.co/query'

# News API Config
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_URL = 'https://newsapi.org/v2/everything'

# Twilio Config
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.environ.get("TWILIO_FROM_NUMBER")
TWILIO_TO_NUMBER = os.environ.get("TWILIO_TO_NUMBER")

## STEP 1: Use https://www.alphavantage.co
parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': ALPHA_VANTAGE_API_KEY
}

response = requests.get(url=ALPHA_VANTAGE_URL, params=parameters)
data = response.json()

yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
daily_data = data.get('Time Series (Daily)', {})

# Find the last available date before yesterday
days_back = 2
day_before_yesterday = None
while not day_before_yesterday and days_back < 10: # Added safety break
    date_to_check = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
    if date_to_check in daily_data:
        day_before_yesterday = date_to_check
    days_back += 1

if yesterday_date in daily_data and day_before_yesterday:
    yesterday_close_price = float(daily_data[yesterday_date]['4. close'])
    day_before_yesterday_close_price = float(daily_data[day_before_yesterday]['4. close'])

    ten_percent_of_yesterday_closing_price = (5 / 100) * yesterday_close_price
    
    # Calculate percentage change
    percentage_change = ((yesterday_close_price - day_before_yesterday_close_price) / day_before_yesterday_close_price) * 100
    symbol = '🔺' if percentage_change > 0 else '🔻'

    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then get news.
    if abs(percentage_change) >= 5:
        ## STEP 2: Use https://newsapi.org
        news_api_parameters = {
            'q': COMPANY_NAME,
            'from': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
            'apikey': NEWS_API_KEY,
            'sortBy': 'popularity'
        }
        
        response = requests.get(url=NEWS_URL, params=news_api_parameters)
        news_data = response.json()
        articles = news_data.get('articles', [])
        
        ## STEP 3: Use https://www.twilio.com
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        # Send the SMS messages for the first 3 articles
        for article in articles[:3]:
            message_body = f"{STOCK}: {symbol}{abs(percentage_change):.2f}%\n"
            message_body += f"Headline: {article['title']}\n"
            message_body += f"Brief: {article['description']}\n"

            message = client.messages.create(
                body=message_body,
                from_=TWILIO_FROM_NUMBER,
                to=TWILIO_TO_NUMBER
            )
            print(f"Message Status: {message.status}")
else:
    print("Could not retrieve stock data for the specified dates.")
