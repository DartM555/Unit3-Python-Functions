# Practice Question #4

# def calculate_discount(price, member_status):
#     if member_status == "premium":
#         return price * 0.7
#     elif member_status == "standard":
#         return price * .85
#     else:
#         return price
    
    
#question #6

# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in text:
#         if char in vowels:
#             count += 1
#     return count  

# print(count_vowels("Hello World"))


def validate_password(password):
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    