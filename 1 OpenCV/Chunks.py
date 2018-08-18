import cv2
import numpy as np
cap = cv2.VideoCapture(1)
StepSize = 5
def getChunks(l, n):
    """Yield successive n-sized chunks from l."""
    a = []
    for i in range(0, len(l), n):   
        a.append(l[i:i + n])
    return a

while(1):
    ret,frame = cap.read()
    img = frame.copy()
    blur = cv2.bilateralFilter(img,9,40,40)
    edges = cv2.Canny(blur,50,100)
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
    chunks = getChunks(EdgeArray,int(len(EdgeArray)/3))
    c = []
    for i in range(len(chunks)-1):        
        x_vals = []
        y_vals = []
        for (x,y) in chunks[i]:
            x_vals.append(x)
            y_vals.append(y)
        avg_x = int(np.average(x_vals))
        avg_y = int(np.average(y_vals))
        c.append([avg_y,avg_x])
        cv2.line(frame,(320,480),(avg_x,avg_y),(255,0,0),2) 
        cv2.imshow("frame",frame) 
    k = cv2.waitKey(5) & 0xFF  ##change to 5
    if k == 27:
       break
cv2.destroyAllWindows
cap.release()       