''' Problem Statement: Implement a dynamic programming solution to the classic Knapsack Problem.
Given a set of items, each with a weight and a value, determine the number of each item to include
in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

Example: Items: [(weight: 1, value: 1), (weight: 3, value: 4), (weight: 4, value: 5), (weight: 5, value: 7)]
Weight limit: 7 Output: Maximum value = 9 (Choosing items with weights 3 and 4) '''

# I first learned about the Knapsack Problem in Spring of 2020, and haven't used it since. Needed a refresher
# on this, just like I did with Dijkstra's algorithm

def knapsack(items, weight_limit):
    # create a table to store the max value for different weights
    # rows represent items, cols represent weights
    # initialize the table with zeros
    dp_table = [[0] * (weight_limit + 1) for _ in range(len(items) + 1)]
    
    # iterate through each item
    for i in range(1, len(items) + 1):
        weight_i, value_i = items[i - 1]  # item's weight and value
        # iterate through each weight limit
        for w in range(1, weight_limit + 1):
            # if current item's weight exceeds the current weight limit, skip it
            if weight_i > w:
                dp_table[i][w] = dp_table[i - 1][w]
            else:
                # calculate the max value by either including or excluding the current item
                dp_table[i][w] = max(dp_table[i - 1][w], value_i + dp_table[i - 1][w - weight_i])
    
    # the max value is stored in the bottom-right cell of the table
    return dp_table[len(items)][weight_limit]

# items and weight limit given in example
items = [(1, 1), (3, 4), (4, 5), (5, 7)]
weight_limit = 7

# find the max value
max_value = knapsack(items, weight_limit)
print("Maximum value =", max_value)