# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "273601600-wyF84WnBs29PZCuLR72Jd9JCydGwpRCTlE3dECcU"
access_token_secret = "5gkkFlPFdtKbnHsVIxTfnbSwzoPa2bnIVbNg2Dr9yrpEF"
consumer_key = "LDHNJnUom7eodTDkw19kt34H3"
consumer_secret = "bnaVcIwvy1XE1ZnlFBrBiip7Gy1zR8wgtfNtvctt1nAEXdLdEW"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('UMSI')

results = 0
subjectivity = 0.0
polarity = 0.0

for tweet in public_tweets:
	results += 1
	print(tweet.text + "\n")
	analysis = TextBlob(tweet.text)
	subjectivity += analysis.subjectivity
	polarity += analysis.polarity

try:
	ave_subjectivity = subjectivity/results
	ave_polarity = polarity/results
	print("\nAverage subjectivity is: " + str(ave_subjectivity))
	print("Average polarity is: " + str(ave_polarity) + "\n")
except:
	print("It appears that there are no tweets with that term. Try searching for another term!")