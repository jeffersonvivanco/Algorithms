# Simple flight program
# This program uses breadth-first search to find the fastest flight to your destination.
# Note: This program only supports a few countries.

from collections import deque

graph = {}
graph['USA'] = ['CANADA', 'UK', 'MEXICO']
graph['CANADA'] = ['USA','UK']
graph['UK'] = ['USA', 'ICELAND']
graph['MEXICO'] = ['USA', 'PERU']
graph['PERU'] = ['ARGENTINA']
graph['ARGENTINA'] = ['MEXICO', 'CHILE']
graph['ICELAND'] = ['GREENLAND']
graph['GREENLAND'] = ['CANADA']
graph['CHILE'] = []

print('List of countries we fly to and from.\n')
for key in graph.keys():
    print(key)

missingData = True

while missingData:
    origin = input('Where are you flying from ?\n')
    if origin.upper() not in graph.keys():
        print("We don't fly from that country, please refill form.")
        continue
    destination = input('Where are you flying to ?\n')
    if destination.upper() not in graph.keys():
        print("We don't fly to that country, please refill form.")
        continue
    missingData = False



origin = origin.upper()
destination = destination.upper()

search_queue = deque() # creates a new queue
search_queue += graph[origin] # this is adding all the direct flights from this country
parent_root_queue = deque()
parent_root_queue.append(origin)
parent_children_num = len(graph[origin])
path_dict = {}
searched_list = []

parent_root = parent_root_queue.popleft()
children_count = 0

pathFound = False # flag to check if path was found

while search_queue: # while queue is not empty
    country = search_queue.popleft()

    if children_count is parent_children_num:
        parent_root = parent_root_queue.popleft()
        parent_children_num = len(graph[parent_root])
        children_count = 0

    children_count += 1

    if not country in searched_list:
        print('searching ' + country)
        path_dict[country] = parent_root
        parent_root_queue.append(country)
        if country == destination:
            print('Path found between ' + origin + ' and ' + destination)
            pathFound = True
            break
        else:
            search_queue += graph[country]
            searched_list.append(country)
    
if pathFound is False:
    print('No path found between ' + origin  + ' and ' + destination + ' , sorry!')

if pathFound is True:
    path_array = []
    country_stop = destination

    while True:
        path_array.append(country_stop)
        if country_stop is origin:
            break
        country_stop = path_dict[country_stop]

    path_array.reverse()
    final_path_string = ' -> '.join(path_array)
    print(final_path_string)








