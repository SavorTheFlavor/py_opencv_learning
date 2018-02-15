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
	
	kernel = np.ones((5,5), np.uint8)
	erosion = cv2.erode(mask, kernel, iterations = 1)
	dilation = cv2.dilate(mask, kernel, iterations = 1)
	
	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	
	cv2.imshow('frame',frame)
	cv2.imshow('dilation',dilation)
	cv2.imshow('opening',opening)
	cv2.imshow('closing',closing)
	
	# k = cv2.waitKey(5) & 0xFF
	# if k == 27:
	k = cv2.waitKey(10)
	if k != -1:
		break

cv2.destroyAllWindows()
cap.release()