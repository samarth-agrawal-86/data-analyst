import tweepy
from tweepy import OAuthHandler
import json
from timeit import default_timer as timer

# Query Twitter API for each tweet in the Twitter archive and save JSON in a text file
# These are hidden to comply with Twitter's API terms and conditions
consumer_key = 'YBUY2iKk7C1sRkfJ8T7pO2bOo'
consumer_secret = 'R3XIHSqfbPkDbNrUr7VbGoa2wYfwJr44FeVFNYvjVocgKvztRp '
access_token = '3199394082-3h1bxiItyKbwnXftqwMMl1pYSjvjQgBFG8INGop'
access_secret = 'KlbTLpKRS9uaET1tqS72SpaCLnjGQlzOdobjreugkyqIy'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.api(auth, wait_on_rate_limit = True)
