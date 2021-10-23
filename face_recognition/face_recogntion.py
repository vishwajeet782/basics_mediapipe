import cv2
import face_recognition
import numpy as np

chris=face_recognition.load_image_file("chris.jpg")
chris_location_=face_recognition.face_locations(chris)[0]
chris_encodings=face_recognition.face_encodings(chris)[0]

robert=face_recognition.load_image_file('robert.jpg')
robert_location=face_recognition.face_locations(robert)[0]
robert_encodings=face_recognition.face_encodings(robert)[0]
virat=face_recognition.load_image_file("virat.jpg")
virat_location_=face_recognition.face_locations(virat)[0]
virat_encodings=face_recognition.face_encodings(virat)[0]

dhoni=face_recognition.load_image_file('msdhoni.jpg')
dhoni_location=face_recognition.face_locations(dhoni)[0]
dhoni_encodings=face_recognition.face_encodings(dhoni)[0]

known_face_encodings=[virat_encodings,dhoni_encodings,chris_encodings,robert_encodings]
known_face_names=["virat","dhoni","chris","robert"]

cap=cv2.VideoCapture(0)

while cap.isOpened():
	flag,frame=cap.read()
	if not flag:
		print("couldnt find camera")
		break
	small_frame=cv2.resize(frame,(0,0),fx=1/4,fy=1/4)
	rgb_small_frame=cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)
	face_locations = face_recognition.face_locations(rgb_small_frame)
	face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
	face_names=[]
	for face_encoding in face_encodings:
		matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
		name = "Unknown"
		face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
		best_match_index = np.argmin(face_distances)
		if matches[best_match_index]:
			name = known_face_names[best_match_index]
		face_names.append(name)
	print(face_names)

	for (top, right, bottom, left), name in zip(face_locations, face_names):
		top *= 4
		right *= 4
		bottom *= 4
		left *= 4
		cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
		cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
		font = cv2.FONT_HERSHEY_DUPLEX
		cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)       
	
	cv2.imshow("frame",frame)
	if cv2.waitKey(1) & 0xff ==ord('q'):
			break
	
	


	

		
	
	

cap.release()
cv2.destroyAllWindows()
