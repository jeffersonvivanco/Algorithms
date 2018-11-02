from maps import Maps
import unittest


class MapsTestCase(unittest.TestCase):

    # setting up a map with values (all same for testing adjacent places)
    # these values are used to check if Maps's dijkstra algorithm
    # is running correctly
    # some of these values are changed via functions that start with _set_map.*
    def setUp(self):
        map = {}

        map['central_park'] = {}
        map['central_park']['times_square'] = 10

        map['times_square'] = {}
        map['times_square']['union_square'] = 10

        map['union_square'] = {}
        map['union_square']['nyu_washington_sq_pk'] = 10
        map['union_square']['brooklyn_bridge'] = 10
        map['union_square']['east_river'] = 10

        map['nyu_washington_sq_pk'] = {}
        map['nyu_washington_sq_pk']['battery_park'] = 10

        map['battery_park'] = {}
        map['battery_park']['brooklyn_bridge'] = 10

        map['east_river'] = {}
        map['east_river']['brooklyn_bridge'] = 10

        map['brooklyn_bridge'] = {}
        map['brooklyn_bridge']['one_world_trade_center'] = 10

        # the finish node does not have any neighbors
        map['one_world_trade_center'] = {}
        self.map_engine = Maps(map)


    def test_adjacent_places(self):
        for p in self.map_engine.map.keys():
            for k in self.map_engine.map[p]:
                self.map_engine.setup_costs_and_parents_table(p, k)
                path = self.map_engine.run_dijkstra_algorithm()
                p_name = p.replace('_', ' ').title()
                k_name = k.replace('_', ' ').title()
                self.assertEqual(path, '{p} -> {k}'.format(p=p_name, k=k_name))

    def test_shorter_time(self):
        # setting long times to force the algorithm to take a shorter path
        self.map_engine.map['union_square']['brooklyn_bridge'] = 1000
        self.map_engine.map['union_square']['east_river'] = 1000
        self.map_engine.setup_costs_and_parents_table('union_square', 'brooklyn_bridge')
        path = self.map_engine.run_dijkstra_algorithm()
        self.assertEqual(path, 'Union Square -> Nyu Washington Sq Pk -> Battery Park -> Brooklyn Bridge')

    def test_shorter_time2(self):
        self.map_engine.map['union_square']['nyu_washington_sq_pk'] = 1000
        self.map_engine.map['union_square']['brooklyn_bridge'] = 1000
        self.map_engine.setup_costs_and_parents_table('central_park', 'one_world_trade_center')
        path = self.map_engine.run_dijkstra_algorithm()
        self.assertEqual(path, 'Central Park -> Times Square -> Union Square -> East River -> Brooklyn Bridge -> One World Trade Center')

    def test_regular_time(self):
        # check1
        self.map_engine.setup_costs_and_parents_table('union_square', 'brooklyn_bridge')
        path = self.map_engine.run_dijkstra_algorithm()
        self.assertEqual(path, 'Union Square -> Brooklyn Bridge')

        # check2
        self.map_engine.setup_costs_and_parents_table('union_square', 'one_world_trade_center')
        path = self.map_engine.run_dijkstra_algorithm()
        self.assertEqual(path, 'Union Square -> Brooklyn Bridge -> One World Trade Center')

        # check3
        self.map_engine.setup_costs_and_parents_table('central_park', 'one_world_trade_center')
        path = self.map_engine.run_dijkstra_algorithm()
        self.assertEqual(path, 'Central Park -> Times Square -> Union Square -> Brooklyn Bridge -> One World Trade Center')













