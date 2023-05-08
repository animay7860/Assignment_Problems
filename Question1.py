import re

# read in the file of tweets
with open("tweets.txt", "r") as f:
    tweets = f.readlines()

# define the set of racial slurs
racial_slurs = {"w1", "w2", "w3"}

# define a function to calculate the degree of profanity for a given sentence


def degree_of_profanity(sentence):
    words = sentence.split()
    num_slurs = len([w for w in words if w.lower() in racial_slurs])
    return num_slurs / len(words)


# iterate over the tweets and calculate the degree of profanity for each sentence
for tweet in tweets:
    sentences = re.split(r"\s+", tweet)
    for sentence in sentences:
        if len(sentence) > 0:
            profanity = degree_of_profanity(sentence)
            print(f"Sentence: {sentence.strip()}")
            print(f"Profanity: {profanity:.2f}")
            print()
