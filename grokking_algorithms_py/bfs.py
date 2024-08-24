# Monday 14 June

# Implementation of breadth-first search

from collections import deque

# Finding if there is / what's the closest connection in your FB friends that's 
# a mango seller.

# 1. Model the problem with a graph: Nodes are people and the edges represent 
# they're FB friends.

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

# 2. Solve the problem uding breadth-first search.

def person_is_seller(name):
    is_seller = False
    if 'ny' == name[-2:]:
        is_seller = True
    return is_seller

def breadth_first_search(person):
    search_queue = deque()
    search_queue += graph['you'] # Adds my neighbors to the search queue
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

breadth_first_search('you')
