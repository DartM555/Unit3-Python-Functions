# Scope - The visibility of variables, where it can be seen and used
# Global - Outside all functions
# Local - inside a function(only visible there )

# The BUG - Crashes(UnboundLocalError)
def add_bonus():
    score = score + 100 # Python thinks its local
    
score = 500
add_bonus()
