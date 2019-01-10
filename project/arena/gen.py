from models import Arena
import json
import util

with open('./arena_megadict.json') as f:
    mega_dict = json.load(f)
    mega_dict = util.clean_tree_dict(mega_dict)

arena = Arena(data=mega_dict)
print (arena)
