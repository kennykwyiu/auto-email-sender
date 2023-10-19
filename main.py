import time
import datetime


import requests
import send_email

search_keyword1 = "bankrupt"
search_keyword2 = "AI"


page_size = 30
now_date = datetime.datetime.now()  # 現在的日期和時間
days_aga = now_date - datetime.timedelta(25) # 計算20天前的日期
right_date = days_aga.strftime('%Y-%m-%d')  # 以指定的格式輸出日期

api_key = "Your API KEY"
url = f"https://newsapi.org/v2/everything?" \
      f"q={search_keyword1}&" \
      f"from={right_date}&" \
      f"sortBy=publishedAt&" \
      f"apiKey={api_key}&" \
      f"language=en&" \
      f"pageSize={page_size}"

# Make request
request1 = requests.get(url)

# Get a dictionary with data
content1 = request1.json()

# Access the article titles and description
body = f"Subject: Today's news about {search_keyword1}" + "\n"
for article in content1['articles']:
    if article['title'] is not None:
        body = body + article['title'] + "\n" + article['publishedAt'] + "\n" \
               + article['url'] + "\n" + article['description'] + 2*"\n"

body = body.encode("utf-8")
send_email.send_email(body)
print(f"{search_keyword1} - message was sent")

#######################################################################

url = f"https://newsapi.org/v2/everything?" \
      f"q={search_keyword2}&" \
      f"from={right_date}&" \
      f"sortBy=publishedAt&" \
      f"apiKey={api_key}&" \
      f"language=en&" \
      f"pageSize={page_size}"

# Make request
request2 = requests.get(url)

# Get a dictionary with data
content2 = request2.json()

# Access the article titles and description
body = f"Subject: Today's news about {search_keyword2}" + "\n"
for article in content2['articles']:
    if article['title'] is not None:
        body = body + article['title'] + "\n" + article['publishedAt'] + "\n" \
               + article['url'] + "\n" + article['description'] + 2*"\n"

body = body.encode("utf-8")
send_email.send_email(body)
print(f"{search_keyword2} - message was sent")




