# Tweet script for GUSEC twitter account

Needs [twitter dev account](https://developer.twitter.com/en/apply-for-access) keys to function. Place in json file called `creds.json`. Takes random choice of hashtags then performs the choice of actions and times out for some time.

Currently auto-pushes to my dockerhub for image deployment on heroku. If you need to change what account is pushed to then change the secrets in repo.

## Cloning the repo

```bash
workspace$: git clone https://github.com/gusecurity/twitter-account-script.git
```

or using ssh:

```bash
git clone git@github.com:gusecurity/twitter-account-script.git
```

## To select hashtags and time-out time between actions

```python
if __name__ == '__main__':
    api = auth()
    while True:
        logging.warning("Going into run")
        run(random.choice(["#cybersecurity"]))  # put hashtags to scan here
        sleep(random.randint(500, 1100))  # how much to wait in ms after run
```

## To select actions performed

```python
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
                logging.info(f'Followed the user {tweet.user}')

        except tw.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
    logging.warning("Exiting run")
```

## To run the script

```bash
workspace$: python tweet.py
```
