import sys
import json
import pdb
def hw():
    print 'Hello, world!'

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

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #print lines(sent_file)
    #print lines(tweet_file)
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
    		print score_tweet
    	else:
    		sent_score.append(0)    
    		print 0
    
if __name__ == '__main__':
	main()
	
	
	


	