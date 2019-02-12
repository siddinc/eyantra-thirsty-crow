from math import cos, sin, radians
import numpy as np


def to_vec(angle):
    """ Convert an angle to a 3D vector. """
    return np.array([cos(radians(angle)), sin(radians(angle)), 0])


def positive_angle(angle):
    """ Takes an angle and returns the positive value of the angle. """
    return (angle + 360) % 360


def get_viscinity(angle, offset):
    """ Return the angles in viscinity of this angle. """
    return (angle + offset + 360) % 360


def inverse_angle(angle):
    """ Returns the inverse of the angle. """
    return (angle + 180) % 360
