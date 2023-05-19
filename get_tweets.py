#import wordcloud
#import textblob import Textblob
#import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import spacy
# from spacy import displacy
import re
import os
#import seaborn as sns
import tweepy

api_key = "qZvjrJELbPt0QcyXpoLzTrP64"
api_secret = "Fjilw3PEMNqRLtyNB0CAfDnfWBMaXCAPGLCtWnm59Ar9JBU5wj"
access_token = "1423921567948427268-ZQIsssBCi7UffFPuJls0Tz1oER6zsg"
access_secret = "bvZtxJzixY2BOTIq1eJxxnOZLAPChlwI9K5XBSK7hUKh9"

# Build an api object to fetch tweets from twitter
auth = tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
q = input("Enter Keyword: ")
tweets = api.search_tweets(q,count = 10)

for tw in tweets:
    print(tw.text)
    print()