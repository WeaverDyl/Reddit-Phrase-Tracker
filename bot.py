import praw, prawcore, argparse, csv, time, re
from datetime import datetime

def authenticate():
    """Logs into Reddit through PRAW so data collection can start"""
    reddit = praw.Reddit('phrasetrend', user_agent="Phrase trend detector")
    return reddit

def collect_comment_info(reddit, thread_url, phrase):
    """Goes throgh the reddit post, searching every comment for the given phrase,
    returns a csv containing a timestamp and id of every comment containing the
    phrase"""
    try:
        submission = reddit.submission(url=thread_url)
        with open('comments.csv', 'w', newline='') as score_file:
            writer = csv.writer(score_file)
            writer.writerow(["Time", "id"]) # Write column names

            submission.comments.replace_more(limit=None, threshold=0)
            r = re.compile(r'\b' + phrase + r'\b')
            for comment in submission.comments.list():
                if r.search(comment.body):
                    writer.writerow([time.time(), comment.id])
            return
    except prawcore.exceptions.NotFound:
        print("Invalid thread URL!")
        return None
    except Exception as e: # narrow down
        # possibility that comment was deleted/removed
        print("Custom error:", type(e), e)
        return None

def main():
    """Runs the program"""
    thread, phrase = get_args()
    reddit = authenticate()
    comment_info = collect_comment_info(reddit, thread, phrase)
    print(f"Collected all comments up to {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def get_args():
    """Sets up the argument parser, returning the Reddit thread URL and
    the phrase to collect data for"""
    parser = argparse.ArgumentParser()
    parser.add_argument("thread", help="Stores the Reddit thread URL")
    parser.add_argument("phrase", help="Stores the phrase to search for")

    args = parser.parse_args()
    thread = args.thread
    phrase = args.phrase

    return thread, phrase

if __name__ == "__main__":
    main()