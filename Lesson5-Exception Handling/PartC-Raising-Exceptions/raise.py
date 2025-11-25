# The raise syntax
# Basic Syntax
"""
raise ExceptionType("Your message!")
Examples:
raise ValueError("Quantity myst be at least 1")
raise TypeError("expected a player object, got a potato)
raise PermissionError("You are not a mod, nice try though!)
"""
# Just returning
def open_loot_box(player, quantity):
    if quantity <= 0:
        return None
    # Rest of the code
    
# Raising exception
def open_loot_box(player, quantity):
    if quantity <= 0:
        raise ValueError("Bad quantity!")
    # Rest of the code
    
VALID_PROTEINS = ['chicken', 'steak', 'barbacoa', 'carnitas']
VALID_RICE = ['white', 'brown', 'none']
VALID_BEANS = ['black', 'pinto', 'none']
MAX_FREE_EXTRAS = 3

def build_bowl(protein, rice, extras):
    """Buld a Chipotle bowl with validation
    
    Raises:
    ValueError: If protein is invalid
    TypeError: If extras is not a list
    """
    
    # 1 - Check if extras is not a list
    if not isinstance(extras, list):
        raise TypeError("Extras must be a list!")
    # 2 - Validate protein
    if protein.lower() not in VALID_PROTEINS:
        raise ValueError(f"'{protein}' is not valide! Choose from {VALID_PROTEINS}")
    # 3 - Return the bowl
    return { 
            "protein": protein.lower(),
            "rice": rice,
            "extrax": extras,
            "price" : 10.50}
    
# Test the function
try:
    bowl = build_bowl("chicken", "brown", ["corn"])
    print(f"Created bowl: {bowl}")
except Exception as e:
    print(f"Error: {e}")