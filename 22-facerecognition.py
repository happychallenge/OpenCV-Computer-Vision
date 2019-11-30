import face_recognition as face
from PIL import Image, ImageDraw
import cv2

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
guess_image = origin.copy()

# Find all the faces and face encodings in the unknown image
face_locations = face.face_locations(guess_image)
for (top, right, bottom, left) in face_locations:
    cv2.rectangle(guess_image, (left, top), (right, bottom), (255, 0, 0), 3)
cv2.imshow("Guess Image", guess_image)
cv2.waitKey(0)

face_landmarks_list = face.face_landmarks(origin)

pil_image = Image.fromarray(origin)
d = ImageDraw.Draw(pil_image, 'RGBA')

for face_landmarks in face_landmarks_list:

    # Make the eyebrows into a nightmare
    d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
    d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
    d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
    d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

    # Add Chin
    d.polygon(face_landmarks['chin'], fill=(100, 100, 0, 128))
    d.polygon(face_landmarks['nose_bridge'], fill=(255, 0, 0, 128))
    d.polygon(face_landmarks['nose_tip'], fill=(0, 200, 0, 128))

    # Gloss the lips
    d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

    # Sparkle the eyes
    d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
    d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

    # Apply some eyeliner
    d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
    d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)

pil_image.show()

face_encodings = face.face_encodings(guess_image, face_locations)

# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
# See http://pillow.readthedocs.io/ for more about PIL/Pillow
pil_image = Image.fromarray(origin)
# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    matches = face.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
    name = "Unknown"

    # If a match was found in known_face_encodings, just use the first one.
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw a label with a name below the face
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


# Remove the drawing library from memory as per the Pillow docs
del draw

# Display the resulting image
pil_image.show()

# You can also save a copy of the new image to disk if you want by uncommenting this line
# pil_image.save("image_with_boxes.jpg")
