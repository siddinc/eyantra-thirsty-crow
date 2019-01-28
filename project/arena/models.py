DIRECTION_MAPPING = {
    "1-1": (60, 240), 
    "2-2": (0, 180), 
    "3-3": (120, 300)
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
        return "<Node pos={}>".format(str(self.pos))

    def __hash__(self):
        return hash(tuple(sorted(self.pos.items())))


class NodeDict(dict):
    def __init__(self, *arg, **kwargs):
        super(NodeDict, self).__init__(*arg, **kwargs)

    def get_node(self, hex_no, angle):
        for n in self.keys():  # Loop over all arena nodes
            if hex_no in n.pos.keys():  # Get the node which contains the hex number
                if n.pos[hex_no] == angle:  # If the node is at that angle for the hex
                    return n


class Arena:
    def __init__(self, data={}):
        self.hexes = {}
        if data:
            self.add(data=data)

    def add(self, data):
        self.hexes = {**self.hexes, **data}

    @property
    def vertices(self):
        nodes = NodeDict()

        # Make nodes and add positions.
        for h in self.hexes:
            for v in VERTEX_ANGLES:
                n = Node()
                n.add(h, v)
                # Get the hexes in viscinity
                hex_visc = [get_viscinity(v, -30), get_viscinity(v, +30)]
                # Get vertices in viscinity
                vert_visc = [
                    get_viscinity(inverse_angle(hex_visc[0]), -30),
                    get_viscinity(inverse_angle(hex_visc[1]), +30),
                ]
                # Check adjoining hexes
                for i, vhex in enumerate(hex_visc):
                    if vhex in self.hexes[h]:  # If there is a hex at angle vhex
                        adj_hex = self.hexes[h][vhex]  # Get hex number
                        adj_vertex = vert_visc[i]  # Get vertex
                        n.add(adj_hex, adj_vertex)  # Add to node parameters
                nodes[n] = []

        # Add links.
        for n in nodes:
            s = set()
            for h, a in n.pos.items():  # Loop over all the hexes node is connected to
                adj_node = nodes.get_node(
                    h, (a + 60) % 360
                )  # Get the node 60degrees after this node
                s.add(adj_node)  # Add to adjacency dictionary
                adj_node = nodes.get_node(
                    h, (a - 60 + 360) % 360
                )  # Get the node 60degrees before this node
                s.add(adj_node)  # Add to adjacency dictionary
                nodes[n] = list(s)

        return nodes
