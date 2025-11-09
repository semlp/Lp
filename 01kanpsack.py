def knapsack_01(weights, values, capacity):
    n = len(values)
    # DP table: dp[i][w] = maximum value using first i items and capacity w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    # Build table bottom-up
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    # Traceback to find which items are included
    res = dp[n][capacity]
    w = capacity
    selected = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == dp[i - 1][w]:
            continue
        else:
            selected.append(i - 1)
            res -= values[i - 1]
            w -= weights[i - 1]

    selected.reverse()
    return dp[n][capacity], selected
# --- Main Program --- 
n = int(input("Enter number of items: "))
values = []
weights = []
for i in range(n):
    v = int(input(f"Enter value of item {i+1}: "))
    w = int(input(f"Enter weight of item {i+1}: "))
    values.append(v)
    weights.append(w)
capacity = int(input("Enter knapsack capacity: "))
max_value, selected_items = knapsack_01(weights, values, capacity)

print("\nItem selection process:")
print("Item\tValue\tWeight\tSelected")
for i in range(n):
    print(f"{i+1}\t{values[i]}\t{weights[i]}\t{'Yes' if i in selected_items else 'No'}")

print(f"\nMaximum value in Knapsack = {max_value}")

   