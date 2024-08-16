import praw

CLIENT_ID = ''
SECRET_KEY = ''

with open('api.txt', 'r') as f:
    CLIENT_ID = f.readline().strip()
    SECRET_KEY = f.readline().strip()

with open('pw.txt', 'r') as f:
    pw = f.read()

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=SECRET_KEY,
    user_agent="POB SCRAPPER by u/zZUST13",
    username= "zZUST13",
    password= pw,
)

subreddit = reddit.subreddit("pathofexile")

top_posts = subreddit.top(limit=10)
new_posts = subreddit.new(limit=10)

for post in top_posts:
    print("Title - ", post.title)
    print("ID - ", post.id)
    print("Author - ", post.author)
    print("URL - ", post.url)
    print("Score - ", post.score)
    print("Comment count - ", post.num_comments)
    print("Created - ", post.created_utc)
    print("\n")

post = reddit.submission(id="dwx2rt")

comments = post.comments

for comment in comments[:2]:
    print("Printing comment...")
    print("Comment body - ", comment.body)
    print("Author - ", comment.author)
    print("\n")