import twitter
import json
import simplejson
import re
from score_functions import cal_scores
from normalized_average import normalized_average

CONSUMER_KEY = 'tnBsdayluBFaHh5ueqz83AmWa'
CONSUMER_SECRET = 'cjRAodvZtUuIdfpyQqSRlCJGsrz8NUBgTEbxVCqpmyPIkg52OT'
OAUTH_TOKEN = '3222693991-NofnFAWUL4179vTYtQ5qwRHc6q4b3xSG6wrIGOw'
OAUTH_TOKEN_SECRET = 'WKn8YPpUV7FGKeRb93LMsClTjRHAfQmtYJbhgaoSPC8Lp'


#running the api
api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

n = '#KanyeWest' 
j = '#Jay-Z'
e = '#Eminem'

c = 500

#get and print statuses

n_search_results = api.GetSearch(term=n, count=c, lang='en')
j_search_results = api.GetSearch(term=j, count=c, lang='en')
e_search_results = api.GetSearch(term=e, count=c, lang='en')

#Three different dictionaries
#Liu-Opinion

# calculate scores from tweets
n_scores = map(lambda x: cal_scores(x, "Liu-Opinion"), n_search_results)
j_scores = map(lambda x: cal_scores(x, "Liu-Opinion"), j_search_results)
e_scores = map(lambda x: cal_scores(x, "Liu-Opinion"), e_search_results)

#normalized_average to be add

print ("Set 1")
n_avg = normalized_average([i[2] for i in n_scores])
j_avg = normalized_average([i[2] for i in j_scores])
e_avg = normalized_average([i[2] for i in e_scores])

#Sent140

n_scores_2 = map(lambda x: cal_scores(x, "sent140"), n_search_results)
j_scores_2 = map(lambda x: cal_scores(x, "sent140"), j_search_results)
e_scores_2 = map(lambda x: cal_scores(x, "sent140"), e_search_results)

print ("Set 2")
n_avg_2 = normalized_average([i[2] for i in n_scores_2]) 
j_avg_2 = normalized_average([i[2] for i in j_scores_2]) 
e_avg_2 = normalized_average([i[2] for i in e_scores_2])

#SentiWordNet

n_scores_3 = map(lambda x: cal_scores(x, "SentiWordNet"), n_search_results)
j_scores_3 = map(lambda x: cal_scores(x, "SentiWordNet"), j_search_results)
e_scores_3 = map(lambda x: cal_scores(x, "SentiWordNet"), e_search_results)

print ("Set 3")
n_avg_3 = normalized_average([i[2] for i in n_scores_3])
j_avg_3 = normalized_average([i[2] for i in j_scores_3])
e_avg_3 = normalized_average([i[2] for i in e_scores_3])
rch_results[1].text)

print ("--------------------")

