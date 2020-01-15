import tweepy as tw
import random
from pushbullet import Pushbullet

consumer_key= 'your twitter consumer key'
consumer_secret= 'your twitter consumer secret'
access_token= 'your twitter access token'
access_token_secret= 'your twitter access token secret'
pb = Pushbullet('your pushbullet access token')

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

def twitter(search_words="#eko_kendimenotlar",date_since="2018-01-01"):
    
    tweets = tw.Cursor(api.user_timeline,
              id= 12345678, #Your twitter user_id
              since=date_since,
              tweet_mode='extended').items()
    
    content = []
    for i in tweets:
        content.append(i.full_text)
    
    tweets2=[]
    for i in content:
        if i.find(search_words) != -1:
            tweets2.append(i)  
    
    push = pb.push_note("Twitter Ekonomi Notları ",tweets2[random.choice(range(0,len(tweets2)))])
    return push['body']

twitter()
