# Wednesday 16 June

# Implementation of directed and weighted graphs and Dijkstra's Algorithms

infinity = float('inf')

graph = {
    'book': {'lp':5, 'poster': 0},
    'lp': {'bass guitar': 15, 'drums': 20},
    'poster': {'bass guitar':30, 'drums': 35},
    'bass guitar': {'piano':20},
    'drums': {'piano': 10},
    'piano': {}
    }

costs = {
    'lp': 5,
    'poster': 0,
    'bass guitar': infinity,
    'drums': infinity,
    'piano': infinity
    } 
    
parents = {
    'lp': 'book',
    'poster': 'book'}

def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if (cost < lowest_cost) and (node not in processed):
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def djk(graph, costs, parents):
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
                print(parents)
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    return parents

djk(graph, costs, parents)