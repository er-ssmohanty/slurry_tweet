In this example program, we read in the racial slurs from a file called 'racial_slurs.txt', and we read in the tweets from a file 
called 'tweets.txt'. We use a set to store the racial slurs, because sets have faster lookup times than lists (which can be 
important if we have a large number of slurs).
																
We then loop through each tweet and count the number of times each racial slur appears in the tweet. We sum these counts to get 
the total profanity score for the tweet, and we output the profanity score along with the tweet number. The tweet number is just
 i+1, because Python lists are zero-indexed but we want to start counting from 1.
