import numpy as np
import argparse
import imutils
import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
#cv2.waitKey(0)

# print("max of 255 by cv2: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
# print("min of 0 by cv2: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

# print("wrap of max by np: {}".format(np.uint8([200])+np.uint8([100])))
# print("wrap of min by np: {}".format(np.uint8([50])-np.uint8([100])))


#define color
#draw the line
#arguments are canvas/image, starting point, ending point, color, thickness(optional)
#display in cv2 window
canvas = np.ones(image.shape, dtype="uint8") * 100
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)

# draw line with width
red = (0,0,255)
cv2.line(canvas,(300,0),(0,300),red, 3)

#draw rectangles
blue = (255, 0,0)
cv2.rectangle(canvas,(30,30),(270,270),blue)
cv2.rectangle(canvas,(10,10),(60,60),red, 3)
cv2.rectangle(canvas,(210,210),(260,260),blue, -1)
added = cv2.add(image, canvas)
cv2.imshow("Added image", added)


#generating one array and multiplying it with 50
#substracting that array to the actual image numpy array
subtracted = cv2.subtract(image, canvas)
cv2.imshow("Subtracted image", subtracted)

cv2.waitKey(0)








