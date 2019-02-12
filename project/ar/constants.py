""" 
* Team Id : 5377
* Author List : Vikrant Gajria
* Filename: aruco.py
* Theme: TC -- Specific to eYRC
* Functions: get_camera_params (str)
* Global Variables: marker_length, INVERSE_MATRIX
"""
import numpy as np


# marker_length: Length of aruco marker in meters.
marker_length = 100

# Matrix to convert OpenCV coordinates to OpenGL system.
INVERSE_MATRIX = np.array(
    [
        [+1.0, +1.0, +1.0, +1.0],
        [-1.0, -1.0, -1.0, -1.0],  # Inverts Y axis
        [-1.0, -1.0, -1.0, -1.0],  # Inverts Z axis
        [+1.0, +1.0, +1.0, +1.0],
    ]
)
