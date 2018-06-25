#q3 Using Tweepy library try to extract tweets from Twitter.

#method 1  by having user input for tweet search..

import tweepy

consumer_key_20="************"           #identification of user
consumer_secret_20="************"        #secret key or password


access_token_20="***********"             #accesstoken
access_secret_20="************"           #secret key


auth=tweepy.OAuthHandler(consumer_key_20,consumer_secret_20)      #authentication
auth.set_access_token=(access_token_20,access_secret_20)           #authorization
api=tweepy.API(auth)                                               #api is generated
n=input("enter the word without hashtags you want to search for...? ")   #user input search
n = "#" + n
num=int(input("enter the count or number of tweets you want to see.."))   #user input number of tweets
tweets=api.search(n,count=num,lang="en",tweet_mode="extended")   #whatever tweets we want to search with hashtags



# print(tweets)    #using this print statement JSON format appears

for tweet in tweets:
	print("..........")
	print(tweet.full_text)           #full user understandable lang.
	print("..........")
	

#method 2 by predefined search for hashtag tweets and count.

import tweepy

consumer_key_20="************"           #identification of user
consumer_secret_20="************"        #secret key or password


access_token_20="***********"             #accesstoken
access_secret_20="************"           #secret key


auth=tweepy.OAuthHandler(consumer_key_20,consumer_secret_20)      #authentication
auth.set_access_token=(access_token_20,access_secret_20)           #authorization
api=tweepy.API(auth)                                               #api is generated

tweets=api.search("#kanha",count=5,lang="en",tweet_mode="extended")   #whatever tweets we want to search with hashtags



# print(tweets)    #using this print statement JSON format appears

for tweet in tweets:
	print("..........")
	print(tweet.full_text)           #full user understandable lang.
	print("..........")