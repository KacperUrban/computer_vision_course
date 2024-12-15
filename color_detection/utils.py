import cv2
import numpy as np
from typing import Union

def get_limits(color: list) -> Union[np.array, np.array]:
    """Function convert color in BGR to HSV and then calculate upper and lower limit for this color.

    Args:
        color (list): Color in BGR format, for example [0, 255, 255] -> yellow in BGR

    Returns:
        Union[np.array, np.array]: upper and lower limit for ceratin color
    """

    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    hue = int(hsvC[0][0][0])  # Convert to standard Python int to handle arithmetic safely

    # Handle red hue wrap-around for cyclic nature of HSV
    if hue >= 165:  # Upper limit for divided red hue
        lowerLimit = np.array([hue - 7, 125, 125], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for divided red hue
        lowerLimit = np.array([0, 125, 125], dtype=np.uint8)
        upperLimit = np.array([hue + 7, 255, 255], dtype=np.uint8)
    else:  # For other colors
        lowerLimit = np.array([hue - 7, 125, 125], dtype=np.uint8)
        upperLimit = np.array([hue + 7, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit