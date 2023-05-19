import tweepy

api_key = "qZvjrJELbPt0QcyXpoLzTrP64"
api_secret = "Fjilw3PEMNqRLtyNB0CAfDnfWBMaXCAPGLCtWnm59Ar9JBU5wj"
access_token = "1423921567948427268-ZQIsssBCi7UffFPuJls0Tz1oER6zsg"
access_secret = "bvZtxJzixY2BOTIq1eJxxnOZLAPChlwI9K5XBSK7hUKh9"

# Build an api object to fetch tweets from twitter
auth = tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# Get the User object that represents the user, @Twitter
username = input("Enter Name of account: ")
# user = input("Enter User Name: ")
user = api.get_user(screen_name = username)
print("User Name: ", user.screen_name)
print("Description: ", user.description)
print("Number of Followers: ", user.followers_count)
print("Following count: ", user.friends_count)
print("Following: ")
for friend in user.friends():
   print(friend.screen_name)
# blocked_ids = api.get_blocked_ids(username)
# print(blocked_ids)