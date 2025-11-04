# Question #1 - Code Tracing

# Answer: ["key_a": "value_1", "key_b": "150", "key_d": 50] ; False
data = {"key_a": "value_1", "key_b": "100", "key_c": False}
data["key_d"] = 50
data["key_b"] = 150

x = data.pop("key_c")

print(data)
print(x)


# Explanation: After giving the initial data, we add key_d with a value of 50.
# We remove the "key_c", which leaves us with False

# Question #2 - Code Tracing

# Answer: 120 ; 60

# For the total, we add the two data values together, 100 and 20. 
# We then divide that by 2 to get value Z, 60.

# Question #3 - Code Writing (Bio Checker)

def get_user_bio(user):
    for key in user:
        if "bio" in user:
            return user["bio"]
    return "No bio available"

print(get_user_bio({"username": "coder", "bio": "Python Enthusiast"}))
print(get_user_bio({"username": "newbie"}))

# Question #4 - Code Tracing

# Answer:  110, 60

# Explanation: The inital values of the data is 110, 50, and 150.
# For the data in the users, we add 10 to all of the values.
# Since they only ask for the first two values, we return 110 and 60.

# Question #5 - Code Tracing

# Answer: 0

# Explanation: The code wants to find and false status in the record. 
# However, there are no false statuses in the record, so the count does not increase.

# Question #6 - Code Writing (get total engagement)

def get_total_engagement(post):
    total = 0
    for key in post:
        if "likes" in post and "comments" in post and "shares" in post:
            total = post["likes"] + post["comments"] + post["shares"]
            return total
        return 0
    
print(get_total_engagement({"likes": 100, "commments": 20, "shares": 10}))

# Question #7 - Code Tracing

# Answer:  3; 3

# Explanation: We are counting how many times alpha appears in the data. We see alpha 3 times.
# Then we count the length of the data, which is 3

# Question #8 - Code Tracing

# Answer: 

# Question #9 - Code Writing
def find_most_followed(users):
    for user in users:
        max_followers = 0
        if user["followers"]

