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

    response = requests.get(url,params)
    print("totalResults: "+ str(response.json().get("totalResults")))
    return(response.json().get("articles"))


getArticles("micron")