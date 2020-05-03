import pandas as pd
import numpy as np

trump = []
for line in open('project-trump.txt', 'r'):
    trump.append(json.loads(line))
for line in trump:
    if len(line) == 1:
        trump.remove(line)
trump_text = []
for tweet in trump:
    trump_text.append(tweet['text'])
trump_text = pd.Series(trump_text)
trump_text = trump_text.str.lower()

# %% Code for getting terms to determine tweet polarity
terms = pd.read_csv('list of terms.txt',
                    sep=' ',
                    header=None,
                    names=['Type', 'Length', 'Word', 'pos1', 'stemmed', 'polarity'])

wordList = pd.Series(terms['Word'])
wordList = wordList.str.slice(start=6, stop=None, step=None)  # trimming the Word column so its just the words
terms['WordsTrimmed'] = wordList

for index, row in terms.iterrows():  # this loop is keeping only the non-stemmed words
    if row['stemmed'] == "stemmed1=y":
        terms.drop(index, inplace=True)

strongPositive = []
positive = []
negative = []
strongNegative = []
for index, row in terms.iterrows():
    if row['Type'] == "type=weaksubj":  # must be either positive or negative, not strong
        if row['polarity'] == "priorpolarity=negative":  # just negative words, no strong negatives
            negative.append(row['WordsTrimmed'])
        if row['polarity'] == "priorpolarity=positive":
            positive.append(row['WordsTrimmed'])
    elif row['Type'] == "type=strongsubj":
        if row['polarity'] == "priorpolarity=negative":  # just negative words, no strong negatives
            strongNegative.append(row['WordsTrimmed'])
        if row['polarity'] == "priorpolarity=positive":
            strongPositive.append(row['WordsTrimmed'])

# %% Code for tweet polarity and approval rating
strongPositive_list = []
positive_list = []
strongNegative_list = []
negative_list = []
for tweet in trump_text:
    tweet = tweet.split()
    strongPositive_list.append(np.intersect1d(tweet, strongPositive))
    positive_list.append(np.intersect1d(tweet, positive))
    strongNegative_list.append(np.intersect1d(tweet, strongNegative))
    negative_list.append(np.intersect1d(tweet, negative))

strongPositive_points = []
positive_points = []
strongNegative_points = []
negative_points = []
sp = 10  # values to multiply by count of each term
p = 5
sn = -10
n = -5
for line in strongPositive_list:
    strongPositive_points.append(len(line) * sp)
for line in positive_list:
    positive_points.append(len(line) * p)
for line in strongNegative_list:
    strongNegative_points.append(len(line) * sn)
for line in negative_list:
    negative_points.append(len(line) * n)

strongPositive_points = np.array(strongPositive_points)
positive_points = np.array(positive_points)
strongNegative_points = np.array(strongNegative_points)
negative_points = np.array(negative_points)

approval = strongPositive_points + positive_points + strongNegative_points + negative_points
approval = pd.Series(approval)
print(approval.min())
print(approval.max())
print(approval.mean())
approval_grouped = approval.groupby(approval).count()

approval_grouped.to_csv("approval.csv", encoding='utf-8')

#%% Finding 25 most popular hashtags in tweets about Trump

hashtagList01 = []
for tweet in trump_text:
    if tweet.count('#') > 0:                                                # determines if tweet has a hashtag
        words = pd.Series(tweet.split())                                    # splits the tweets
        hashtagList01 = hashtagList01 + list(words[words.str.contains('#')])    # adds hashtags to the list
hashtagList01 = pd.Series(hashtagList01)                                        # makes it into a series
hashtagList01 = hashtagList01[hashtagList01.str.startswith('#')]
trump01_hashtags = hashtagList01.value_counts()

print(trump01_hashtags[0:25])

#%% Finding 25 most popular mentions in tweets about Trump

mentionList01 = []
for tweet in trump_text:
    if tweet.count('@') > 0:                                                # determines if tweet has a hashtag
        words03 = pd.Series(tweet.split())                                    # splits the tweets
        mentionList01 = mentionList01 + list(words03[words03.str.contains('@')])    # adds hashtags to the list
mentionList01 = pd.Series(mentionList01)                                        # makes it into a series
mentionList01 = mentionList01[mentionList01.str.startswith('@')]
trump01_mentions = mentionList01.value_counts()

print(trump01_mentions[0:25])
