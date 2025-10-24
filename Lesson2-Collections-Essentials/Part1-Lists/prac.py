# def filter_evens(numbers):
#     even = []
#     for num in numbers:
#         if even % 2 == 0:
#             even.append(num)
#     return even
        
# print(filter_evens([1, 2, 3, 4, 5, 6]))
# print(filter_evens([10, 15, 20, 25, 30]))

def list_stats(numbers):
    for num in numbers:
        if not numbers:
            return None
    min = min(numbers)
    max = max(numbers)
    avg = round(sum(numbers) / len(numbers),2)
    
    
    print(list_stats([10, 20, 30, 40]))