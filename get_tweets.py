###### TWITTER CLIENT ######
class TwitterClient():
    '''
    Class for using twitter client to access tweets of desired users
    '''

    def __init__(self, twitter_user=None, filename=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user
        self.filename = filename

    # This function is used pull the most recent tweets from a user's timeline
    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    # This function is used to extract the friends list of a certain user
    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    # This function extracts the home timeline tweets of a given user
    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets

    # This function can be used to write the extracted tweets to a text file
    def write_to_file(self, object_to_write, overwrite=True):
        if overwrite:
            with open(self.filename, 'w') as file:
                file.write(object_to_write + '\n')
                file.close()
        else:
            with open(self.filename, 'a') as file:
                file.write(object_to_write + '\n')
                file.close()
            return file


###### TWITTER AUTHENTICATOR ######
class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth


###### TWITTER STREAMER ######
class TwitterStreamer():
    '''
    Class for streaming and processing live tweets
    '''

    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, fetched_tweets_filename, tweet_limit, hash_tag_list):
        # This handles twitter authentications and the connection to the twitter streaming API
        listener = TwitterListener(fetched_tweets_filename, tweet_limit)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
        # Grabs the tweets containing the desired strings
        stream.filter(track=hash_tag_list)


###### TWITTER LISTENER ######
class TwitterListener(StreamListener):
    """
    Basic Listener Class that just prints received tweets to stdout
    """

    def __init__(self, fetched_tweets_filename, tweet_limit):
        self.fetched_tweets_filename = fetched_tweets_filename
        self.counter = 0
        self.limit = tweet_limit
        open(self.fetched_tweets_filename, 'w').close()

    def on_data(self, data):
        try:
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)  # tf.write(data + '\n')
            self.counter += 1
            if self.counter < self.limit:
                print(self.counter)
                return True
            else:
                return False
        except BaseException as e:
            print('Error on data: %s' % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            # Returning false on data method in case rates limit occurs
            return False
        print(status)

# %% Code for pulling tweets
hash_tag_list = ['Trump']
fetched_tweets_filename = 'project-trump.txt'
twitter_streamer = TwitterStreamer()
twitter_streamer.stream_tweets(fetched_tweets_filename, 10000, hash_tag_list)