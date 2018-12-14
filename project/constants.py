''' 
* Team Id : 5377
* Author List : Vikrant Gajria
* Filename: aruco.py
* Theme: TC -- Specific to eYRC
* Functions: get_camera_params (str)
* Global Variables: marker_length, INVERSE_MATRIX
'''
import numpy as np


# marker_length: Length of aruco marker in meters.
marker_length = 14/100

# Matrix to convert OpenCV coordinates to OpenGL system.
INVERSE_MATRIX = np.array([[+1.0, +1.0, +1.0, +1.0],
                           [-1.0, -1.0, -1.0, -1.0], # Inverts Y axis
                           [-1.0, -1.0, -1.0, -1.0], # Inverts Z axis
                           [+1.0, +1.0, +1.0, +1.0]])

"""
Function Name : detect_markers()
Input: img (numpy array)
Output: aruco list in the form [(aruco_id_1, centre_1, rvec_1, tvec_1),(aruco_id_2,
        centre_2, rvec_2, tvec_2), ()....]
Purpose: This function takes the image in form of a numpy array, camera_matrix and
         distortion matrix as input and detects ArUco markers in the image. For each
         ArUco marker detected in image, paramters such as ID, centre coord, rvec
         and tvec are calculated and stored in a list in a prescribed format. The list
         is returned as output for the function
"""
def get_camera_params(npz_file='System.npz'):
    with np.load(npz_file) as X:
        camera_matrix, dist_coeff, _, _ = [X[i]
                                           for i in ('mtx', 'dist', 'rvecs', 'tvecs')]
        return camera_matrix, dist_coeff
