from textblob import TextBlob

import tweepy
import time
import datetime
import dataset

# Tweepy Streaming API to fetch real time tweets

# Create StreamListener which extends Tweepy StreamListener
class StreamListener(tweepy.StreamListener):

    # Load database connection and table
    tweetsDatabase = dataset.connect("sqlite:///Tweets.db")
    table = tweetsDatabase["tweets"]

    def on_status(self, status):
        # Exclude retweets
        if (status.retweeted):
            return
        # Set content based on tweet character length
        try:
            content = status.extended_tweet['full_text'].replace("\n", " ")
        except:
            content = status.text.replace("\n", " ")
        # Extract sentiment using Textblob and write info to db
        blob = TextBlob(content)

        # Insert Records
        StreamListener.table.insert(dict(
            tweetId = status.id_str,
            user = status.user.screen_name,
            tweet = content,
            timestamp = status.created_at,
            polarity = blob.sentiment.polarity,
            subjectivity = blob.sentiment.subjectivity,
            datecreated = datetime.date.today()
        ))

    def on_error(self, status_code):
        if (status_code == 401):
            print("unauthorized access, Check credentials")
            return False
