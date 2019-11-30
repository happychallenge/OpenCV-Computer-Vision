import face_recognition as face
from PIL import Image, ImageDraw

# Load the jpg file into a numpy array
image = face.load_image_file("daughter.jpg")

# Find all facial landmarks in all the faces in the image
face_landmarks_list = face.face_landmarks(image)

pil_image = Image.fromarray(image)
# RGBA - create an image using alpha composite , to make it translucent
d = ImageDraw.Draw(pil_image, 'RGBA')

for face_landmarks in face_landmarks_list:
    print(face_landmarks.keys())
    # eyebrows darker 
    d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
    d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
    d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
    d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

    # Add Chin
    d.polygon(face_landmarks['chin'], fill=(100, 100, 0, 128))
    d.polygon(face_landmarks['nose_bridge'], fill=(255, 0, 0, 128))
    d.polygon(face_landmarks['nose_tip'], fill=(0, 200, 0, 128))

    # Add lipstick
    d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

    # reddish eyes
    d.polygon(face_landmarks['left_eye'], fill=(255, 0, 0, 30))
    d.polygon(face_landmarks['right_eye'], fill=(255, 0, 0, 30))

    # Apply some mascara to eyes
    d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
    d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)

    pil_image.show()

    # You can also save a copy of the new image to disk if you want by uncommenting this line
pil_image.save("abhimakeup.jpg")