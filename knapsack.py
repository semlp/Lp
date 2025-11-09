def fractional_knapsack(weights, values, capacity):
    n = len(values)
    ratio = []  # value/weight ratio
    for i in range(n):
        ratio.append(values[i] / weights[i])
    # Step 2: Sort items by ratio in descending order
    items = list(zip(values, weights, ratio))
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0.0
    remaining_capacity = capacity

    print("\nItem selection process:")
    print("Value\tWeight\tRatio\tTaken")
    # Step 3: Pick items greedily
    for value, weight, r in items:
        if remaining_capacity == 0:
            break
        if weight <= remaining_capacity:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
            print(f"{value}\t{weight}\t{r:.2f}\t1 (full)")
        else:
            # Take fractional part
            fraction = remaining_capacity / weight
            total_value += value * fraction
            print(f"{value}\t{weight}\t{r:.2f}\t{fraction:.2f} (partial)")
            remaining_capacity = 0  # Knapsack is now full
    return total_value
# --- Main Program ---
n = int(input("Enter number of items: "))
values = []
weights = []
for i in range(n):
    v = float(input(f"Enter value of item {i+1}: "))
    w = float(input(f"Enter weight of item {i+1}: "))
    values.append(v)
    weights.append(w)
capacity = float(input("Enter knapsack capacity: "))
max_value = fractional_knapsack(weights, values, capacity)
print(f"\nMaximum value in Knapsack = {max_value:.2f}")
