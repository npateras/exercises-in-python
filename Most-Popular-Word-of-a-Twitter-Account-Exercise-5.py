import tweepy
import sys
import codecs
from string import punctuation
from operator import itemgetter
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'ZF9RAC4BQQ22dAIbGmM8yXNK5'
consumer_secret = 'JAsqitYfiyUGuNaej3swV48Cds8pas8F9Zirg0KQpGy5D253Yz'
access_token = '962849140597280768-g6hSONcF4loI55hofsVzVT9XDrkihAJ'
access_secret = 'MM6C3qLEQoJuDBuv7q7V20PPTzZqKAbh1maxNU4cG3sLk'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

user=raw_input('Enter twitter username: ')

f=codecs.open("tweets.txt","a+",encoding='utf8')
timeline = api.user_timeline(screen_name=user, include_rts=False, count=10)
tweet=0
for tweet in timeline:
    value=tweet.text
    with codecs.open("tweets.txt",'a',encoding='utf8') as f:
        f.write(value)
        f.write('\n')

N=1
words={}

words_gen=(word.strip(punctuation).lower() for line in open("tweets.txt")
for word in line.split())
for word in words_gen:
    words[word]=words.get(word, 0)+1
top_words=sorted(words.iteritems(), key=itemgetter(1), reverse=True)[:N]
for word, frequency in top_words:
    print "I pio xrisimopoimeni le3i einai:\n[%s] kai xrisomopoithike %d fores" % (word, frequency)
with open('tweets.txt','w'): pass
f.close()
