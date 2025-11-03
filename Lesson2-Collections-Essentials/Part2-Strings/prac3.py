def sanitize_filename(filename):
    a = filename.replace(" ", "_")
    for char in a:
        # if not char .isalpha() and not char.isdigit()  and char not:    
            a = a.replace(char, "")
    if len(a) > 50:
        return "Invalid filename"
    return a

print(sanitize_filename("Ancient Scroll.txt"))
print(sanitize_filename("Quest 2042! (Epic)"))
print(sanitize_filename("notes"))