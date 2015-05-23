import twitter
import simplejson
import re

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

CONSUMER_KEY = 'tnBsdayluBFaHh5ueqz83AmWa'
CONSUMER_SECRET = 'cjRAodvZtUuIdfpyQqSRlCJGsrz8NUBgTEbxVCqpmyPIkg52OT'
OAUTH_TOKEN = '3222693991-NofnFAWUL4179vTYtQ5qwRHc6q4b3xSG6wrIGOw'
OAUTH_TOKEN_SECRET = 'WKn8YPpUV7FGKeRb93LMsClTjRHAfQmtYJbhgaoSPC8Lp'

auth = twitter.SetCredentials(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

