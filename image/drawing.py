import numpy as np
import cv2

img = cv2.imread('XXX.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(70,70),(860,540),(0,0,255),40)
cv2.line(img,(860,70),(70,540),(0,0,255),40)
cv2.rectangle(img,(70,70),(860,540),(0,255,0),40)
cv2.imshow('xxxx',img)

img = cv2.imread('XXX.jpg',cv2.IMREAD_COLOR)
cv2.circle(img,(450,320),400,(255,0,0),-1) # -1 fill in
pts = np.array([[110,40],[70,70],[450,320],[860,540],[450,320],[860,70],[450,320],[70,540]],np.int32)
cv2.polylines(img,[pts],False,(255,255,0),40)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'HEY!!',(420,320),font,2,(0,0,255),10,cv2.LINE_AA)
cv2.imshow('xxxx2',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
