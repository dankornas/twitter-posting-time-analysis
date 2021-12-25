# twitter-posting-time-analysis

This is project allows a user to parse THEIR OWN twitter profile posts to and do simple  and date analysis to see what posting times yield the best engagement.

**DISCLAIMER! - I am not responsible in any way for what you do with these scripts, especially parsing Twitter. I am not responsible if you get blocked or banned by Twitter.**

### What you need for it to work

1. You need Python 3.6 or higher.
2. Install the requirements from requirements.txt
3. By default, you need Windows and Microsoft Edge (sorry for the inconvenience) for the parsing mechanism to work.
   1. You can replace Microsoft Edge with a different browser engine in the twitterscraper.py file. Then you can do it on any operating system.

### How to use it

I suggest using the jupyter notebook file version - post_time_analysis.ipynb. The file first uses selenium to parse your Twitter profile. Be sure to replace the string:

```python
twitterUser = 'yourTwitterHandleHere'
```

with your own Twitter handle. The parsing can take a couple of minutes depending on how many tweets you have. This does not include retweets, only your personally created tweets.

Once the parsing is done, a CSV file will be created and then read into a pandas dataframe and cleaned up.

Finally, I have prepared some simple stats to show such as how many likes each our and each day you get. Feel free to play around a do some data analysis on your own!
