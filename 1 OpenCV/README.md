## ADD images  
## Add codes

### Remove noise and detect edges
This project uses the the bilateral filter to remove noise from the frame captured by the webcam.There are four parameters that needs to be entered to apply this filter and these parameters include the source image,filter size,sigma space and colour.After removing the noise,the Canny function is applied to detect the edges from the image.There are three parameters that needs to be entered to apply this function and these parameters include the source image,minVal and maxVal.Minval is the first and lower threshold to detect the edge while Maxval represents the upper and maximum threshold.

### Representation of edges
An empty matrix is created to store the coordinates of the edges.A for loop is used to go through every row at intervals of 5 and a nested for loop is used to determine the height of the edge at every row.Once the coordinates for all the edges are obtained,a line is drawn connecting all the heights of the edges and from the bottom of every row.

### Dividing the frame into chunks
The dimensions of the entire frame is 640 by 480.Therefore,if the edges are obtained from the rows at every 5 intervals,a total of 128 edge coordinates are expected to be obtained.The first to step to decide which direction the rover should move to avoid an obstacle is to divide the frame into chunks.If the frame is divided into three chunks,approximately 42 different edge coordinates are expected to be obtained in each chunk.The average edge coordinates is obtained from each chunk and a line is drawn from the midpoint of the frame towards the chunks.If an obstacle is detected at the center chunk,the longest line drawn towards the chunk at the sides will be considered and rover will decide on which direction to move by following the longest line.
