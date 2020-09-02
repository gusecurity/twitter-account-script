import random
import tweepy as tw
import json
from time import sleep
import logging


# use key to auth
def auth():
    """
    :return: api, authenticated with credentials
    """
    with open('creds.json') as creds:
        credentials = json.load(creds)  # load creds of api from json

    auth = tw.auth.OAuthHandler(
        credentials["consumer_key"], credentials["consumer_secret"])
    auth.set_access_token(
        credentials["access_token"], credentials["access_secret"])
    api = tw.API(auth, wait_on_rate_limit=True)
    return api


def run(hash_tag):
    """
    :param hash_tag: hash tag to search in order to find things to re-tweet
    """
    for tweet in tw.Cursor(api.search, q=hash_tag).items(1):
        try:
            logging.info('\nTweet by: @' + tweet.user.screen_name)
            tweet.retweet()  # turn of to not retweet
            logging.info('Retweeted the tweet')
            tweet.favorite()  # turn off to not like

            if not tweet.user.following:
                tweet.user.follow()  # turn off to not follow
                logging.info(f"Followed the user {tweet.user}")

        except tw.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
    logging.warning("Exiting run")


if __name__ == '__main__':
    api = auth()
    hash_tags = ["#cybersecurity", "#hacking", "#security", "#hacker", "#technology", "#infosec",
                 "#ethicalhacking", "#tech", "#linux", "#cybercrime", "#malware", "#kalilinux", "#informationsecurity"]
    while True:
        logging.warning("Going into run")
        run(random.choice(hash_tags))  # put hashtags to scan here
        sleep(random.randint(500, 1100))  # how much to wait in ms after run
