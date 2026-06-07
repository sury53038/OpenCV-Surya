from operator import truediv
from turtle import reset

import cv2
import os

img_path = "images/"
saveDir = "images/saveImgs"
img4use = []

os.makedirs(saveDir, exist_ok=True)


def loadImg():
    for img in os.listdir(img_path):
    
        img_loc = os.path.join(img_path, img)

        imgg = cv2.imread(img_loc)

        if img is not None:
            img4use.append(imgg)


def saveOrShowImg():
    for img in img4use:
        if img is not None:
            imgInUse = img

            imgInUse = cv2.cvtColor(imgInUse, cv2.COLOR_BGR2GRAY)

            print("Do you want to save or display image? S/D :")
            user = input()

            if(user == "S" or user == "s"):

                name = input("Enter image name :")

                imgLoc = os.path.join(saveDir, name)

                cv2.imwrite(imgLoc, imgInUse)

                print("New image added to saveImgs")

            elif(user == "D" or user == "d"):

                cv2.imshow("Image", imgInUse)

                cv2.waitKey(0)

                cv2.destroyAllWindows()

            else:
                continue


def cropImage(img):
     cropped = img[10:400, 10:350]
     cv2.imshow("Original", img)
     cv2.imshow("Croopped", cropped)
     
     cv2.waitKey(0)
     cv2.destroyAllWindows()

def resizeImage(img):
     h, w, c = img.shape

     resized = cv2.resize(img, (480, 360))

     return resized

loadImg() 

# cropImage(resizeImage(img4use[0]))

def rotateImg(img, angle):
    h,w = img.shape[:2]
    center = (h//2, w//2)

    rotate = cv2.getRotationMatrix2D(center, angle, 1.0)
    resultImg = cv2.warpAffine(img, rotate, (w,h))

    cv2.imshow("orignal", img)
    cv2.imshow("rotated", resultImg)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# rotateImg(img4use[0], -90) #positive angle rotates the image in counter-clockwise dir and -ve angle value rotates in clock-wise dir

def flipImg(img):
    flipped_horizontal = cv2.flip(img, 1)
    flipped_vertical = cv2.flip(img, 0)
    flipped_both = cv2.flip(img, -1)

    cv2.imshow("Original Image", img)
    cv2.imshow("Horizontal Flip", flipped_horizontal)
    cv2.imshow("Vertical Flip", flipped_vertical)
    cv2.imshow("Both Flip", flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# flipImg(img4use[0])

def drawLine(img):
    if img is not None:
        pt1 = (50,100)
        pt2 = (300,100)

        ln = cv2.line(img,
                pt1, pt2,
                (255, 0, 0),
                4)
        
        cv2.imshow("Lined Image", ln)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


# drawLine(img4use[0])

def drawRect(img):
    if img is not None:
        pt1 = (50,50)
        pt2 = (300,300)
        color = (0,255,0)

        rect = cv2.rectangle(img, pt1, pt2, color, 4)

        cv2.imshow("Rectangle", rect)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# drawRect(img4use[0])

def textPrint(img):
    if img is not None:
        txtImg = cv2.putText(img, "This is Billa's image", 
                    (400, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.2,
                    (0,255,220),
                    2)
        cv2.imshow("image", txtImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        

textPrint(img4use[0])