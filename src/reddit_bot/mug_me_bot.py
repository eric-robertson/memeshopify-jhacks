# TODO Add functionality for multiple subreddits at once
# TODO Get karma for the bot

import praw

# Create Reddit instance using config from praw.ini
#reddit = praw.Reddit('mugme-bot')
reddit = praw.Reddit()
subreddit = reddit.subreddit('testingground4bots')
mugme_user = reddit.user.me()

keyphrase = '!MugMeBot '

# Check for keyphrase in comments
for comment in subreddit.stream.comments():
    if comment.body.startswith(keyphrase) and (comment not in mugme_user.saved(limit=None)):
        print(comment.body)

        # Save comment so bot doesn't reply again later
        comment.save()

        # Reply
        comment.reply('Hello there from MugMeBot!')

        print('Replied')
