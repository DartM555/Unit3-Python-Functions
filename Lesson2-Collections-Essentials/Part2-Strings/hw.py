# Question #1
# Answer: john.smith  gmail.com

# Question #2

# Answer: t q b f

# Question #3

def extract_domain(email):
    email = email.count("@")
    if email != 1:
        return "Invalid email"
    email = email.lower()
    domain = email.split("@")[1]
    return domain
    
print(extract_domain("john@gmail.com"))
print(extract_domain("JANE@YAHOO.COM"))

# Question #4

# Finds the numbers
# Answer: 123456

# Question #5

# Ans:MY_DOCUMENT

# Question #6

# locates longest
# Answer: banana

# Question #7
def filter_numbers(text):
    res = ""
    for char in text:
        if char.isdigit():
            res += char
    return res

# Question #8
# Answer: https://example.com/user/profile

# Question #9
def count_character_types(text):
    letter = 0
    digit = 0
    space = 0
    
    for char in text: 
        if char.isalpha():
            letter += 1
        elif char.isdigit():
            digit += 1
        elif char == " ":
            space += 1
    return letter, digit, space

