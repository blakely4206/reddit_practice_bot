import praw

reddit = praw.Reddit(client_id = 'DNWcar3ZStWn-w', 
                    client_secret = 'nfJ11PZo_VhvCnJ3w7VA58T1GNc', 
                    username='man-who-says-cock', 
                    password = 'jb1570432', 
                    user_agent='cock_agent')

subreddit = reddit.subreddit('breakingbad')

hot_python = subreddit.new(limit=1)

for sub in hot_python:
    print("Sub Title: ", sub.title, "\nUpdoots ", sub.ups, "\nVisited: ", sub.visited)
    sub.reply('Sends chills down my spine')
    sub.comments.replace_more(limit=0)

    for comment in sub.comments.list():
        print(20*'-')
        print('Parent ID: ', comment.parent())
        print('Comment ID: ', comment.id)
        print(comment.body)
