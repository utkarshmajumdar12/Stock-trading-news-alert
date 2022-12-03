import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "VW4ZAZBLKFHO84L7"
API_KEY2 = "9592b18b447d4f12b992aa535ae5ddfa"
TWILIO_SID = "SK6f823cf6430dbdce539360846fb11c39"
TWILIO_AUTH_TOKEN = "93929abef6b39a356081d475cc126eea"

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

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

response1 = requests.get(STOCK_ENDPOINT, params= stock_params)
data = response1.json()
closing_price_y =  float(data["Time Series (Daily)"]['2022-12-02']['4. close'])
print(f"{closing_price_y} is yesterdays closing price")

#TODO 2. - Get the day before yesterday's closing stock price

response1 = requests.get(STOCK_ENDPOINT, params= stock_params)
data = response1.json()
closing_price_dby =  float(data["Time Series (Daily)"]['2022-12-01']['4. close'])
print(f"{closing_price_dby} is day before yesterdays closing price")

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

pos_dif = abs(closing_price_y - closing_price_dby)
print(f"{pos_dif} is the absolute difference between yesterdays and day before yesterdays closing prices")

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
perc_diff =  (pos_dif/closing_price_y)*100
print(f"Percentage difference in closing prices = {perc_diff}")
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if perc_diff > 0:
    response2 = requests.get(NEWS_ENDPOINT, params= news_params)
    news_data = response2.json()
    articles = news_data["articles"]
    three_articles = articles[:3]
    art_title = three_articles('title')
    art_desc = three_articles['description']
    print(art_title)

    formatted_article = [f"Headline : {articles['title']}. \n Brief : {articles['description']}" for article in three_articles ]
    print(formatted_article)
    client1 = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for i in formatted_article:
        message = client1.sms.message.create(
            body = i,
            from_ = "+12282564571",
            to = "+919100761207",

        )
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

