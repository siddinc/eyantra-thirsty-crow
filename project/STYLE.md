<h1 align='center'>
    Python Coding Standard
</h1>
<h6 align='center'>
    For Thirsty Crow, e-Yantra theme
</h6>

## File level comments:
> In the beginning of all the files.

```python
''' 
* Team Id : 5377
* Author List : Vikrant Gajria, Manan Gandhi
* Filename: aruco.py
* Theme: TC -- Specific to eYRC
* Functions: detect_markers(PIL.Image), init_gl()
* Global Variables: marker_length, INVERSE_MATRIX
'''
import numpt as np
import cv2
...
```

## Function level comments:
> Before function definitions.

```python
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
    ...
    return aruco_list
```

## Variable level comments:
> Names should be descriptive enough; or if they require an explanation,
> use the following convention...

```python
# gray: Grayscaled image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

## Implementation detail comments:
> you should have comments in tricky, non‐obvious,
> interesting, or important parts of the code.

```python
# Megik
centre = tuple(map(int, (sum(cornersx) // 4, sum(cornersy) // 4)))
```

---

<blockquote align='center'>
“Any fool can write code that a computer can understand. Good programmers
write code that humans can understand.”<br> - Martin Fowler

“Programs must be written for people to read, and only incidentally for machines
to execute.”<br> - Hal Abelson & Gerald Jay Sussman

“Always code as if the guy who ends up maintaining your code will be a violent
psychopath who knows where you live.”<br> - Rick Osborne
</blockquote>
