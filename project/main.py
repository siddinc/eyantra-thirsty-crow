from arena.models import Arena, DIRECTION_MAPPING
from arena.pathfind import bfs, traverse
from xbee import send_xbee, read_xbee_forever
from threading import Thread
import util
import json


# ARENA CONFIGURATION

# CONFIG 1
arena_config = {
    0: ("Water Pitcher", 8, "2-2"),
    1: ("Pebble", 13, "3-3")
}
Robot_start = "START-2"

# CONFIG 2
# arena_config = {
#     0: ('Water Pitcher', 9, '2-2'),
#     1: ('Pebble', 2, '2-2'),
# }
# Robot_start = 'START-2'


# UTILITY FUNCTIONS

# v: Vertices
v = None

# Thread for listening to serial
xbee_thread = Thread(target=read_xbee_forever)

def get_vertices():
    with open("./arena/arena_megadict.json") as f:
        mega_dict = json.load(f)
        mega_dict = util.clean_tree_dict(mega_dict)

    arena = Arena(data=mega_dict)  # Make arena
    return arena.vertices


def get_pebble_nodes(pebble_list):
    nodes = list()
    for hex_no, direction in pebble_list:
        for i in range(2):
            n = v.get_node(hex_no, DIRECTION_MAPPING[direction][i])
            n.hex_no = hex_no
            n.angle = DIRECTION_MAPPING[direction][i]
            nodes.append(n)
    return nodes

def get_direction_nodes(h, d):
    global v
    return [v.get_node(h, DIRECTION_MAPPING[d][0]), v.get_node(h, DIRECTION_MAPPING[d][1])]


# STARTING POINT

def main():
    global v
    v = get_vertices()

    if Robot_start == "START-1":
        source = v.get_node(10, 180)
        orientation = 0
    else:
        source = v.get_node(14, 0)
        orientation = 180

    pitcher_hex = next((v[1], v[2]) for _, v in arena_config.items() if v[0] == "Water Pitcher")
    pitcher_nodes = get_direction_nodes(*pitcher_hex)
    pebble_list = [(v[1], v[2]) for k, v in arena_config.items() if v[0] == "Pebble"]

    to_send = []

    xbee_thread.start()

    while pebble_list:
        pebble_node_list = get_pebble_nodes(pebble_list)
        paths = map(lambda n: bfs(v, source, n), pebble_node_list)
        best_path = min(paths, key=lambda e: len(e))
        t, orientation = traverse(best_path, orientation, "p")
        print (best_path)
        print (t)
        to_send = t
        pebble_list.pop()

    for c in to_send:
        print ("Sent {}".format(c))
        send_xbee(c)
    


if __name__ == "__main__":
    main()