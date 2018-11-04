import tweepy as tp
import time
import os

# credentials for twitter api
consumer_key = "rAHnaI81Ayqa9G4HeWj2wecBQ"
consumer_secret = "RFIC7nh3B3t1zGxNZxFL2ZOgzorNUheRkWSN4BE30i4B8iOfYO"
access_token = "929173793674706944-r6yTTUKnC3mAIOEezkrs3mUo9SvnS0S"
access_secret = "NeWnq2akCaxNVIT0UuYqfowTAniSaFYRu2W4efnatcyOl"

# login to twitter api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# iterates over pictures in models folder
os.chdir('models')
for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    time.sleep(3)
