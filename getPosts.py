from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import praw

user_agent = "Reddit Scrapper v1.0 by /u/deadshot994"
reddit = praw.Reddit (
    client_id = "IS7_9VkuTl56DSAfh8c7mg",
    client_secret = "lTb_RwNuwR1-UooiPRPgS7YRWDXYSA",
    user_agent = user_agent
)
# Hot 
# New Rising Topics
subreddit = input("Enter subreddit: ")
for submission in reddit.subreddit(subreddit).hot(limit = 3):
    print("Title: ", submission.title)
    print("Post Id: ", submission.id)
    print("Submitted by: u/", submission.author)
    print("Created at: ", submission.created_utc)
    print("Submission score: ", submission.score)
    print("Upvote ratio: ", submission.upvote_ratio)
    print("URL: ", submission.url)
    print("\n")
    
    