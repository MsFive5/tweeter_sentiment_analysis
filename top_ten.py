## $ python top_ten.txt output.txt
## returns the top ten most frequently occuring hashtags given tweeter file
import sys
import json
from collections import OrderedDict
from operator import itemgetter

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
    tweet_file = open(sys.argv[1])
    hashtags_all = {}
    num_hash = 0
    for line in tweet_file:
        tweet = json.loads(line)
        if 'entities' in tweet:
            a = tweet['entities']['hashtags']
            if a != []:
                b = a[0]['text']
                c = format_title_unicode_translate(b)
                hashtag = c.lower()
                if len(hashtag) > 0:
                    num_hash = num_hash + 1
                    if hashtag not in hashtags_all:
                        hashtags_all[hashtag] = 1
                    else: 
                        hashtags_all[hashtag] = hashtags_all[hashtag]+1
    #values = sorted(hashtags_all.values())[::-1]      
    #for i in range(10):
    a = 1
    d = sorted(hashtags_all, key=hashtags_all.get, reverse=True)                       
    for ha in d:
        if a < 11:
            sys.stdout.write(ha)
            sys.stdout.write(' ')
            sys.stdout.write(str(hashtags_all[ha]))
            sys.stdout.write('\n')
            a += 1
        

if __name__ == '__main__':
	main()
	
