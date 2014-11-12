## $ python happiest_state.py AFINN-111.txt output.txt
## takes the sentiment file and tweeter file as input
## output the happiest state name

import sys
import json
import pdb

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def format_title_unicode_translate(title):
    return title.translate(title_unicode_trans)

class TitleUnicodeTranslate(dict):
    def __missing__(self,item):
        uni = unichr(item)
        res = u''
        if uni.isupper() or uni.islower():
            res = uni
        self[item] = res
        return res
title_unicode_trans=TitleUnicodeTranslate()


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    for line in sent_file:
    	term, score = line.split("\t")
    	scores[term] = int(score)
    sent_score = []
    for line in tweet_file:
    	tweet = json.loads(line)
    	if 'text' in tweet:
    		one_tweet = tweet['text'].split()
    		score_tweet = 0
    		for part in one_tweet:
    			word = format_title_unicode_translate(part) # stripped alphabetic word
    			word = word.lower()
    			if word in scores:
    				score_tweet = score_tweet + scores[word]
    		sent_score.append(score_tweet)
    	else:
    		sent_score.append(0)    
    
    happiness = {}
    i = 0
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        tweet = json.loads(line)
        if 'user' in tweet:
            if 'location' in tweet['user']:
                one_tweet = tweet['user']['location'].split()
                for part in one_tweet:
                    word = format_title_unicode_translate(part)
                    word = word.lower().capitalize()
                    if word in states.values():
                        if word not in happiness:
                            happiness[word] = sent_score[i]
                        else:
                            happiness[word] = sent_score[i] + happiness[word]
        i = i+1
    inverse = [(value, key) for key, value in happiness.items()]
    happy = max(inverse)[1]                       
    code = [k for k, v in states.iteritems() if v == happy] 
    print code[0]               
                    
if __name__ == '__main__':
    main()

