import praw
import time
import random
from random import randrange

import credentials

user_agent = credentials.user_agent
client_id = credentials.client_id
client_secret = credentials.client_secret
username = credentials.username
password = credentials.password

# CONSUMER_KEY = environ['CONSUMER_KEY']
# CONSUMER_SECRET = environ['CONSUMER_SECRET']
# ACCESS_KEY = environ['ACCESS_KEY']
# ACCESS_SECRET = environ['ACCESS_SECRET']
# FORECAST_APIKEY = environ['FORECAST_APIKEY']

reddit = praw.Reddit(
user_agent = user_agent,
client_id = client_id,
client_secret = client_secret,
username = username,
password = password

)  # must be edited to properly authenticate


botphrases = ["Upvoted", "Upvote"]

counter = 0
seen_submissions = set()
while True:
	subreddit = reddit.subreddit('FreeKarma4U')
	if counter%4 == 0:
		time.sleep(randrange(90,210))
		seen_submissions = set()
	for submission in subreddit.new(limit=5):
		if submission.fullname not in seen_submissions:
			seen_submissions.add(submission.fullname)
			time.sleep(randrange(31,101))
			print('{} {}\n'.format(submission.title, submission.url))
			submission.reply(botphrases[randrange(0,1)])
			counter +=1
	subreddit = reddit.subreddit('FreeKarma4You')
	for submission in subreddit.new(limit=5):
		if submission.fullname not in seen_submissions:
			seen_submissions.add(submission.fullname)
			time.sleep(randrange(31,101))
			print('{} {}\n'.format(submission.title, submission.url))
			submission.reply(botphrases[randrange(0,1)])
			counter +=1