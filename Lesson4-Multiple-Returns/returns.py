def search_data(query):
    if query =="":
        return None # No query provided
    if query == "empty":
        return 0 # Found 0 results
    if query == "error":
        return False # Search failed
    return len(query) # Normal case - return count

#1 Return Type - None -> "No Value"
# Meaning: Absense of value, not set, not found
# Use for: Missing data, search failures, optional parameters
result = None
print(result is None) #True - identity check
print(result == None) #True - equality check
print(not result)     #True - falsy check

#2 Return Type - False -> Boolean False
# Meaning: Explicit false condition, validation failure, negative result
# Use fpr: Validation result, boolean operations, success/failure status
result = False
print(result is False)  #True - identity check
print(not result)       #True - boolean negation
print(result == 0)  #True - falsy check

#3 Return Zero - A valid number
# Zero is VALID numeric value, not absense of value!

result = 0
print(result == 0)          #True - Numeric equality
print(not result)           #True - (falsy in boolean context)
print(result is not None)   #False - different objects
print(result is False)      #False - different types
