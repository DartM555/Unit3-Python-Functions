# # Question 1 - Code Tracing

# # Answer: 2300

# # Explanation: Goes through every single viewcount for the highest view count,
# # which is equal to i.It then prints the highest view count, 2300 

# # Test:
# viewers = [1240, 1580, 2100, 1890, 2300]

# peak = viewers[0]
# i = 1
# while i < len(viewers):
#     if viewers[i] > peak:
#         peak = viewers[i]
#     i += 1
#     print(peak)
    
# # Question 2- Code Tracing

# # Answer: WOW WOW LFG

# # Explanation: Keeps only words that are below 5 characters.

# # Test:
# message = "WOW POGGERS WOW LFG"
# words = message.split()
# filtered = ""
# for word in words:
#      if len(word) <= 5:
#          filtered += word + " "
# print(filtered.strip())

# Question 3 - Code Writing - Find The Top Donar and print the name

# Test
donations = {
    "neon": 250,
    "vibe": 180,
    "lunar": 400,
    "pixel": 150
}

def find_top_donor(donations):
    top_donor = ""
    top_amount = -1
    for name, amount in donations.items():
        if amount > top_amount:
            top_amount = amount
            top_donor = name
    return top_donor




print(find_top_donor(donations))


         