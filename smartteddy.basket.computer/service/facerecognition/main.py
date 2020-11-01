# make sure visual studio for c++ is installed
# pip3 install cmake
# pip3 install face-recognition
# add a picture of the senior into the folder and load that picture on line 23 and write the name on line 87
import face_recognition
import cv2
from PIL import Image, ImageDraw
from datetime import datetime


# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

def saveFeatures(frame, name):
    global current_second
    difference = datetime.now() - datetime.strptime(current_second, '%d-%m-%Y %H:%M:%S')
    if (name != "Unknown") and difference.total_seconds() > 15:
        print(current_second)
        current_second = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        face_landmarks_list = face_recognition.face_landmarks(frame)

        for face_landmarks in face_landmarks_list:

            # Print the location of each facial feature in this image
            facial_features = [
                'chin',
                'left_eyebrow',
                'right_eyebrow',
                'nose_bridge',
                'nose_tip',
                'left_eye',
                'right_eye',
                'top_lip',
                'bottom_lip'
            ]

            pil_image = Image.fromarray(frame)
            d = ImageDraw.Draw(pil_image)

            for facial_feature in facial_features:
                d.line(face_landmarks[facial_feature], width=5)

            file_name = 'facerecognition/images/' + name + str(datetime.now().strftime('%d-%m-%Y %H_%M_%S')) + '.JPEG'
            print(file_name, 'JPEG')
            pil_image.save(file_name, 'JPEG')

def main(camera):
    print('in face')
    # global variables
    global video_capture
    global jeoffrey_face_encoding
    global face_locations
    global face_encodings
    global face_names
    global process_this_frame
    global current_second

    # Get a reference to webcam #0 (the default one)
    video_capture = camera

    # Load a sample picture and learn how to recognize it.
    jeoffrey_image = face_recognition.load_image_file("facerecognition/jeoffrey.jpg")
    jeoffrey_face_encoding = face_recognition.face_encodings(jeoffrey_image)[0]

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    current_second = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(small_frame)
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                match = face_recognition.compare_faces([jeoffrey_face_encoding], face_encoding)
                name = "Unknown"

                if match[0]:
                    name = "Jeoffrey"

                face_names.append(name)

                # remove this line if you don't want to save the images due to storage space
                # estimated to be 74 GB after one year when taking 1 picture every 15 seconds
                saveFeatures(frame, name)

        process_this_frame = not process_this_frame


        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()
