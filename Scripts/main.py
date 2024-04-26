import pandas as pd
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("apikey")
print(api_key)

url = "https://newsapi.org/v2/everything"

params = {
    "apiKey":api_key,
    "q":"micron",
    "SearchIn":"title"
}

response = requests.get(url, params)
print(response.json())

