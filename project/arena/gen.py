from models import Arena
from pathfind import bfs, traverse
import util
import json

with open("./arena_megadict.json") as f:
    mega_dict = json.load(f)
    mega_dict = util.clean_tree_dict(mega_dict)

arena = Arena(data=mega_dict)  # Make arena
v = arena.vertices

# for i in v:
#     print ("{} : {}".format(i, v[i]))

source = v.get_node(10, 180)
d1 = v.get_node(13, 120)
d2 = v.get_node(13, 300)

x1 = bfs(v, source, d1)
print(x1)
t1 = traverse(x1, 0, "p")
print(t1)
