''' 
* Team Id : 5377
* Author List : Vikrant Gajria
* Filename: aruco.py
* Theme: TC -- Specific to eYRC
* Functions: detect_markers(PIL.Image)
* Global Variables: NONE
'''
import cv2
import cv2.aruco as aruco
from constants import marker_length


'''
* Function Name: detect_markers
* Input: img (numpy.array)
* Output: aruco list in the form 
*        [(aruco_id_1, centre_1, rvec_1, tvec_1),
*        (aruco_id_2, centre_2, rvec_2, tvec_2), 
*        ()...]
* Logic: This function takes the image in form of a numpy array, camera_matrix and
*        distortion matrix as input and detects ArUco markers in the image. For each
*        ArUco marker detected in image, paramters such as ID, centre coord, rvec
*        and tvec are calculated and stored in a list in a prescribed format. The list
*        is returned as output for the function
* Example Call: detect_markers(frame)
'''
def detect_markers(img):
    # aruco_list: Return value
    aruco_list = []

    # Grayscale the image.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Initialise aruco library.
    aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
    parameters = aruco.DetectorParameters_create()

    # Detect the markers as per the parameters.
    corners, ids, _ = aruco.detectMarkers(
        gray, aruco_dict, parameters=parameters)

    # Execute only if the above function returns something.
    if type(ids) == np.ndarray:
        for i in range(len(ids)):
            rvec, tvec, _ = aruco.estimatePoseSingleMarkers(
                corners[i], marker_length, camera_matrix, dist_coeff)

            cornersx = [r[0] for r in tuple(corners[i][0])]
            cornersy = [r[1] for r in tuple(corners[i][0])]
            centre = tuple(map(int, (sum(cornersx) // 4, sum(cornersy) // 4)))

            aruco_list.append((ids[i][0], centre, rvec, tvec))

    return aruco_list
