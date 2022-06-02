# Wednesday 30 Jun

# Implementation of the knapsack's problem solution

items_to_steal = {
    'stereo': {'price': 3000, 'weight': 4},
    'laptop': {'price': 2000, 'weight': 3},
    'guitar': {'price': 1500, 'weight': 1}
    } 

number_of_items = len(items_to_steal.keys())
size_of_knapsack = 4
grid = [[0]*size_of_knapsack]*number_of_items

for i in range(number_of_items):
    item = items_to_steal[i]
    for j in range(size_of_knapsack):
        prev_value = 0
        curr_value = #valor del item acutal + valor del item que quepa en la 

