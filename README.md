# Reddit-Phrase-Tracker

Creates charts based on the trends of certain comment phrases within a Reddit thread.

Inspired by [this](https://www.reddit.com/r/dataisbeautiful/comments/8ybsr3/uses_of_the_word_fuck_in_the_rsoccer_match_thread/) Reddit post, I've finally gotten around to designing a program to easily replicate the results shown.

Example:
 
Reddit post:

![](https://i.redd.it/jjy7s72ixj911.png)

My program (Running `python dl_process_comments.py -t 8y1m08 -p fuck -n 4`):  

![](https://imgur.com/inEEHra.png)

Another example from the 2019 Canadian Grand Prix:

![](https://imgur.com/Oz0cGmW.png)

The uses of the word 'penalty' spiked due to a controversial FIA call that caused Hamilton to win the race despite Vettel finishing first.

## Setup

You must have [PRAW](https://praw.readthedocs.io/en/latest/) installed to run this program. Install it using `pip install praw`.

You must also have [R](https://www.r-project.org/) installed along with the [Tidyverse](https://www.tidyverse.org), [anytime](https://github.com/eddelbuettel/anytime), and [scales](https://cran.r-project.org/web/packages/scales/index.html) libraries installed.

Create a `praw.ini` file with the following format:

	[phrasetrend]
	username=YOUR_REDDIT_USERNAME
	password=YOUR_REDDIT_PASSWORD
	client_id=YOUR_REDDIT_CLIENT_ID
	client_secret=YOUR_REDDIT_CLIENT_SECRET  

## Running the Program

Simply run `python dl_process_comments.py -t THREAD_ID -p PHRASE -n NUM_HOURS_TO_COLLECT`. The program will output a `matched_comments.csv` and `all_comments.csv` file, each containing two columns:

1. The Unix timestamp of each comment containing the phrase
2. The corresponding Reddit comment ID

These files are used in R to create a plot of the data in the CSV file. Do this by running `Rscript plot.r`.

## LICENSE

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
