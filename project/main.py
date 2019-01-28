from arena.models import Arena, DIRECTION_MAPPING
from arena.pathfind import bfs, traverse
import util
import json


# ARENA CONFIGURATION

# CONFIG 1
arena_config = {0: ("Water Pitcher", 8, "2-2"), 1: ("Pebble", 16, "1-1")}

Robot_start = "START-1"

# CONFIG 2
# arena_config = {
#     0: ('Water Pitcher', 9, '2-2'),
#     21: ('Pebble', 18, '2-2'),
#     2: ('Pebble', 2, '3-3'),
# }

# Robot_start = 'START-2'


# UTILITY FUNCTIONS


def get_vertices():
    with open("./arena/arena_megadict.json") as f:
        mega_dict = json.load(f)
        mega_dict = util.clean_tree_dict(mega_dict)

    arena = Arena(data=mega_dict)  # Make arena
    return arena.vertices


# STARTING POINT

if __name__ == "__main__":
    v = get_vertices()

    if Robot_start == "START-1":
        source = v.get_node(10, 180)
        orientation = 0
    else:
        source = v.get_node(14, 0)
        orientation = 180

    pitcher = arena_config[0]
    pebble = arena_config[1]

    pebble_nodes = [
        v.get_node(pebble[1], DIRECTION_MAPPING[pebble[2]][0]),
        v.get_node(pebble[1], DIRECTION_MAPPING[pebble[2]][1]),
    ]
    pitcher_nodes = [
        v.get_node(pitcher[1], DIRECTION_MAPPING[pitcher[2]][0]),
        v.get_node(pitcher[1], DIRECTION_MAPPING[pitcher[2]][1]),
    ]

    # To the pebble
    paths_to_pebble = list(map(lambda n: bfs(v, source, n), pebble_nodes))

    best_path = bfs(v, source, pebble_nodes[0])

    for i in paths_to_pebble:
        print(i, end="\n\n")

    if len(paths_to_pebble[0]) < len(paths_to_pebble[1]):
        best_path = paths_to_pebble[0]
    else:
        best_path = paths_to_pebble[1]

    t, orientation = traverse(best_path, orientation, "p")
    print(t)
