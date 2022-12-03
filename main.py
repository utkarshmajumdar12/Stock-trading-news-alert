import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
#API KEYS AND AUTH TOKENS
API_KEY = ""
API_KEY2 = ""
TWILIO_SID = "
TWILIO_AUTH_TOKEN = ""

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": API_KEY,
}

news_params = {
    "apiKey": API_KEY2,
    "q" : COMPANY_NAME,
}



response1 = requests.get(STOCK_ENDPOINT, params= stock_params)
data = response1.json()
closing_price_y =  float(data["Time Series (Daily)"]['2022-12-02']['4. close'])
print(f"{closing_price_y} is yesterdays closing price")


response1 = requests.get(STOCK_ENDPOINT, params= stock_params)
data = response1.json()
closing_price_dby =  float(data["Time Series (Daily)"]['2022-12-01']['4. close'])
print(f"{closing_price_dby} is day before yesterdays closing price")


pos_dif = abs(closing_price_y - closing_price_dby)
print(f"{pos_dif} is the absolute difference between yesterdays and day before yesterdays closing prices")

perc_diff =  (pos_dif/closing_price_y)*100
print(f"Percentage difference in closing prices = {perc_diff}")

if perc_diff > 3:
    response2 = requests.get(NEWS_ENDPOINT, params= news_params)
    news_data = response2.json()
    articles = news_data["articles"]
    three_articles = articles[:3]

    formatted_article = [f"Headline : {articles['title']}. \n Brief : {articles['description']}" for article in three_articles ]
    print(formatted_article)
    client1 = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for i in formatted_article:
        message = client1.message.create(
            body = i,
            from_ = "+12282564571",
            to = "+919100761207",

        )
    
