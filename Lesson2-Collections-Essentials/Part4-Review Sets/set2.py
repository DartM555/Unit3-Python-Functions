# Question 1 - Code Tracing

# Answer: 4 7000

# Test:
prices = [58200, 59500, 61000, 59800, 62500, 64000]
gains = []
i = 1
while i < len(prices):
    diff = prices[i] - prices[i-1]
    if diff > 1000:
        gains.append(diff)
    i += 1  
print((len(gains)))
print(sum(gains))

# Question 2 - Code Tracing

# Answer: 0...x...9...F...1...a...B...C......

# Test
wallet = "0x9F1aB3c...dE8f"
short = ""
i=0
while i < 10:
    short += wallet[i]
    i+=1
    short += "..."
print(short)

# Question 3 - Code Writing
holdings = {"BTC": 0.5,"ETH": 8.2,"SOL": 50}

prices = {"BTC": 62400,"ETH": 2480,"SOL": 142}


def portfolio_value(holdings, prices):
    total = 0
    for coin, amount in holdings.items():
        total += amount * prices[coin]
        return round(total, 2)

print(portfolio_value(holdings, prices))