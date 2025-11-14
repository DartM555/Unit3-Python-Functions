# Question #1 - Code Writing

def combine_values(*values):
    if not values:
        return 1
    product = 1
    for v in values:
        product *= v
    return product
   
print(combine_values(2,3,4))
print(combine_values(5))
print(combine_values())
    
        

# Question #2 - Code Writing (**kwargs)

def merge_details(label, info):
    result = {"label":label}
    result.update(info)
    return result

print(merge_details("ItemA", size="large", cost = 12.50))
print(merge_details("UserX"))

# Question #3 - Code Tracing

# Answer:8,10,0

# Explanation: You combine the data and multiply it by 2, so 3+1=4 -> 4*2=8. The next is ten
# because the value is 2, but it says the rate is 5, so 2*5 is 10. Finally, there is no value
# for the last output, so we get 0


# Question #4 - Code Tracing

# Answer: 
# {'name': 'Alpha', 'x': 1, 'y': 2, 'count': 2}
# {'name': 'Beta', 'count': 0}

