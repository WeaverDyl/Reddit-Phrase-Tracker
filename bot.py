import praw

def authenticate():
    """Logs into Reddit through PRAW so data collection can start."""
    reddit = praw.Reddit('phrasetrend', user_agent="ENTER A USER AGENT HERE")
    return reddit

# Take in reddit thread & phrase, collect num of comments containing phrase
# and time posted. use matplotlib to generate chart