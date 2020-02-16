# TODO Add functionality for multiple subreddits at once

import praw
import dropbox
import secrets

def send_to_dropbox(dbx, url):
    img_extension = url.split('.')[-1]
    dbx.files_save_url(f'/meme.{img_extension}', url)

    return 'Hello there from MugMeBot!'

if __name__ == '__main__':
    # Create Dropbox instance
    dbx = dropbox.Dropbox(secrets.dropbox_oauth)

    # Create Reddit instance using config from praw.ini
    reddit = praw.Reddit()
    subreddit = reddit.subreddit('testingground4bots')
    mugme_user = reddit.user.me()
    keyphrase = '!MugMeBot '

    # Check for keyphrase in comments
    for comment in subreddit.stream.comments():
        if comment.body.startswith(keyphrase) and (comment not in mugme_user.saved(limit=None)):
            print(comment.body)
            print(comment.submission.url)

            # Upload image to dropbox, get shopify link as response
            reply = send_to_dropbox(dbx, comment.submission.url)
            comment.reply(reply)
            print('Replied')

            # Save comment so bot doesn't reply again later
            comment.save()
