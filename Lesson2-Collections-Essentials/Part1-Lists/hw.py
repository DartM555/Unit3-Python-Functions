# Question 1
def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result

# Question 2
def find_common(list1, list2):
    return list(set(list1) and set(list2))

# Question 3
def reverse_sublists(data, step):
    result = []
    for i in range(0, len(data), step):
        chunk = data[i:i+step]
        result.extend(reversed(chunk[::-1]))
    return result
        
# Question 4
def rotate_list(items, positions):
    positions = positions % len(items)
    return items[-positions:] + items[:-positions]