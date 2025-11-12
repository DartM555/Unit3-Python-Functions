# Question #1 - Code Tracing

# Answer: [23]

# Test:
kills = [3, 0, 5, 2, 8, 1, 7]
streaks = []
current = 0
for k in kills:
    if k > 0: 
        current += k
    else:
        if current >= 5:
            streaks.append(current)
        current = 0
if current >= 5:    
    streaks.append(current)
print(streaks) 

# Question #2 - Code Tracing

# Answer: NEXUS

# Test:
player = "[NEXUS] ShadowViper"
tag = ""
i = 1
while player[i] != "]":
    tag += player[i]
    i += 1
print(tag)

# Question 3 - Code Writing
players = {
    "phoenix": {"kills":28, "deaths":12},
    "cipher": {"kills":35, "deaths":15},
    "blaze": {"kills":22, "deaths":18}
}

def match_pvp(players):
    best_player = ""
    best_ratio = 0.0
    for name, stats in players.items():
        ratio = stats["kills"] / stats["deaths"]
        if ratio > best_ratio:
            best_ratio = ratio
            best_player = name
    return best_player
print(match_pvp(players))

