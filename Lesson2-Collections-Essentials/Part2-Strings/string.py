def format_course_code(code):
    # code = code.strip( )
    # code = code.upper( )
    # return code
    return code.strip().upper( )

print(format_course_code("  webdev101  "))

def count_hashtags(post):
#     count = 0
#     for char in post:
#         if char == "#":
#             count += 1
#     return count
    words = post.split()
    count = 0
    for words in words:
        if words.startswith("#"):
            count = count + 1
    return count
    pass
    
    filename = "assignment.pdf"
    print(filename.endswith(".pdf"))
    print(filename.endswith(".docx"))

print(count_hashtags("Great game today! #BergenTEch #GoGamrz #Pride"))
print(count_hashtags("Meeting tomorrow at room 205"))
print(count_hashtags("#Robotics team wins #StateChampionship #STEM #BergenTech"))
                    



# announcement = "  BERGEN TECH robotics meeting TODAY!  "