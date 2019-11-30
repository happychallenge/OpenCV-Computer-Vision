import face_recognition as face
from PIL import Image, ImageDraw
import cv2
import numpy as np

# This is an example of running face recognition on a single image
# and drawing a box around each person that was identified.

# Load a sample picture and learn how to recognize it.
obama_image = face.load_image_file("obama.jpg")
obama_face_encoding = face.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face.load_image_file("biden.jpg")
biden_face_encoding = face.face_encodings(biden_image)[0]

namju_image = face.load_image_file("namju.jpg")
namju_face_encoding = face.face_encodings(namju_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding,
    namju_face_encoding,
]
known_face_names = [
    "Barack Obama",
    "Joe Biden",
    "NAMJU YOON",
]

# Load an image with an unknown face
origin = face.load_image_file("three-people.jpg")

face_locations = face.face_locations(origin)
face_encodings = face.face_encodings(origin, face_locations)

for face_encode in face_encodings:
    face_distance = face.face_distance(known_face_encodings, face_encode)
    min_value = min(face_distance)
    name = "Unknown"
    if min_value < 0.5:
        index = np.argmin(face_distance)
        name = known_face_names[index]
    
    print("Distance {:.2}, Matching Name : {}".format(min_value, name))

