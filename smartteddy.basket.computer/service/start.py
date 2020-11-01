from threading import Thread
import cv2
from facerecognition.main import main as face
from objectrecognition.main import main as object_rec
# from speechrecognition.main import main as speech
from usb_serial.main import main as usb

camera = cv2.VideoCapture(0)

face_thread = Thread(target=face, args=(camera,))
object_thread = Thread(target=object_rec, args=(camera,))
# speech_thread = Thread(target=speech)
usb_thread = Thread(target=usb)

face_thread.start()
object_thread.start()
# speech_thread.start()
usb_thread.start()
