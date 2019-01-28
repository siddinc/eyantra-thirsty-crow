from queue import Queue
from math import cos, sin, atan2, radians, degrees
import numpy as np
import logging


#######################################################
#######################################################
#######################################################


def to_vec(angle):
    return np.array([cos(radians(angle)), sin(radians(angle)), 0])


#######################################################
#######################################################
#######################################################


def reconstruct_path(came_from, start, goal):  # returns a list of nodes to traverse
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path


def bfs(graph, source, destination):
    frontier = Queue()
    frontier.put(source)
    came_from = {}
    came_from[source] = None

    while not frontier.empty():
        current = frontier.get()

        if current == destination:
            break

        for n in graph[current]:
            if n not in came_from:
                frontier.put(n)
                came_from[n] = current
    return reconstruct_path(came_from, source, destination)


#######################################################
#######################################################
#######################################################


def traverse(path, orientation, mode):
    if mode is not "p" and mode is not "d":
        return ValueError(r"Mode must be pickup 'p' or drop 'd'.")

    commands = list()

    path.append(0)
    pairs = list(
        zip(path, path[1:])
    )  # Make pairs of source and destination, consecutive elements.

    for source, destination in pairs:
        if destination == 0:
            commands.append(mode)
            break

        common_node = [key for key in source.pos if key in destination.pos][0]
        svec = to_vec(source.pos[common_node])
        dvec = to_vec(destination.pos[common_node])

        direction_vec = np.subtract(dvec, svec)
        robot_vec = to_vec(orientation)

        new_orientation = degrees(atan2(direction_vec[1], direction_vec[0]))
        screw_vec = np.cross(robot_vec, direction_vec)

        print ("DEBUG {} to {}".format(source, destination))
        print ("ORIENTATION {} VECTOR {}".format(int(orientation), to_vec(orientation)))
        print ("DIRECTION VECTOR {}".format(direction_vec))
        print ("SCREW VECTOR {}".format(screw_vec))
        print ("COMMAND {}".format('l' if screw_vec[2] > 0 else 'r'))

        print("\n")

        if screw_vec[2] > 0:
            commands.append("l")
        else:
            commands.append("r")
        orientation = new_orientation

    return commands, orientation
