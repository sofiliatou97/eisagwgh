import tweepy
import re

# Keys, tokens and secrets
consumer_key = "BZ6tas2dZz4RhANtpQZT8569t"
consumer_secret = "qZ1eBQgpSBXByXyipKZHCXPzNc3PnTn7jCMgOOR9Dve6ABTkVe"
access_token = "1094595501788418050-kmq2pcJ64nyKjtynVVQCm3yEH2J6Mz"
access_token_secret = "h8lpa8allCQpqPYnrPHtzZj5QBgdBjNTkyV2u7uvr9ryQ"
totalTweets = 10

username1 = ""
username2 = ""
try: 
	while username1=="" or username2=="":
		username1 = raw_input("Username1: ")
		username2 = raw_input("Username2: ")
except:
	print "Error"
	quit()


# Tweepy OAuthHandler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

targets = [username1,username2] 

followers = []
totalWords = []

for target in targets:
	sum = 0 
	user = api.get_user(target)
	info = api.user_timeline(screen_name = target, count=totalTweets)
	for information in info:
		sum = sum + len(re.findall("[a-zA-Z_]+", information.text))
	totalWords.append(sum)
	print(user.name, user.followers_count)
	followers.append(user.followers_count)

user1Score = followers[0]*totalWords[0]
user2Score = followers[1]*totalWords[1]
  

if user1Score > user2Score:
	print "User 1 wins: " + username1 + ': ' + str(user1Score)
elif user1Score < user2Score:
	print "User 2 wins: " + username2 + ': ' + str(user2Score)
else: 
	print "Noone wins" 
	print username1 + ': ' + str(user1Score)
	print username2 + ': ' + str(user2Score)
