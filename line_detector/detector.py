import cv2 as cv
import numpy as np


def line_detector(image, options=None):
    origin = cv.imread(image)
    img = cv.cvtColor(origin, cv.COLOR_BGR2GRAY)
    img = cv.GaussianBlur(img, (3, 3), 0)

    img = cv.fastNlMeansDenoising(img, None, 21, 5, 21)

    edges = cv.Canny(img, 50, 150, apertureSize=3)
    lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=0, maxLineGap=10)

    height, width, _ = origin.shape

    return {
        "lines": lines,
        "shape": {
            "height": height,
            "width": width
        }
    }
