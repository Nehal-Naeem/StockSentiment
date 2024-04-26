import requests

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("apikey")
print(api_key)


## append articles cieling of (totalResults/100)
# def getDescriptions()

url = "https://newsapi.org/v2/everything"

params = {
    "apiKey":api_key,
    "q":"micron",
    "SearchIn":"title",
    "page": "1"
}

response = requests.get(url, params)
articles = response.json().get("articles")
counter = 1
for a in articles:
    print("article number: "+ str(counter))
    print(a.get("title"))
    counter += 1