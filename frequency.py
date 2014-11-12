import sys
import json
import pdb
import re

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

file = open('outputtest.txt','w')
def main():
    tweet_file = open(sys.argv[1])
    total_word_count = 0
    word_count = {}
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in tweet:
            one_tweet = re.split(' ',tweet['text'])
            for part in one_tweet:
                word = format_title_unicode_translate(part) # stripped alphabetic word
                word = word.lower()
                if word != '':
                    total_word_count = total_word_count + 1
                    if word not in word_count:
                        word_count[word] = 1;
                    else:
                        word_count[word] = word_count[word] + 1
    for word in word_count:
        print word," ",str(word_count[word]/float(total_word_count))

if __name__ == '__main__':
    main()
