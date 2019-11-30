import numpy as np
import argparse
import cv2
from matplotlib import pyplot as plt

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])


# BGR to GRAY
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(gray)
cv2.imshow("Normal and Equilized",np.hstack([gray, eq]))
cv2.waitKey(0)

plt.figure()
plt.title("Grayscale Histogram")

hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.plot(hist, color='r')

hist = cv2.calcHist([eq], [0], None, [256], [0, 256])
plt.plot(hist, color='b')
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)