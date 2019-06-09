import requests, json, time, argparse, csv
from datetime import datetime

def download(thread_id, phrase, hours):
    THREAD_CREATED = get_creation_utc(thread_id)
    NEWEST_DATA_UTC = THREAD_CREATED + (60 * 60 * hours)
    BASE_URL = 'https://api.pushshift.io/reddit/comment/search/'
    PARAMS = {
        'link_id': thread_id,
        'q': phrase,
        'aggs': 'created_utc',
        'before': NEWEST_DATA_UTC,
        'frequency': 'minute',
        'size': 0
    }

    data = json.loads(requests.get(BASE_URL, params=PARAMS).text)['aggs']
    return data, THREAD_CREATED, NEWEST_DATA_UTC

def process(data, thread_created_utc, newest_data_utc):
    with open('comments.csv', 'w', newline='') as score_file:
        writer = csv.writer(score_file)
        writer.writerow(["Time", "ID"]) # Write column names
        for point in data['created_utc']:
            writer.writerow([point['key'], point['doc_count']])
    return

def get_creation_utc(thread_id):
    """Gets the UTC timestamp of when the thread was created"""
    BASE_URL = 'https://api.pushshift.io/reddit/submission/search/'
    PARAMS = {
        'ids': thread_id
    }

    thread_data = json.loads(requests.get(BASE_URL, params=PARAMS).text)['data']
    return thread_data[0]['created_utc']

def get_args():
    """Sets up the argument parser, returning the Reddit thread URL and
    the phrase to collect data for"""
    parser = argparse.ArgumentParser()
    parser.add_argument("thread", help="Stores the Reddit thread URL")
    parser.add_argument("phrase", help="Stores the phrase to search for")
    parser.add_argument("hours", help="Stores the number of hours to aggregate from the post creation time")

    args = parser.parse_args()
    thread = args.thread
    phrase = args.phrase
    hours = args.hours

    return thread, phrase, hours

def main():
    thread, phrase, hours = get_args()
    data, thread_created, newest_data_utc = download(thread, phrase, int(hours))
    process(data, thread_created, newest_data_utc)

if __name__ == "__main__":
    main()
    