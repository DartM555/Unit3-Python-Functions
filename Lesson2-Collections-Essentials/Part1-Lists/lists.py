'''
JavaScript vs Python:

create: [1, 2, 3] vs [1, 2, 3]
add: .push(val) vs .append(val)
remove end: .pop() vs .pop()
insert: .splice(index, 0, val) vs. .insert(index, val)
length:  len()
max/min: max()/min()
sum: sum()
'''


# Creating Lists
daily_likes = [500, 600, 750, 400]
usernames = ["@nasa", "@tswift", "@netflix"]
mixed_data = [500, "likes", "@user1234", True]
# accessing elements
first_day = daily_likes[0]
last_day = daily_likes[-1]
third_day = daily_likes[2]
# Slicing (like JavaScript slice())
first_three = daily_likes[0:3]
last_two = daily_likes[-2:]

# Code Along - Post Analyzer
def analyze_post(likes_list):
    if likes_list:
     total = sum(likes_list)
    average = total / len(likes_list)
    best_day = max(likes_list)
    return(average, best_day)
# Format usernames
def format_usernames(handles):
    '''Add @ prefix to all usernames.'''
    formatted = []
    for handle in handles: 
        formatted.append("@" + handle)
        return formatted

result = format_usernames(["nasa", "tswift", "netflix"])

def filter_trending_posts(likes_list):
    '''Return posts with over 1000 likes'''
    trending = []
    for likes in filter_trending_posts:
        if likes > 1000:
            trending.append(likes)
        return trending
    