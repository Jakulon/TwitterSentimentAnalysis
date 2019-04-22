import tweepy
from textblob import TextBlob
import csv


# AUTHENTICATION DETAILS IN PLAIN TEXT :-/
# remote them before upload to github !!!!!!!!!!!!
consumer_key = '***'
consumer_secret = '***'

access_token = '***'
access_token_secret = '***'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
searchtext = 'Sri Lanka'
public_tweets = api.search(searchtext)

with open('twitterSentimentAnalysis.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['label','tweet','sentiment'])
    for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
        print('\n')
        if analysis.sentiment.polarity <= 0:
            polarity = "Negative"
        else:
            polarity = "Positive"
        csvwriter.writerow([searchtext, tweet.text, polarity])
    

