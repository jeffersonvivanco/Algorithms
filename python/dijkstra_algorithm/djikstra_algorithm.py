
# implementing the graph hash table
# we need to store the neighbors of a node and the cost for getting to that neighbor
# To represent the weight of those edges, we'll use another hash table
graph = {}

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {} # The finish node doesn't have any neighbors

# the costs hash table, we use infinity when we don't know the costs yet
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# parents hash table
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = [] # array to keep track all nodes already processed

# function to find the lowest cost node
def find_the_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs: # go through each node
        cost = costs[node]
        print(node)
        if cost < lowest_cost and node not in processed: # if it's the lowest cost so far and hasn't been processed yet
            lowest_cost = cost # set it as the new lowest-cost node
            lowest_cost_node = node

    return lowest_cost_node

# algorithm
node = find_the_lowest_cost_node(costs) # find the lowest-cost node that you haven't processed yet
while node is not None: # if you have processed all the nodes, this while loop is done
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # go through all the neighbors of this node
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: # if it's cheaper to get to this neighbor by going through this node ...
            costs[n] = new_cost # ... update the cost for this node
            parents[n] = node # this node becomes the new parent for this neighbor
    processed.append(node)
    node = find_the_lowest_cost_node(costs)