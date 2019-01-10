DIRECTION_MAPPING = {
    '1-1': (60, 240),
    '2-2': (0, 180),
    '3-3': (120, 300),
}

@DeprecationWarning
class Node:
    def __init__(self, number, neighbours):
        self.number = number
        self.neighbours = neighbours

class Arena:
    def __init__(self, data={}):
        self.nodes = {}
        if data:
            self.add(data=data)

    def add(self, number=0, neighbours={}, data={}):
        # If JSON is passed
        if data:
            self.nodes = { **self.nodes, **data }
            return

        if number not in self.nodes:
            self.nodes[number] = neighbours
        else:
            self.nodes[number] = {**self.nodes[number], **neighbours}

        for d, n in neighbours.items():
            if n not in self.nodes:
                self.nodes [n] = {
                    (d+180) % 360: number
                }
            elif number not in self.nodes [n]:
                self.nodes [n][(d+180) % 360] = number

    def remove(self, number):
        if number in self.nodes:
            del self.nodes[number]
    
    def __str__(self):
        return self.nodes.__str__()
    
    def __repr__(self):
        return "Arena<Nodes: {}>".format(len(self.nodes))
