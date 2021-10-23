import cv2
import mediapipe as mp
mp_drawing=mp.solutions.drawing_utils
mp_face_detection=mp.solutions.face_detection
model_detection=mp_face_detection.FaceDetection()
cap=cv2.VideoCapture(0)
while cap.isOpened():
    flag,frame=cap.read()
    if not flag:
        print("couldnt access cam")

        break
    results=model_detection.process(frame)
    
    print(results.detections)
    if results.detections is not None:
        for landmarks in results.detections:
            mp_drawing.draw_detection(frame,landmarks)
    cv2.imshow("fra",frame)
    if cv2.waitKey(10) & 0xff==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
