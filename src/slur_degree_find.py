import sys

# Read in the racial slurs from a file
with open('racial_slurs.txt', 'r') as f:
    racial_slurs = set(line.strip().lower() for line in f)

# Read in the tweets from a file
with open('tweets.txt', 'r') as f:
    tweets = [line.strip().lower() for line in f]

# Check each tweet for profanity
for i, tweet in enumerate(tweets):
    profanity_score = sum(tweet.count(slur) for slur in racial_slurs)
    print(f"Tweet {i+1}: profanity score = {profanity_score}")
