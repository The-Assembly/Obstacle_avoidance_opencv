import cv2
import numpy as np
cap = cv2.VideoCapture(1)

while(1):
    ret,frame = cap.read()
    img = frame.copy()
    blur = cv2.bilateralFilter(img,9,40,40)
    edges = cv2.Canny(blur,50,100)
    cv2.imshow("Canny",edges)
    k = cv2.waitKey(5) & 0xFF  ##change to 5
    if k == 27:

        break
cv2.destroyAllWindows
cap.release()
        