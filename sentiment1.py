import twitter
import json
import simplejson
import re
import image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from tweet_cleaner import tweet_cleaner


# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

CONSUMER_KEY = 'tnBsdayluBFaHh5ueqz83AmWa'
CONSUMER_SECRET = 'cjRAodvZtUuIdfpyQqSRlCJGsrz8NUBgTEbxVCqpmyPIkg52OT'
OAUTH_TOKEN = '3222693991-NofnFAWUL4179vTYtQ5qwRHc6q4b3xSG6wrIGOw'
OAUTH_TOKEN_SECRET = 'WKn8YPpUV7FGKeRb93LMsClTjRHAfQmtYJbhgaoSPC8Lp'


auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)


q = '$aapl' 

count = 500


search_results = twitter_api.search.tweets(q=q, count=count, lang='en')

statuses = search_results['statuses']


#get and print statuses
status_texts = [ status['text'] 
                 for status in statuses ]


status_texts1 = tweet_cleaner(status_texts)

wordcloud = WordCloud(font_path='Verdana.ttf').generate(status_texts1)

#wordcloud = WordCloud().generate(text)
# Open a plot of the generated image.
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


#print json.dumps(status_texts, indent=1)
print status_texts1



