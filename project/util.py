def clean_tree_dict(d):
    d = dict(zip(map(int, d.keys()), d.values()))
    for k, v in d.items():
        if type(v) is dict:
            d[k] = clean_tree_dict(v)
    return d
