from queue import Queue
from math import cos, sin, atan, radians, degrees
import numpy as np


def to_vec(angle):
    return np.array([cos(radians(angle)), sin(radians(angle)), 0])

def cross(avec, bvec):
    """ Return cross product of 2 vectos in angle representations. """
    cvec = np.cross(avec, bvec)
    return cvec

def get_node_dir_vec(avec, bvec):
    """ Return the vector originating from a to b. """
    cvec = np.subtract(bvec, avec)
    return cvec

def angle(v1, v2, acute=True):
    """ v1 is your firsr vector
    v2 is your second vector """
    
    angle = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
    if (acute == True):
        return degrees(angle)
    else:
        return degrees(2 * np.pi - angle)


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

        for next in graph[current]:
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    return reconstruct_path(came_from, source, destination)


#######################################################
#######################################################
#######################################################


def traverse(path, orientation, mode):
    if mode is not 'p' and mode is not 'd':
        return ValueError(r"Mode must be pickup 'p' or drop 'd'.")

    commands = list()

    path.append(0)
    pairs = list(zip(path, path[1:])) # Make pairs of source and destination, consecutive elements.

    for source, destination in pairs:
        if destination == 0:
            commands.append(mode)
            break
        
        common_node = [key for key in source.pos if key in destination.pos][0]
        svec = to_vec (source.pos[common_node])
        dvec = to_vec (destination.pos[common_node])

        dir_vec = get_node_dir_vec(svec, dvec)
        new_orientation = atan(dir_vec[1]/dir_vec[0])

        v = cross(to_vec(orientation), dir_vec)

        if v[2] > 0:
            commands.append('l')
        else:
            commands.append('r')
        orientation = new_orientation

    return commands
