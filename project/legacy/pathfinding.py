import collections

graph = {
    1: [2],
    2: [1, 5, 6],
    3: [4, 10],
    4: [3, 5],
    5: [2, 4, 12],
    6: [2, 7, 14],
    7: [6, 8],
    8: [7, 16],
    9: [10, 19],
    10: [3, 9, 11],
    11: [10, 12, 21],
    12: [5, 11, 13],
    13: [12, 14, 23],
    14: [6, 13, 15],
    15: [14, 16, 25],
    16: [8, 15, 17],
    17: [16, 27],
    18: [19, 29],
    19: [9, 18, 20],
    20: [19, 21, 31],
    21: [11, 20, 22],
    22: [21, 23, 33],
    23: [13, 22, 24],
    24: [23, 25, 35],
    25: [15, 24, 26],
    26: [25, 27, 37],
    27: [17, 26, 28],
    28: [27, 39],
    29: [18, 30],
    30: [29, 31, 40],
    31: [20, 30, 32],
    32: [31, 33, 42],
    33: [22, 32, 34],
    34: [33, 35, 44],
    35: [24, 34, 36],
    36: [35, 37, 46],
    37: [26, 36, 38],
    38: [37, 39, 48],
    39: [28, 38],
    40: [30, 41],
    41: [40, 42, 49],
    42: [32, 41, 43],
    43: [42, 44, 51],
    44: [34, 43, 45],
    45: [44, 46, 53],
    46: [36, 45, 47],
    47: [46, 48, 55],
    48: [38, 47],
    49: [41, 50],
    50: [49, 51],
    51: [43, 50, 52],
    52: [51, 53, 56],
    53: [45, 52, 54],
    54: [53, 55],
    55: [47, 54],
    56: [52],
}

orientation = {
    1: [[27, 38], [28, 37], [26, 39]],  #: [[1-1], [2-2], [3-3]]
    2: [[16, 26], [17, 25], [15, 27]],
    3: [[25, 36], [26, 35], [24, 37]],
    4: [[37, 47], [38, 46], [36, 48]],
    5: [[7, 15], [8, 14], [6, 16]],
    6: [[14, 24], [15, 23], [13, 25]],
    7: [[23, 34], [24, 33], [22, 35]],
    8: [[35, 45], [36, 44], [34, 46]],
    9: [[46, 54], [47, 53], [45, 55]],
    10: [[2, 13], [6, 12], [5, 14]],
    11: [[12, 22], [13, 21], [11, 23]],
    12: [[21, 32], [22, 31], [20, 33]],
    13: [[33, 44], [34, 42], [32, 44]],
    14: [[44, 52], [45, 51], [43, 53]],
    15: [[4, 11], [5, 10], [3, 12]],
    16: [[10, 20], [11, 19], [9, 21]],
    17: [[19, 30], [20, 29], [18, 31]],
    18: [[31, 41], [32, 40], [30, 42]],
    19: [[42, 50], [43, 49], [41, 51]],
}


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


def reconstruct_path(came_from, start, goal):  # returns a list of nodes to traverse
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path


def bfs(
    graph, source, destination
):  # returns a list of nodes in shortest path to traverse
    frontier = Queue()
    frontier.put(source)
    came_from = {}
    came_from[source] = None

    while not frontier.empty():
        current = frontier.get()

        if current == destination:
            break

        for next in graph[current]:
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    return reconstruct_path(came_from, source, destination)


path1 = bfs(graph, 1, 34)
path2 = bfs(graph, 1, 42)

if len(path1) < len(path2):
    final_path = path1
else:
    final_path = path2

print(path1)
print(path2)
print(final_path)
