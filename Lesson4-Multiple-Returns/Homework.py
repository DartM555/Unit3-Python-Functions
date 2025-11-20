# Question #1
def search_user_database(query):

    if query.strip() == "":
          return None, "No search query", False

    if not query.isAlpha():
        return False, "Invalid characters", False
    
    results = {
        "john": 3,
        "mary":1,
        "alex": 2,
    }
    
    if query not in results:
        return 0, "No users found", True
    count = results[query]
    return count, f"Found {count} users", True


# Question #2

def analyze_book_pages(pages):
    if len(pages) == 0:
        return 0, 0, 0.0, False
    count = len(pages)
    total_pages = sum(pages)
    avg_pages = total_pages / count
    
    has_long_book = any(p > 500 for p in pages)
    
    return count, total_pages, avg_pages, has_long_book


