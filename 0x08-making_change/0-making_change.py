#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array with a large number
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make 0 amount

    # Update dp array based on coin denominations
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, return -1, meaning it's not possible to form the amount
    return dp[total] if dp[total] != float('inf') else -1


