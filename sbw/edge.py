import numpy as np
import cv2
img = cv2.imread('1.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
edge = cv2.Canny(img, 100, 200)
res = cv2.bitwise_not(edge)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('res.png', res)
