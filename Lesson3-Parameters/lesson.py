# Using keyword arguements
def create_gamer(username, level, xp, rank, online):
    """Create a gamer profile"""
    return{
        "username": username,
        "level": level,
        "xp": xp,
        "rank": rank,
        "online": online
    }
    
player1 = create_gamer(
    username = "BTStudent",
    level = 25,
    rank = "Gold",
    xp = 10000,
    online = True
    )
print(player1)

def send_message(sender, recipient, message, urgent):
    return {
        "sender": sender,
        "recipient": recipient,
        "message": message,
        "urgent": urgent,
    }
email = send_message(
      sender = "Alex",
      recipient = "Jordan",
     message = "Check Discord",
     urgent = True,
    )
print(send_message)


def post_content(username,text,likes=0,retweets=0):
   return f"@{username}: {text} | ❤️ {likes} 🔁 {retweets}"

print(post_content("techguru", "Python is amazing!"))
    
# *args - Accept Any Number of Values
def sum_scores(*scores):
    """Sum ANY Number of Scores"""
    total = 0
    for score in scores:
        total += score
    return total
result = sum_scores(10,20,30)
result = sum_scores(10,20,30,60,67,55)
