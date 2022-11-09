##### Importing all the things.
import tweepy
import time
from credentials import *
from tweetlist import *     ## So the arrays in tweetlist.py can be used.


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
tweet = input(" ")
api.update_status(status =(tweet))
print ("Done!")

## Can the f' ' thing be used in an input thing?
# Apparently not.