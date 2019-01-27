import collections


arena_config = {0: (“Water Pitcher”, 5, “2-2”), 1: (“Pebble”, 3, “1-1”), 2: (“Pebble”, 11, “3-3”), 3: (“Pebble”, 13, “2-2”)}
pebble_spots = []
water_spot = []

for key, value in arena_config.items():
    if value[0] == "Water Pitcher":
        water_spot.append([value[1], value[2]])

    elif value[0] == "Pebble":
        pebble_spots.append([value[1], value[2]])

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
    1: [[27, 38], [28, 37], [26, 39]],      #: [[1-1], [2-2], [3-3]]
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


def bfs(graph, source, destination):  # returns a list of nodes in shortest path to traverse
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


# returns shortest path out of 2 paths for diagonally opposite nodes
def path_generate(robot_source, robot_destination):
    #robot_destination = [cell_no, orientation]
    if robot_destination[1] == "1-1":
        path1 = bfs(graph, robot_source,
                    orientation[robot_destination[0]][0][0])
        path2 = bfs(graph, robot_source,
                    orientation[robot_destination[0]][0][1])

    elif robot_destination[1] == "2-2":
        path1 = bfs(graph, robot_source,
                    orientation[robot_destination[0]][1][0])
        path2 = bfs(graph, robot_source,
                    orientation[robot_destination[0]][1][1])

    else:
        path1 = bfs(graph, robot_source,
                    orientation[robot_destination[0]][2][0])
        path2 = bfs(graph, robot_source,
                    orientation[robot_destination[0]][2][1])

    if len(path1) < len(path2):
        final_path = path1
    else:
        final_path = path2
    return final_path


def water_pitcher_zone(water_spot):
    if water_spot[0][1] == "1-1":


def current_node_visit():


def traverse(final_path):
    # motor functions


def pickup():
    # pickup functions


def drop():
    # drop functions

def left():
    print ('robot moved lieft')


def task():
    # assuming that each pebble zone has only 1 pebble for simplicity
    length = len(pebble_spots)
    robot_start = 1  # 1 start1 or 56 for start2
    pebble_zone = pebble_spots.pop(0)
    while(length > 0):  # till all pebble zones not visited
        road = path_generate(robot_start, pebble_zone)
        traverse(road)
        pickup()
        robot_start = pebble_zone
        road = path_generate(robot_start, water_spot[0])
        traverse(road)
        drop()
        robot_start = water_pitcher_zone()  # water pitcher location
        pebble_zone = pebble_spots.pop(0)  # next pebble zone location
        length -= 1

        '''
        generate path from start1 or start2 to 1st pebble zone
        go to that pebble zone
        pickup pebble
        set that pebble zone as robot_start and water pitcher as destination
        generate path from new robot_start to water pitcher
        go to the water pitcher
        drop pebble
        set water pitcher as robot_start and destination new pebble zone
        generate path and go to new pebble zone... and loop over

        '''
