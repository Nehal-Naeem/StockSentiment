import requests

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("key")
# print(api_key)

def getSourceIDs(category):
    sources_url = "https://newsapi.org/v2/top-headlines/sources"
    sources_params = {
        "apiKey":api_key,
        "category":category,    
        "language": "en"
    }
    
    response = requests.get(sources_url, sources_params)
    
    sources = []
    for s in response.json().get("sources"):
        sources.append(s.get("id"))
    
    return sources

def parseSourcesArray(arr):
    out = str(arr).replace("'","")
    out = out[1:len(out)-1]
    return out


business = getSourceIDs("business")
technology = getSourceIDs("technology") 
sources = business + technology

sourceIDs = parseSourcesArray(sources)

## append articles cieling of (totalResults/100)
## return article title, descriptions, content,url and publishedAt
def getArticles(company):
    url = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": api_key,
        "q": company,
        "searchin": "title,description",
        "sources" : sourceIDs,
        "language":"en",
        "sort":"publishedAt"
    }
    
    
    articles = []
    page = 1

    while True:
        print("fetching page: " + str(page))
        params["page"] = str(page)
        response = requests.get(url,params)
        totalResults = response.json().get("totalResults")
        pageArticles = response.json().get("articles")
        # if len of page articles = 100 request again
        print("totalResults: "+ str(totalResults))
        print("Articles on page: "+ str(len(pageArticles)))
        
        for article in response.json().get("articles"):
            articles.append(article)
            
        
        if len(pageArticles) < 100:
            break

        page = page + 1
    
    return articles