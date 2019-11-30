from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])


# BGR to GRAY
channels = cv2.split(image)
colors = ('b', 'g', 'r')

plt.figure()
plt.title("Flattned Color Histogram")
# create the histogram

for (channel, color) in zip(channels, colors):
	hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
	plt.plot(hist, color=color)
	plt.xlim([0, 256])

plt.show()

cv2.waitKey(0)