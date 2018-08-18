import cv2
import numpy as np
cap = cv2.VideoCapture(1)
StepSize = 5
while(1):
    ret,frame = cap.read()
    img = frame.copy()
    blur = cv2.bilateralFilter(img,9,40,40)
    edges = cv2.Canny(blur,50,100)
    cv2.imshow("Canny",blur)
    img_h = img.shape[0] - 1
    img_w = img.shape[1] - 1
    EdgeArray = []
    for j in range(0,img_w,StepSize):
        pixel = (j,0)
        for i in range(img_h-5,0,-1):
            if edges.item(i,j) == 255:
                pixel = (j,i)
                break
        EdgeArray.append(pixel)
    
    for x in range(len(EdgeArray)-1):
        cv2.line(img, EdgeArray[x], EdgeArray[x+1], (0,255,0), 1)
    for x in range(len(EdgeArray)):
        cv2.line(img, (x*StepSize, img_h), EdgeArray[x],(0,255,0),1)
    cv2.imshow("result",img)
    k = cv2.waitKey(5) & 0xFF  ##change to 5
    if k == 27:
        break
cv2.destroyAllWindows
cap.release()