import cv2
import numpy as np
import os

imgPath = "images/"
img4use = []

def loadImg():
    for img in os.listdir(imgPath):
        img_loc = os.path.join(imgPath, img)

        loaded_img = cv2.imread(img_loc)

        if loaded_img is not None:
            img4use.append(loaded_img)


loadImg()


def gaussBlur(img):
    if img is not None:
        blurdImg = cv2.GaussianBlur(img, (9,9), 3)


        # cv2.imshow("Real Image", img)
        # cv2.imshow("Blurred Image", blurdImg)

        return blurdImg

    cv2.waitKey(0)
    cv2.destroyAllWindows()

blur_img = gaussBlur(img4use[0])


def sharpenImg(img):
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0],
    ]
    )

    sharp = cv2.filter2D(img, -1, kernel)

    cv2.imshow("Original Image", img)
    cv2.imshow("Sharp Image", sharp)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# sharpenImg(blur_img)


def getContours(img):

    imgCp = img.copy()

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(grayImg, 127, 200, cv2.THRESH_BINARY)

    contours, heirarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntImg = cv2.drawContours(grayImg,  contours, -1,  (0,255,0), 2)

    cv2.imshow("Contours", cntImg)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


getContours(img4use[1])
print("hello opencv")