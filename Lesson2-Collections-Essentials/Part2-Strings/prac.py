def create_username(first_name, last_name):
    username = (first_name + "_" + last_name).lower()
    return username

print(create_username("John", "Smith"))
print(create_username("MARY", "Jones"))

def check_email(email):
    if "@" in email and ".com" in email:
        return True
    else:
         return False
    
print(check_email("test@gmail.com"))
print(check_email("user@yahoo.COM"))
print(check_email("invalid.com"))

# def check_email(email):
#     email = email.lower()
#     return "@" in email and email_lower_endswiths(".com")

def create_slug(title):
#  slug =  title.lower().replace(" ", "-").strip()
    # return slug
    return title.lower().replace(" ", "-").strip()
    
print(create_slug("My First Blog Post!"))
print(create_slug("   Pyton Tutorial   "))
