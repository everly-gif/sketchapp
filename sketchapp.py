import cv2
import numpy as np

def sketch(image):
    grayimg=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blurimg=cv2.GaussianBlur(grayimg(3,3),0)
    edges=cv2.Canny(blurimg,10,80)
    ret,mimg=cv2.threshold(edges,50,255,cv2,THRESH_BINARY_INV)
    return ming
vidCapt=cv2.VideoCapture(0)
while(True):
    ret,picCapt=vidCapt.read()
    cv2.imshow("Your Sketch",getmysketch(picCapt))
    if cv2.waitKey(1)==13:
        break
vidCapt.release()
cv2.destroyAllWindows()