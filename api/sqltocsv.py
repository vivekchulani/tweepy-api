import dataset
import datetime

# Connect to db and write tweets stored in table to csv
tweetsDatabase = dataset.connect("sqlite:///Tweets.db")
tweets = tweetsDatabase.query("SELECT * FROM tweets WHERE DATECREATED > DATE(CURRENT_DATE, '-1 DAY')")
with open(str(datetime.date.today()) + "_DVA_tweets.csv", "w+") as tweetsFile:
    tweetsFile.write("id||tweetId||user||tweet||timestamp||polarity||subjectivity\n")
    for tweet in tweets:
        tweetsFile.write(str(tweet["id"])+"||"+tweet["tweetId"]+"||"+tweet["user"]+"||"+tweet["tweet"]+"||"+str(tweet["timestamp"])+"||"+str(tweet["polarity"])+"||"+str(tweet["subjectivity"])+"\n")
