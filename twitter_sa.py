import tweepy
import re
import sys
from textblob import TextBlob
from collections import OrderedDict

def clean_tweet(tweet):
    '''
    Utility function to clean the text in a tweet by removing 
    links and special characters using regex.
    Credits to Rodlfo Ferro https://dev.to/rodolfoferro/sentiment-analysis-on-trumpss-tweets-using-python-
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


# Consumer keys and access tokens, used for OAuth
# Replace with valid keys and access tokens
consumer_key = 'XXXXXXXXXX'
consumer_secret = 'XXXXXXX'
access_token = 'XXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXX'

# OAuth Process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#
api = tweepy.API(auth)
keyword = raw_input("Search for:")
search_results = api.search(q=keyword, count=100)

posresults, negresults = 0, 0
postweets, negtweets = [], []
for tweet in search_results:
    text = clean_tweet(tweet.text)
    stext = TextBlob(text)
    if stext.sentiment.polarity > 0:
        posresults += 1
        postweets.append(text)
    else:
        negresults += 1
        negtweets.append(text)
    
print ('{0} positive tweets'.format(posresults))
print ('{0} negative tweets'.format(negresults))

print ('\nPositive tweets:')
for tweets in list(OrderedDict.fromkeys(postweets)):
    print (tweets)
print ('\nNegative tweets:')
for tweets in list(OrderedDict.fromkeys(negtweets)):
    print (tweets)

