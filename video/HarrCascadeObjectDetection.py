import cv2
import numpy as np

# these classifiers have been trained.
face_cascade = cv2.CascadeClassifier('D:/learning/py_opencv_learning/video/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('D:/learning/py_opencv_learning/video/haarcascade_eye.xml')
cap = cv2.VideoCapture(1)

while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh),(0,255,0),1)
	
	cv2.imshow('faces and eyes', img)
	k = cv2.waitKey(5)
	if k != -1:
		breaks

cap.release()
cv2.destroyAllWindows()