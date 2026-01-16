import praw
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",        # Replace with your Reddit app client ID
    client_secret="YOUR_CLIENT_SECRET",# Replace with your Reddit app client secret
    user_agent="YOUR_USER_AGENT"       # Replace with a descriptive user agent
)


def get_subreddits(subreddits, num_posts):
    title = []
    text = []
    post_id = []
    reddit_detail = []

    for sub in subreddits:
        subreddit_obj = reddit.subreddit(sub)
        for posts in subreddit_obj.top(limit=num_posts):
            title.append(posts.title)
            text.append(posts.selftext)
            post_id.append(posts.id)
            reddit_detail.append(posts.subreddit)

    res_dict = {"id": post_id, "subreddit": reddit_detail,
                "title": title, "text": text}

    return res_dict
