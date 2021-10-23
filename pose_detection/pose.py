import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
model_pose=mp_pose.Pose()
cap=cv2.VideoCapture(0)

while cap.isOpened():
	flag,frame=cap.read()
	if not flag:

		print("couldnt access camera")
		break
	
	results = model_pose.process(frame)
	
	
	mp_drawing.draw_landmarks(
		   frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
	cv2.imshow("Frame",frame)
	if cv2.waitKey(50)&0xff==ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
