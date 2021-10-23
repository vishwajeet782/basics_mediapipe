import cv2
import numpy as np 

cap=cv2.VideoCapture(0)
image1=cv2.imread("background1.jpg")
image2=cv2.imread("background2.jpg")
image3=cv2.imread("background3.jpg")
image4=cv2.imread("background4.jpg")
image5=cv2.imread("background5.jpg")
image6=cv2.imread("background6.jpg")

while cap.isOpened():
	
	sucess ,frame=cap.read()
	if sucess:
    
		image1=cv2.resize(image1,(frame.shape[1],frame.shape[0]))
		image2=cv2.resize(image2,(frame.shape[1],frame.shape[0]))
		image3=cv2.resize(image3,(frame.shape[1],frame.shape[0]))
		image4=cv2.resize(image4,(frame.shape[1],frame.shape[0]))
		image5=cv2.resize(image5,(frame.shape[1],frame.shape[0]))
		image6=cv2.resize(image6,(frame.shape[1],frame.shape[0]))
        
		blended_image1=cv2.addWeighted(frame,0.8,image1,0.3,gamma=0.5)
		blended_image2=cv2.addWeighted(frame,0.8,image2,0.3,gamma=0.5)
		blended_image3=cv2.addWeighted(frame,0.8,image3,0.3,gamma=0.5)
		blended_image4=cv2.addWeighted(frame,0.8,image4,0.3,gamma=0.5)
		blended_image5=cv2.addWeighted(frame,0.8,image5,0.3,gamma=0.5)
		blended_image6=cv2.addWeighted(frame,0.8,image6,0.3,gamma=0.5)
		
		cv2.imshow("Frame",frame)
		k=cv2.waitKey(50)
    
	 

		if k & 0xff==ord('1'):
			cv2.imshow("blend",blended_image1)
		elif k & 0xff==ord('2'):
			cv2.imshow("blend2",blended_image2)
		elif k & 0xff==ord('3'):
			cv2.imshow("blend3",blended_image3)
		elif k & 0xff==ord('4'):
			cv2.imshow("blend4",blended_image4)
		elif k & 0xff==ord('5'):
			cv2.imshow("blend5",blended_image5)
		elif k & 0xff==ord('6'):
			cv2.imshow("blend6",blended_image6)
				
			
		elif k & 0xff==ord('q'):
			break
    
	else:
		break

cap.release()
cv2.destroyAllWindows()
