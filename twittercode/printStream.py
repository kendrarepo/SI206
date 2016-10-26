import tweepy
import json

# Unique code from Twitter
access_token = "273601600-wyF84WnBs29PZCuLR72Jd9JCydGwpRCTlE3dECcU"
access_token_secret = "5gkkFlPFdtKbnHsVIxTfnbSwzoPa2bnIVbNg2Dr9yrpEF"
consumer_key = "LDHNJnUom7eodTDkw19kt34H3"
consumer_secret = "bnaVcIwvy1XE1ZnlFBrBiip7Gy1zR8wgtfNtvctt1nAEXdLdEW"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
def process_or_store(tweet):
	print(tweet.get('user').get('screen_name'))
	print(tweet.get('text').encode('unicode_escape'))
	print(tweet.get('created_at'))

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json) 


for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)


