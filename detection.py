import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# choosing image
# img = cv2.imread("r2.jfif")
# webcam = cv2.VideoCapture("Doraemon")
webcam = cv2.VideoCapture(0)

# iterate with frames forever
while True:
    # reading the current frame
    successful_frame_read, frame = webcam.read()


    # converting to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect Faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # Draw rectangles around the face
    for (x, y, w, h) in face_coordinates:
    #(x, y, w, h) = face_coordinates[0]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 3)

    cv2.imshow('image', frame)
    key = cv2.waitKey(1)

    # Stop if Q key is pressed
    if key == 81 or key==113:
        break

# Release the video capture object
webcam.release()



""""
# Detect Faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# Draw rectangles around the face
for (x, y, w, h) in face_coordinates:
#(x, y, w, h) = face_coordinates[0]
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 3)

#print(face_coordinates)



cv2.imshow('image', img)
cv2.waitKey()

"""
print("code completed")