
# coding: utf-8

# ## Collecting the Data

# In[4]:

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


# In[5]:

consumer_key = 'wPeEyDrjfMdyQzN763Iyyl02d'
consumer_secret = '481up7mpWX5zy9IusZoe2e4BZ6GywQCA37Q8Q8rn5hMF6WF5mQ'
access_token = '3259586191-vEjD3fCWvWC7p0wg1eWBcrWxGJgsomclwYkeTsY'
access_secret = 'jVU2TyipiAbvpuxF0FGXSYfGDDA09Gq1ghk9onn4aAvIl'


# In[6]:

class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


# In[9]:

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python'])

