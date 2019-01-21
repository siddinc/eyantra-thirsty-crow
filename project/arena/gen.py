from models import Arena
import util
import json

with open('./arena_megadict.json') as f:
    mega_dict = json.load(f)
    mega_dict = util.clean_tree_dict(mega_dict)

arena = Arena(data=mega_dict) # Make arena
v = arena.vertices

for i in v:
    print ("{} : {}".format(i, v[i]))


