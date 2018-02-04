import numpy as np
import cv2


img = cv2.imread('sweetie.jpg',cv2.IMREAD_COLOR)

px = img[23,55] # a pixel of (23,55)
print(px)

img[22:120, 90:255] = [104,74,205]
img[140:218,90:200] = img[22:100, 40:150]

cv2.imshow('image',img)
cv2.waitKey(0)


img1 = cv2.imread('p1.jpg')
img2 = cv2.imread('p2.jpg')
# img12 = img1 + img2
#img12 = cv2.add(img1,img2) # add pixels together..if exceed =255
img12 = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('image',img12)
cv2.waitKey(0)



pic = cv2.imread('p2.jpg')
logo = cv2.imread('logo.jpg')
rows,cols,channels = logo.shape  # 颜色通道、灰度通道...
roi = pic[0:rows,0:cols] # region of image..

logogray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
# threshold:220 if >= --> 255  else ---> 0     BINARY-- 0 or 1 inverse
ret, mask = cv2.threshold(logogray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask) # bitwise 按位..

pic_bg = cv2.bitwise_and(roi,roi, mask=mask_inv)
logo_fg = cv2.bitwise_and(logo,logo, mask=mask)

dst = cv2.add(pic_bg, logo_fg)
pic[0:rows,0:cols] = dst


cv2.imshow('p2 with logo',pic)
cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('pic_bg',pic_bg)
cv2.imshow('logo_fg',logo_fg)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
