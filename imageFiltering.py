import cv2
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
        blurdImg = cv2.GaussianBlur(img, (7,7), 3)


        cv2.imshow("Real Image", img)
        cv2.imshow("Blurred Image", blurdImg)

        cv2.waitKey(0)
    cv2.destroyAllWindows()

gaussBlur(img4use[0])




