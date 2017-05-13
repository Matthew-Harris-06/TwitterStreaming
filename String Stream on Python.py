import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
# Creates the myStreamListener class and Overrides the OnStatus method & OnError method
class myStreamListener(tweepy.StreamListener):	

	def on_status(self, status):
		print(status.text)
	def on_error(self, status_code):
		if status_code == 420:
			return False

myStreamListener = myStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['Insert String Here'], async=True)









    
