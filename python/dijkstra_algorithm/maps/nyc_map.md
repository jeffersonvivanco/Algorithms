# NYC Map (Implemented using Dijkstra's Algorithm)

![Alt nyc map graph](nyc_maps.svg "Nyc Maps")

## Project
* Implemented a map covering only some parts of NYC using a graph.
* Using Dijkstra's algorithm, the program finds the fastest route to the destination.
* The fastest route is determined based on traffic and distance.
* The map only works uptown to downtown as shown by the arrows in the graph.
* To run the program, run nyc_map.py
* The project also comes with a test file -> nyc_map_test.py
* The program prints out notifications informing you how the traffic is
between places. Note: The time between places is in seconds because this map
is used in the future by flying cars who take seconds to get to places.

## Places
1. One World Trade Center
2. NYU (Washington Square Park)
3. Union Square
4. Central Park
5. Times Square
6. Brooklyn Bridge
7. Battery Park
8. East River

## Graph
* Weight of edges is determined based on distance and traffic. (Generated random at runtime)
* Nodes are the places

