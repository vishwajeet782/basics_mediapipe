import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils

mp_hands = mp.solutions.hands
model_hands=mp_hands.Hands()
cap=cv2.VideoCapture(0)
while cap.isOpened():
    flag,frame=cap.read()
    if not flag:
        print("colundnt acces cam")
        break
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    frame.flags.writeable = False
    results =model_hands.process(frame)

    frame.flags.writeable = True
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    
    for landmark in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            frame,
            landmark,
            mp_hands.HAND_CONNECTIONS)

    cv2.imshow("windows",frame)
    if cv2.waitKey(10) & 0xff==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
