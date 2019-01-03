import argparse
import tweepy
from textblob import TextBlob

consumer_key='zJeCP3Do1XquqZzrWxu8yeIXW'
consumer_secret='Mh3woGs7L0PD5wZKS9VREUYtiAj5uflMBW6yfDoZ33089Hqhog'

access_token='214783983-mUqYd2SEj6wNuLVbTAWAVl9VruyG4cZ7v910ulMB'
access_token_secret='r8K1Zop4IkmmZwslz2K5qT3GjhgOJkqAkxhlr3hWkNIzU'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# Get Command line  ArguementsTwe
# define parseer
parser = argparse.ArgumentParser(description='Twitter Keyword  to search')

# declare arugment to store the value.
#parser.add_argument('--TweetKeyword', action = "store" , dest= 'TweetKeyword', default ='dow')
parser.add_argument('TweetKeyword')
args = parser.parse_args()
print(args.TweetKeyword)



myTweetapi = tweepy.API(auth)

public_tweets = myTweetapi.search(args.TweetKeyword)

for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print (analysis.sentiment)

    