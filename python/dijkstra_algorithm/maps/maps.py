import random

# costs hash table, we use infinity when we don't know the cost yet
global infinity
infinity = float('inf')

class Maps():

    def __init__(self, map):
        self.map = map
        # map names stored used for notifications
        self.map_names = {}
        for k in self.map.keys():
            self.map_names[k] = k.replace('_', ' ').title()
        # notifications store
        self.notifications = []
        self.choice_table = self._setup_choice_table()
        self.costs = {}
        self.parents = {}
        self.processed = []

    # assigns random values to maps edges values (aka distance between nodes/places)
    def determine_time(self):
        for m in self.map.keys():
            for n in self.map[m].keys():
                time = random.randint(0, 120)
                message = self._get_traffic_message(m, n, time)
                self.notifications.append(message)
                self.map[m][n] = time

    # returns the traffic message (notifications) to display in the console
    def _get_traffic_message(self, origin, dest, t):
        if t < 30:
            message = 'Pathway is clear between {o} and {d}. Time estimate: {t} seconds'
            return message.format(o=self.map_names[origin], d=self.map_names[dest], t=t)
        elif t < 60:
            message = 'Light traffic between {o} and {d}. Time estimate: {t} seconds'
            return message.format(o=self.map_names[origin], d=self.map_names[dest], t=t)
        elif t < 90:
            message = 'There is traffic between {o} and {d}. Time estimate: {t} seconds'
            return message.format(o=self.map_names[origin], d=self.map_names[dest], t=t)
        else:
            message = 'There is heavy traffic between {o} and {d}. Time estimate: {t} seconds'
            return message.format(o=self.map_names[origin], d=self.map_names[dest], t=t)

    # prints and returns the choice table to help the user choose an origin and destination
    def _setup_choice_table(self):
        index = 0
        choice_table = {}
        for place_key in self.map_names.keys():
            choice_table[index] = place_key
            index += 1
        return choice_table

    # sets up costs and parents hash table
    def setup_costs_and_parents_table(self, origin, dest):
        self.origin = origin
        self.dest = dest
        # setting up parents
        for n in self.map[origin]:
            self.parents[n] = origin

        # setting up dest parent
        # origin and destination could be close to each other, so in that case we leave it
        # cause we have a parent but we don't know if it has the lowest cost
        if dest not in self.parents.keys():
            self.parents[dest] = None

        # setting up costs
        for n in self.map[origin]:
            self.costs[n] = self.map[origin][n]

        # setting up dest cost
        # same explanation as parents
        if dest not in self.costs.keys():
            self.costs[dest] = infinity

    def _find_the_lowest_cost_node(self):
        lowest_cost = infinity
        lowest_cost_node = None
        for node in self.costs:
            cost = self.costs[node]
            if cost < lowest_cost and node not in self.processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def run_dijkstra_algorithm(self):

        node = self._find_the_lowest_cost_node()

        while node != None and node != self.dest:
            cost = self.costs[node]
            neighbors = self.map[node]
            for n in neighbors:
                new_cost = cost + neighbors[n]
                if n not in self.costs.keys():
                    self.costs[n] = infinity
                if new_cost < self.costs[n]:
                    self.costs[n] = new_cost
                    self.parents[n] = node
            self.processed.append(node)
            node = self._find_the_lowest_cost_node()

        return self._get_path()

    def _get_path(self):
        temp = self.dest
        path = [self.dest]
        while True:
            temp = self.parents[temp]
            path.append(temp)
            if temp == self.origin:
                break
        path.reverse()
        path = [self.map_names[p] for p in path]
        self.path = ' -> '.join(path);
        return self.path
