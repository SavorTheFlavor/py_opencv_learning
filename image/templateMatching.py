import cv2
import numpy as np

img_bgr = cv2.imread('somedevices.png')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread('templateToMatch.png', 0)
w, h = template.shape[::-1]  # reverse

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.75
loc = np.where(res >= threshold)  # filter matching point >= threshold

for pt in zip(*loc[::-1]):
	cv2.rectangle(img_bgr, pt, (pt[0]+w,pt[1]+h),(0,0,255))
	
cv2.imshow('img_matching',img_bgr)
cv2.imshow('template',template)
cv2.waitKey(0)
cv2.destroyAllWindows()