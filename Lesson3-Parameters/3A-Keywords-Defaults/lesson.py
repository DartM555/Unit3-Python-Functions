def calculate_cart_total(*prices):
    """Calculate total for any number items
    Parameters: variable number of price values
    Returns: Total sum of all prices rounded to 2 decimal
    """
    # check if cart is empty
    if not prices:
        return 0.00
    # sum all prices
    subtotal = sum(prices)
    # Round to 2 decimals and return
    return round(subtotal, 2)
print(f"Empty Cart: ${calculate_cart_total()}")
print(f"1 Item: ${calculate_cart_total(19.99)}")
print(f"2 Items: ${calculate_cart_total(19.99, 67.67)}")
print(f"3 ITems: ${calculate_cart_total(19.99, 67.67, 17.38)}")
print(f"4 ITems: ${calculate_cart_total(19.99, 67.67, 17.38, 62.63)}")

def create_order(customer_name, **items):
    """Create an order with any menu items"""
    order = {
        "customer": customer_name,
        "items": items,
        "item_count": len(items),
    }
    return order

# Different Customers, different orders
order1 = create_order("Alex, pizza = 2, soda= 1, wings=12")
order2 = create_order("John", burger = 1, soda= 1, nuggets=6)
order3 = create_order("Atisse", salad = 1)

print(f"Order 1: {order1}")
print(f"Order 2: {order2}")
print(f"Order 3: {order3}")
    
    
# Parameter order is strict
def function(required, *args, default=10, **kwargs):
    pass
    