import praw, prawcore, argparse, pprint

def authenticate():
    """Logs into Reddit through PRAW so data collection can start."""
    reddit = praw.Reddit('phrasetrend', user_agent="Phrase trend detector")
    return reddit

# Take in reddit thread & phrase, collect num of comments containing phrase
# and time posted. use matplotlib to generate chart

def collect_comment_info(thread_id, phrase):
    """Goes throgh the thread_id, searching every comment for the given phrase,
    returns a list containing information about comments that had the phrase.
    """
    try:
        reddit = authenticate()
        submission = reddit.submission(id=thread_id)
        phrase_count = 0 # The total number of occurences of phrase
        comment_info = []

        submission.comments.replace_more(limit=None) # Gets all comments
        for comment in submission.comments.list():
            if phrase in comment.body:
                phrase_count += 1
                comment_info.append((comment.author.name, comment.id,
                                     comment.created_utc))
        return comment_info
    except prawcore.exceptions.NotFound:
        print("Invalid thread ID!")
        return None
    except Exception as e: # narrow down
        # possibility that comment was deleted/removed
        print("Custom error:", type(e), e)
        return None

def main():
    """Runs the program."""
    thread, phrase = get_args()
    comment_info = collect_comment_info(thread, phrase)

    if comment_info is not None:
        # process, create chart
        pass
    else:
        # exception
        print("An error occurred while searching through comments.")
        return

def get_args():
    """Setups up the argument parser, returning the Reddit thread ID and
    the phrase to collect data for."""
    parser = argparse.ArgumentParser()
    parser.add_argument("thread", help="Stores the Reddit thread ID")
    parser.add_argument("phrase", help="Stores the phrase to search for")

    args = parser.parse_args()
    thread = args.thread
    phrase = args.phrase

    return thread, phrase

if __name__ == "__main__":
    main()
