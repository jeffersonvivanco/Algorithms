
# the set covering problem

# states I want to cover
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# list of stations choosing from
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

# final list of stations
final_stations = set()

# calculating answer
# you need to go through every station and pick the one that covers the most uncovered states

while states_needed:
    best_station = None

    states_covered = set() # is a set of all the states that this station covers that haven't been covered yet

    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station

        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    final_stations.add(best_station)
    # updating states needed. Because prev station covers some states, those states arent needed anymore
    states_needed -= states_covered

print('Final stations', final_stations)