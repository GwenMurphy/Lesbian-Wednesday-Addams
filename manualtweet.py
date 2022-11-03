import tweepy
from credentials import *


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
tweet = input(" ")
api.update_status(status =(tweet))
print ("Done!")