from maps import Maps
from maps_exception import MapsException

# implementing the graph hash table
# we store all the neighbors and the cost for getting to that neighbor (weight of the edges)

map = {}

map['central_park'] = {}
map['central_park']['times_square'] = None

map['times_square'] = {}
map['times_square']['union_square'] = None

map['union_square'] = {}
map['union_square']['nyu_washington_sq_pk'] = None
map['union_square']['brooklyn_bridge'] = None
map['union_square']['east_river'] = None

map['nyu_washington_sq_pk'] = {}
map['nyu_washington_sq_pk']['battery_park'] = None

map['battery_park'] = {}
map['battery_park']['brooklyn_bridge'] = None

map['east_river'] = {}
map['east_river']['brooklyn_bridge'] = None

map['brooklyn_bridge'] = {}
map['brooklyn_bridge']['one_world_trade_center'] = None

# the finish node does not have any neighbors
map['one_world_trade_center'] = {}

map_engine = Maps(map)

# determining time between places
map_engine.determine_time()

print('\nNotifications:\n')
for n in map_engine.notifications:
    print(n)

# printing out choice table
print('\nChoice Table\n')
for k in map_engine.choice_table.keys():
    print('{k} : {v}'.format(k=k, v=map_engine.choice_table[k]))

# Getting user input (origin and destination)
print('\nUse the numbers above to indicate your origin and destination\n')

origin = input('Please type the number for your origin (0 - 7)\n')
destination = input('Please type the number for destination (0 - 7)\n')

# Converting user input to number
try:
    origin_int = int(origin)
    dest_int = int(destination)
    if origin_int > dest_int:
        raise MapsException('Destination number has to be greater than origin number, please run again')
    if origin_int in range(3, 5) and dest_int == 5:
        raise MapsException('Currently Maps does not work where origin is either NYU Washting Sq Park or Battery Park and dest is East River or vice versa')
    origin = map_engine.choice_table[int(origin)]
    destination = map_engine.choice_table[int(destination)]

except ValueError:
    print('You did not enter a number, please try again.')
    exit(1)
except KeyError:
    print('You entered a number out of scope of the choice table, please try again.')
    exit(1)
except MapsException as e:
    print(e.args[0])
    exit(1)


# set up parents and costs
map_engine.setup_costs_and_parents_table(origin, destination)


# run dijkstra algorithm to find the shortest path to your destination
print(map_engine.run_dijkstra_algorithm())

