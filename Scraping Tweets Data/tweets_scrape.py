#test data for data_science project.

from nltk.twitter import Twitter
tw = Twitter()
tw.tweets(to_screen=False, limit=5000, lang=["en"])
