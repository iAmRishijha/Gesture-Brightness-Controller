import numpy as np
import mediapipe as mp
import cv2 as cv
import screen_brightness_control as sbc


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode = False, max_num_hands=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

video = cv.VideoCapture(0)
while True:
    ret, frame = video.read()
    frame = cv.flip(frame,1)
    height , width, _ = frame.shape
    results = hands.process(cv.cvtColor(frame, cv.COLOR_BGR2RGB))
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image = frame, landmark_list = hand_landmarks,connections = mp_hands.HAND_CONNECTIONS)
            th = hand_landmarks.landmark[mp_hands.HandLandmark(4).value]
            ind = hand_landmarks.landmark[mp_hands.HandLandmark(8).value]
            x1, y1 = int(th.x*width), int(th.y*height)
            x2 , y2 =  int(ind.x*width), int(ind.y*height)
            cv.circle(frame,(x1,y1),3,(255, 0, 0),2)
            cv.circle(frame,(x2,y2),3,(0, 255, 0),2)
            cv.line(frame,(x1,y1),(x2,y2),(0,0,255),2)
            dist = np.hypot(x2-x1,y2-y1)
            x = np.interp(dist, [50, 200], [0,100])
            sbc.set_brightness(int(x))


    cv.imshow('video', frame)
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break
video.release()
cv.destroyAllWindows()
