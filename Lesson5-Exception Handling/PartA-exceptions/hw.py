# Question #3
def get_phone_number(contacts, name):
    try:
        return contacts[name]
    except KeyError:
       print("Contact not found.")
       
# Test
contacts = {"Mom": "555-0123",
            "Dad": "555-4567",
            "Best Friend": "555-0125"}

print(get_phone_number(contacts, "Mom"))
print(get_phone_number(contacts, "Dad"))
print(get_phone_number(contacts, "Best Friend"))
print(get_phone_number(contacts, "Boss"))

# Question #4
def get_song(playlist, position):
    try:
        return playlist[position]
    except IndexError:
        print("Position out of range")
    except:
        print("Position must be an integer")
        
playlist = ["Song A", "Song B", "Song C","Song D","Song E",]


# Question #5
def calculate_test_average(scores):
    try:
        total = sum(scores)
        count = len(scores)
        avg = total / count
        return round(avg, 2)
    except ZeroDivisionError:
        return 0
    except TypeError:
        return "invalid score data"