import urllib.request, urllib.parse, urllib.error
import ssl
import twurl
import tweepy
import hidden
import json

# secrets = hidden.oauth()
# auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
# auth.set_access_token(secrets['token_key'], secrets['token_secret'])

# api = tweepy.API(auth)
# print(api.me().name)
# api.update_status(status='Updating using OAuth authentication via Tweepy!')
# info = api.user_timeline({'screen_name': 'merclanIT', 'count': '3'})
# print(info)





#
#
print(' * Calling twitter ')
url = twurl.augment('https://api.twitter.com/1.1/statuses/user_timeline.json', {'screen_name': 'merclanIT', 'count': '1'})
#
# print(url)
#
# # ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#
connection = urllib.request.urlopen(url, context=ctx)
# data = connection.read()
# print(data)
#
# headers = dict(connection.getheaders())
# print(headers)