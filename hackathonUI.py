import tweepy
import configparser
import streamlit as st
from datetime import datetime
import pytz
import instaloader
import praw
from streamlit_option_menu import option_menu

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

# Twitter API keys
api_key = 'qZvjrJELbPt0QcyXpoLzTrP64'
api_key_secret = 'Fjilw3PEMNqRLtyNB0CAfDnfWBMaXCAPGLCtWnm59Ar9JBU5wj'

# Twitter access tokens
access_token = '1423921567948427268-ZQIsssBCi7UffFPuJls0Tz1oER6zsg'
access_token_secret = 'bvZtxJzixY2BOTIq1eJxxnOZLAPChlwI9K5XBSK7hUKh9'

# Instagram instance
loader = instaloader.Instaloader()

# Reddit instance
user_agent = "Reddit Scrapper v1.0 by /u/deadshot994"
reddit = praw.Reddit(
    client_id="IS7_9VkuTl56DSAfh8c7mg",
    client_secret="lTb_RwNuwR1-UooiPRPgS7YRWDXYSA",
    user_agent=user_agent
)

# Function to convert UTC to IST
def convert_utc_to_local(utc_dt):
    local_tz = pytz.timezone('Asia/Kolkata')  # Indian Time Zone (Asia/Kolkata)
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_dt

# Function to search tweets
def search_tweets(keyword, count):
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    tweets = api.search_tweets(q=keyword, count=count, tweet_mode='extended')

    for tweet in tweets:
        created_at = tweet.created_at
        local_time = convert_utc_to_local(created_at)
        local_time_str = local_time.strftime("%Y-%m-%d %H:%M:%S")
        st.write(f"Time: {local_time_str}")
        st.write(f"User: {tweet.user.screen_name}")
        st.write(f"Tweet: {tweet.full_text}")
        st.write(f"Link: https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
        st.write("---")

# Function to search twitter user
def search_user(username):
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    user = api.get_user(screen_name=username)

    st.write("User Name: ", user.screen_name)
    st.write("Description: ", user.description)
    st.write("Number of Followers: ", user.followers_count)
    st.write("Following count: ", user.friends_count)
    st.write("Following: ")
    for friend in user.friends():
        st.write(friend.screen_name)
    st.write("---")

# Function to scrape Instagram hashtags
def scrape_hashtags(hashtag, count):
    posts = instaloader.Profile.from_username(loader.context, hashtag).get_posts()
    post_count = 0

    for post in posts:
        if post_count >= count:
            break

        post_count += 1
        st.write(f"Caption: {post.caption}")
        st.write(f"Likes: {post.likes}")
        st.write(f"Link: https://www.instagram.com/p/{post.shortcode}")
        st.write("---")

# Function to search subreddit
def search_reddit(subreddit, limit):
    for submission in reddit.subreddit(subreddit).hot(limit=limit):
        st.write("Title: ", submission.title)
        st.write("Post Id: ", submission.id)
        st.write("Submitted by: u/", submission.author)
        st.write("Created at: ", submission.created_utc)
        st.write("Submission score: ", submission.score)
        st.write("Upvote ratio: ", submission.upvote_ratio)
        st.write("URL: ", submission.url)
        st.write("\n")

# Streamlit app
st.set_page_config(page_title="HackElevate", page_icon=":satellite_antenna:", layout="centered")

# Navigation bar
with st.sidebar:
    navigation=option_menu(
        menu_title="Home",
        options=["Welcome","Twitter","Instagram","Reddit","Contact"],
        icons=["house","twitter","instagram","reddit","envelope"],  # Using Bootstrap icons
        menu_icon="cast",
    )
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)   
local_css("style/style.css")   

if navigation == "Welcome":
    st.title("Welcome to HackElevate")
    st.subheader("Social Media Monitoring Tool")
    st.write("Choose an option from the sidebar to get started!")
elif navigation == "Twitter":
    st.title("Twitter Search")
    twitter_option = st.radio("", ("Search Tweets", "Search User"), index=0, key="twitter_search_option")
    if twitter_option == "Search Tweets":
        keyword = st.text_input("Enter the keyword to search for tweets")
        count = st.number_input("Enter the number of tweets to retrieve", min_value=1, max_value=100, step=1, value=10)
        if st.button("Search"):
            search_tweets(keyword, count)
    elif twitter_option == "Search User":
        username = st.text_input("Enter the username to search for")
        if st.button("Search"):
            search_user(username)
elif navigation == "Instagram":
    st.title("Instagram Hashtag Scraper")
    hashtag = st.text_input("Enter the hashtag to search for posts")
    count = st.number_input("Enter the number of posts to retrieve", min_value=1, max_value=100, step=1, value=10)
    if st.button("Search"):
        scrape_hashtags(hashtag, count)
elif navigation == "Reddit":
    st.title("Reddit Search")
    subreddit = st.text_input("Enter the subreddit to search for posts")
    limit = st.number_input("Enter the number of posts to retrieve", min_value=1, max_value=100, step=1, value=10)
    if st.button("Search"):
        search_reddit(subreddit, limit)
elif navigation == "Contact":
        with st.container():
            st.write("---")
            st.header("Get in touch with the developers")
            st.write("##")

            # Documentation: https://formsubmit.co/ 
            contact_form = """
            <form action="https://formsubmit.co/sanjeethmanikandan@gmail.com" method="POST">
            <input type = "hidden" name = "_captcha" value = "false">
            <input type="text" name="name" placeholder = "Your name" required>
            <input type="email" name="email" placeholder = "Your Email" required>
            <textarea name = "message" placeholder = "Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>

        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
