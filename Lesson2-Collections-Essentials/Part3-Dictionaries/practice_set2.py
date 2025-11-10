# def calculate_engagement_rate(post):
#     # for key in post:
#         # if "likes" in post and "views" in post and "comments" in post and "shares" in post:
#         #     engagement = post["likes"] + post["comments"] + post["shares"]
#         #     rate = engagement / post["views"]
#         #     return rate
#         # else:
#         #    return 0
            
#         views = post.get("views", 0)
#     if views == 0:
#         return 0
#     likes = post.get("likes", 0)
#     comments = post.get("comments", 0)
#     shares = post.get("shares", 0)
#     engagement = likes + comments + shares

#     rate = engagement / views
#     return rate    
    
#     post = {"views": 1000, "likes": 50, "comments": 10, "shares": 5}
    
# print(calculate_engagement_rate(rate))