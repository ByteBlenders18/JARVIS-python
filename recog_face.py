import cv2
import face_recognition
import numpy as np
import time
import pyttsx3
import assist_fuction


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 0)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def recognizer():
    global name
    i = 1
    video_capture = cv2.VideoCapture(0)
    # image and their encoding
    shr_image = face_recognition.load_image_file(r"faces/1706628890587.jpg")
    shr_encoding = face_recognition.face_encodings(shr_image)[0]

    aryan_image = face_recognition.load_image_file(r"faces/aryan.jpg")
    aryan_encoding = face_recognition.face_encodings(aryan_image)[0]

    tapish_image = face_recognition.load_image_file(r"faces/tapish.jpg")
    tapish_encoding = face_recognition.face_encodings(tapish_image)[0]

    parth_image = face_recognition.load_image_file(r"faces/parth.jpg")
    parth_encoding = face_recognition.face_encodings(parth_image)[0]

    bhargav_image = face_recognition.load_image_file(r"faces/bhargav.jpg")
    bhargav_encoding = face_recognition.face_encodings(bhargav_image)[0]

    tare_image = face_recognition.load_image_file(r"faces/tare.jpg")
    tare_encoding = face_recognition.face_encodings(tare_image)[0]

    known_face_encodings = [shr_encoding, aryan_encoding, parth_encoding, tare_encoding, tapish_encoding, bhargav_encoding]

    known_face_names = ["shreyansh", "aryan", "parth", "aditya", "tapish", "devansh"]

    people = known_face_names.copy()

    face_locations = []
    face_encodings = []

    person_file = open("text/person.txt", 'w+')

    while True:

        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:

                name = known_face_names[best_match_index]
            else:
                continue

            if name in known_face_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 100)
                fontScale = 1.5
                fontColor = (255, 0, 0)
                thickness = 3
                lineType = 2
                cv2.putText(frame, name, bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

                while i == 1:
                    time.sleep(3)
                    # speak(f"the person is {name}")
                    if "aryan" in name:
                        assist_fuction.speak_hindi("the person is aryan")

                    elif "parth" in name:
                        assist_fuction.speak_hindi("the person is parth.")

                    elif "devansh" in name:
                        assist_fuction.speak_hindi("the person is devansh")

                    elif "tapish" in name:
                        assist_fuction.speak_hindi("the person is tapish")

                    elif "aditya" in name:
                        assist_fuction.speak_hindi("the person is aditya")
                    i = i + 1

        cv2.imshow("person", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    person_file.write(name)

    video_capture.release()
    cv2.destroyAllWindows()
    person_file.close()
    return name
