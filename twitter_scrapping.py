from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token='3073532904-oca3FiOssY05jNZ47DHuFuS3bgJjFr4xE8lzxLb'
access_token_secret='UT85tRm0RFokMVOg7PDTvJtpi69P4uteF0r8kaGx79Q3e'
consumer_key='9Ny91WK39HJHHdf1XWmLExRjM'
consumer_secret='ZDfpbUcV2QLfvOBtrfGURpAyNZTJwvshhpLcOAgfhnk8k'

class StdOutListener(StreamListener):
    def on_data(self,data):
        print (data)
        return True

    def on_error(self,status):
        print (status)

if __name__== '__main__':
    # this handles Twitter authentication and the connection to Twittter streaming x8OLuaPeN3UgkH5JIrggWB7kPkP6QVYXBPR4pLda7IdkANAN5N
    a=StdOutListener()
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream=Stream(auth,a)

    # This line filter twitter streams to capture data by the keywords :'microfinance'
    stream.filter(track=['microfinance'])
