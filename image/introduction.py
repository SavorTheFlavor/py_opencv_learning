import cv2
import numpy as np

img = cv2.imread('beauty.jpg', cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1
cv2.imwrite('graybeauty.jpg',img)

cv2.imshow("beauty",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
