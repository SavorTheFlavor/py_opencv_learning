import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_,frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	# hsv  hue Saturation Value, hue is crucial
	lower_red = np.array([120,150,50])
	upper_red = np.array([180,255,200])
	
	# from lower_red to upper_red (0 to 255 is the original)
	# in range l..u to create a mask 
	# when mask[,,] = true, then show the color, otherwise cover it(black)
	mask = cv2.inRange(hsv, lower_red, upper_red)
	res = cv2.bitwise_and(frame, frame, mask=mask) # frame&frame in the mask area
	
	# smoothed and blur
	kernel = np.ones((15,15), np.float32)/255 # all elements are 1  (/255
	smoothed = cv2.filter2D(res, -1, kernel)
	
	blur = cv2.GaussianBlur(res, (15,15), 0)
	median = cv2.medianBlur(res, 15)
	bilateral = cv2.bilateralFilter(res, 15, 75, 75)
	
	cv2.imshow('frame',frame)
	# cv2.imshow('res',res)
	cv2.imshow('median',median)
	
	# k = cv2.waitKey(5) & 0xFF
	# if k == 27:
	k = cv2.waitKey(10)
	if k != -1:
		break

cv2.destroyAllWindows()
cap.release()