def find_top_players(players, min_score):
    """ Return a list of usernames for players with score >= min_score """
    # YOUR CODE HERE
    top_player = []
    score = 0
    for player in players:
        if player[score] >= min_score:
            top_player.append(player["username"])
    pass
# Test it
players = [
    {"username": "DragonSlayer", "score": 8500},
    {"username": "NinjaWarrior", "score": 6200},
    {"username": "MageKing", "score": 9100},
    {"username": "ShadowAssassin", "score": 5800}
]

result = find_top_players(players, 7000)

#2
playlist = {
    "Workout Mix": ["Eye of the Tiger", "Stronger", "Lose Yourself"],
    "Study Vibes": ["Lofi Beats 1", "Chill Piano", "Rain Sounds"],
    "Party Hits": ["Uptown Funk", "Levitating", "Blinding Lights"]
}

all_songs = []

for playlist_name, songs in playlist.items():
    for song in songs:
        all_songs.append(song.upper())

print(f"Total songs: {len(all_songs)}")
print(f"First songs: {len(all_songs[0])}")
print(f"Last songs: {len(all_songs[-1])}")

# Total Songs: 9
# First Song: 16
# Last Song: 15 

def calculate_cart_total(cart):
    total = 0.0
    for item in cart:
       item_cost = item["price"] * item["quantity"]
       total += item_cost
       return total
   

