DIRECTION_MAPPING = {
    '1-1': (60, 240),
    '2-2': (0, 180),
    '3-3': (120, 300),
}

VERTEX_ANGLES = [0, 60, 120, 180, 240, 300]

def get_viscinity(angle, offset):
    return (angle + offset + 360) % 360

def inverse_angle(angle):
    return (angle + 180) % 360

class Node:
    def __init__(self):
        self.pos = {}

    def add(self, number, angle):
        self.pos[number] = angle

    def __str__(self):
        return str(self.pos)

    def __repr__(self):
        return "<Node pos={}>".format(self.pos)

    def __hash__(self):
        return hash(tuple(sorted(self.pos.items())))

    def __eq__(self, other):
        return self.pos == other.pos


class Arena:
    def __init__(self, data={}):
        self.hexes = {}
        if data:
            self.add(data=data)

    def add(self, data):
        self.hexes = { **self.hexes, **data }

    def get_vertices(self):
        nodes = {}

        # Make nodes and add positions.
        for h in self.hexes:
            for v in VERTEX_ANGLES:
                n = Node()
                n.add(h, v)
                # Get the hexes in viscinity
                hex_visc = [get_viscinity(v, -30), get_viscinity(v, +30)]
                # Get vertices in viscinity
                vert_visc = [get_viscinity(inverse_angle(hex_visc[0]), -30), get_viscinity(inverse_angle(hex_visc[1]), +30)]
                # Check adjoining hexes
                for i, vhex in enumerate(hex_visc):
                    if vhex in self.hexes[h]: # If there is a hex at angle vhex
                        adj_hex = self.hexes[h][vhex] # Get hex number
                        adj_vertex = vert_visc[i] # Get vertex
                        n.add(adj_hex, adj_vertex)
                nodes[n] = []
        
        # Add links.
        for node in nodes:
            root_hex = list(node.pos.keys())[0]
            angle = node.pos[root_hex]
            visc = [get_viscinity(root_hex, -60), get_viscinity(root_hex, +60)]
            adj_nodes = list(filter(lambda h: root_hex in list(h.pos), nodes))
            print("{} adj = {}".format(node, adj_nodes))
            print ("***")
        
        return nodes
    
    def __str__(self):
        return "\n".join(["{}: {}".format(n, neighs) for n, neighs in self.hexes.items()])
    
    def __repr__(self):
        return "<Arena nodes={}>".format(len(self.hexes))
