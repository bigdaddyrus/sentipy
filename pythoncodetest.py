import twitter
import json
import simplejson
import re
import string
#from tweet_cleaner import tweet_cleaner

#helper functions
def tweet_cleaner(text):
    text1 = ''.join(text)
    #text1 = str(text)
    text1 = re.sub(r'^https?:\/\/.*[\r\n]*', '', text1, flags=re.MULTILINE);
    text1 = re.sub(r'^http?:\/\/.*[\r\n]*', '', text1, flags=re.MULTILINE);
    text1 = re.sub(r'^http:\/\/.*[\r\n]*', '', text1, flags=re.MULTILINE);
    text1 = re.sub(r'RT', '', text1, flags=re.MULTILINE);
    text1 = re.sub(r't.co', '', text1, flags=re.MULTILINE);
    text1 = re.sub(r'@', '', text1, flags=re.MULTILINE);
    text1 = re.sub(r"(?:\@|https?\://)\S+", "", text1)
    return text1;

#calculate the sentiment score for a sentence 
#according to input positive and negative words dictionary

def intersect(a, b):
     return list(set(a) & set(b))

def calscore_Liu(words, pos, neg):
	return len(intersect(words, pos)) - len(intersect(words, neg))

def calscore_Sent140(words, feature_scores_dict):
    keys = feature_scores_dict.key()
    have_keys = intersect(words, keys)
    score = 0
    for i in have_keys:
        score += feature_scores_dict[i]

    return score

#def calscore_SWN(words, pos, neg):


CONSUMER_KEY = 'tnBsdayluBFaHh5ueqz83AmWa'
CONSUMER_SECRET = 'cjRAodvZtUuIdfpyQqSRlCJGsrz8NUBgTEbxVCqpmyPIkg52OT'
OAUTH_TOKEN = '3222693991-NofnFAWUL4179vTYtQ5qwRHc6q4b3xSG6wrIGOw'
OAUTH_TOKEN_SECRET = 'WKn8YPpUV7FGKeRb93LMsClTjRHAfQmtYJbhgaoSPC8Lp'


#running the api
api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

n = 'Kanye West' 
j = 'Jay-Z'
e = 'Eminem'

c = 500

#get and print statuses

fopenpos = open("Liu-Opinion/negative_words.txt")
fopenneg = open("Liu-Opinion/positive_words.txt")

pos_words = fopenpos.read().splitlines()
neg_words = fopenneg.read().splitlines()

fopenpos.close();
fopenneg.close();

n_search_results = api.GetSearch(term=n, count=c, lang='en')
j_search_results = api.GetSearch(term=j, count=c, lang='en')
e_search_results = api.GetSearch(term=e, count=c, lang='en')

#Three different dictionaries
#Liu-Opinion
n_scores = map(lambda x: calscore_Liu(string.split(tweet_cleaner(x.text)), pos_words, neg_words), n_search_results)
j_scores = map(lambda x: calscore_Liu(string.split(tweet_cleaner(x.text)), pos_words, neg_words), j_search_results)
e_scores = map(lambda x: calscore_Liu(string.split(tweet_cleaner(x.text)), pos_words, neg_words), e_search_results)

#normalized_average to be add
n_avg = sum(n_scores) 
j_avg = sum(j_scores) 
e_avg = sum(e_scores)


#Sent140
fsent140 = open("sent140/unigrams-pmilexicon.txt")
dict1 = fsent140.read().splitlines()
dict2 = map(lambda x: string.split(x), dict1)
print[dict2]
dict140 = dict()
for i in dict2:
    dict140[i[0]] = i[1]

fsent140.close()

n_scores_2 = map(lambda x: calscore_Sent140(string.split(tweet_cleaner(x.text)), dict140), n_search_results)
j_scores_2 = map(lambda x: calscore_Sent140(string.split(tweet_cleaner(x.text)), dict140), j_search_results)
e_scores_2 = map(lambda x: calscore_Sent140(string.split(tweet_cleaner(x.text)), dict140), e_search_results)

n_avg_2 = sum(n_scores) 
j_avg_2 = sum(j_scores) 
e_avg_2 = sum(e_scores)

#SentiWordNet
fSWN = open("SentiWordNet/SentiWordNet_scores.csv")
dict1 = fSWN.read().splitlines()
dict2 = map(lambda x: string.split(x, sep=','), dict1)
dictSWN = dict()
for i in dict2:
    dictSWN[i[0]] = i[1]




#print [tweet_cleaner(s.text) for s in search_results]

#test
#sample0 = tweet_cleaner(search_results[0].text)
#sample1 = tweet_cleaner(search_results[1].text)

print ("Kanye West = %d" % n_avg)
print ("Jay-Z = %d" % j_avg)
print ("Eminem = %d" % e_avg)


print ("2 Kanye West = %d" % n_avg_2)
print ("2 Jay-Z = %d" % j_avg_2)
print ("2 Eminem = %d" % e_avg_2)

