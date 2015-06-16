import twitter
import json
import re
import string
from tweet_cleaner import tweet_cleaner
from score_functions import *
import time

CONSUMER_KEY = 'tnBsdayluBFaHh5ueqz83AmWa'
CONSUMER_SECRET = 'cjRAodvZtUuIdfpyQqSRlCJGsrz8NUBgTEbxVCqpmyPIkg52OT'
OAUTH_TOKEN = '3222693991-NofnFAWUL4179vTYtQ5qwRHc6q4b3xSG6wrIGOw'
OAUTH_TOKEN_SECRET = 'WKn8YPpUV7FGKeRb93LMsClTjRHAfQmtYJbhgaoSPC8Lp'


#running the api
api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

n = 'goog' 

c = 50

#get statuses
n_search_results = api.GetSearch(term=n, count=c, lang='en')

# print n_search_results
tb = time.time()

def tweet_clean(tweet):
    word_with_case = tweet_cleaner(tweet.text)
    #change it to case insensitive 
    word = word_with_case.lower()
    return word

def contains(x, words):
    # print "key:%n"
    # print x
    # print "tweet: %n"
    # print words
    try:
        if x in words:
            return x
    except UnicodeDecodeError:
        pass
#for a single tweet
def sent140_bigram_have_keys(keys, tweet):
    have_keys = map(lambda x: contains(x, tweet), keys)
    # print have_keys
    return [x for x in have_keys if x is not None]

def flatmap(f, seq):
    return sum([f(s) for s in seq], [])

list_of_tweets = map(lambda x : tweet_clean(x), n_search_results)


fsent = open("sent140/bigrams-pmilexicon.txt")
dict1 = fsent.read().splitlines()
dict2 = map(lambda x: string.split(x, sep='\t'), dict1)
dict_sent = dict()
for i in dict2:
    dict_sent[i[0]] = i[1]

fsent.close()


keys = dict_sent.keys()
print keys
# Get all the keys
have_keys = flatmap(lambda x: sent140_bigram_have_keys(keys, x), list_of_tweets)

#print have_keys

scores = [float(dict_sent[i]) for i in have_keys]
pos_score = sum_pos(scores)
neg_score = sum_neg(scores)
diff = pos_score + neg_score
hit = len(have_keys)


print [pos_score, neg_score, diff, hit]


print ("--------------------")

tt = time.time() - tb
print ("Total time elapsed = %.5f" % tt)


