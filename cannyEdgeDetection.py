import cv2
import numpy as np

img = cv2.imread("images/rename.jpg")
img = cv2.resize(img, (400, 400))

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow("Original Image", img)

# cv2.imshow("Gray Image", grayImg)

# edges = cv2.Canny(grayImg, 50, 150)

# cv2.imshow("Edged Images", edges)

_, thresh = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Image", thresh)


img2 = cv2.imread("images/lp2.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img2, (400,400))

__, threshh = cv2.threshold(img2, 50, 150, cv2.THRESH_BINARY)

newImg = cv2.bitwise_and(grayImg, img2)
cv2.imshow("And operation", newImg)

# cv2.imshow("Second Image", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()