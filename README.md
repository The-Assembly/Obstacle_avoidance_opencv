# Obstacle_avoidance_opencv

## Introduction to the Workshop
The objective of this workshop is to build a rover (a robot with a set of moving wheels) and introduce Computer Vision using Raspberry Pi to the community in a fun and interactive way. This done by building an obstacle avoiding rover using OpenCV. A webcam will be fitted on a rover that will stream whatever it sees in its path into Python where we will process the capture with OpenCV to check for obstacles in its way and take evasive action. A full recap of OpenCV will take place during the workshop before combining both the efforts of OpenCV and the rover.

## Introduction to Computer Vision
It is a field that deals with how computers can be made for gaining high-level understanding from digital images or videos. From the perspective of engineering, it seeks to automate tasks that a human can do.

## Installing openCV and other libraries

### Expand filesystem
If you’re using a brand new install of Raspbian Jessie, then the first thing you should do is ensure your filesystem has been expanded to include all available space on your micro-SD card.

On the terminal type:  
```
sudo raspi-config
```
Select the first option “1. Expand Filesystem”, arrow down to “Finish”, and reboot your Pi. <br/>
After rebooting, your filesystem will have be expanded to include all available space on your micro-SD card.

### Installing dependencies

First, we need to update and upgrade our existing packages:
```
sudo apt-get update
sudo apt-get upgrade
```

Install our developer tools:
```
$ sudo apt-get install build-essential cmake pkg-config
```

Let’s grab the image I/O packages and install them:
```
$ sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
```

Along with some video I/O packages:
```
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
$ sudo apt-get install libxvidcore-dev libx264-dev
```

We’ll need to install the GTK development library for OpenCV’s GUI interface:
```
$ sudo apt-get install libgtk2.0-dev
```
Let’s also pull down a couple routine optimization packages leveraged by OpenCV:
```
$ sudo apt-get install libatlas-base-dev gfortran
```

Lastly, let’s install the Python 2.7 headers so wen can compile our OpenCV + Python bindings:
``` 
sudo apt-get install python2.7-dev
```
### Grab the OpenCV source

At this point, all of our dependences have been installed, so let’s grab the 3.0.0  release of OpenCV from GitHub and pull it down:
```
$ cd ~
$ wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.0.0.zip
$ unzip opencv.zip
```

Let’s also grab the opencv_contrib repository as well:
```
$ wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.0.0.zip
$ unzip opencv_contrib.zip
```

It’s especially important to grab the ```opencv_contrib```  repo if you want access to SIFT and SURF, both of which have been removed from the default install of OpenCV.

Now that``` opencv.zip ``` and ```opencv_contrib.zip``` have been expanded, let’s delete them to save space:
```
$ rm opencv.zip opencv_contrib.zip
```

### Setup Python
The first step in setting up Python for the OpenCV build is to install pip , a Python package manager:
```
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python get-pip.py
```

Let’s also install virtualenv  and virtualenvwarpper , allowing us to create separate, isolated Python environments for each of our future projects:
```
$ sudo pip install virtualenv virtualenvwrapper
$ sudo rm -rf ~/.cache/pip
```

To complete the install of virtualenv  and virtualenvwrapper , open up your ```~./profile``` :
```
$ nano ~/.profile
```

And append the following lines to the bottom of the file:
```
# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

Now, source  your ~/.profile  file to reload the changes:
```
$ source ~/.profile
```

Let’s create a new Python virtual environment appropriately named cv :
```
$ mkvirtualenv cv
```

The only requirement to build Python + OpenCV bindings is to have NumPy installed, so let’s use pip  to install NumPy for us:
```
$ pip install numpy
```
### Compile and install OpenCV for the Raspberry Pi Zero
We are now ready to compile and install OpenCV. Make sure you are in the cv  virtual environment by using the workon  command:
```  
$ workon cv
```

And then setup the build using CMake:
```
$ cd ~/opencv-3.0.0/
$ mkdir build
$ cd build
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.0.0/modules \
    -D BUILD_EXAMPLES=ON ..
```

Now that the build is all setup, run make  to start the compilation process (this is going to take awhile, so you might want to let this run overnight):
```
$ make
```

Assuming OpenCV compiled without error, you can install it on your Raspberry Pi Zero using:
```
$ sudo make install
$ sudo ldconfig
```
### Finishing the install

Provided you completed the previous step without an error, your OpenCV bindings should now be installed in ```/usr/local/lib/python2.7/site-package``` :
```
$ ls -l /usr/local/lib/python2.7/site-packages
total 1640
-rw-r--r-- 1 root staff 1677024 Dec  2 08:34 cv2.so
```

All we need to do now is sym-link the ```cv2.so```  file (which are our actual Python + OpenCV bindings) into the ```site-packages```  directory of the``` cv```  virtual environment:
```
$ cd ~/.virtualenvs/cv/lib/python2.7/site-packages/
$ ln -s /usr/local/lib/python2.7/site-packages/cv2.so cv2.so
```

### Verifying your OpenCV install

All that’s left to do now is verify that OpenCV has been correctly installed on your Raspberry Pi Zero.<br/>
Whenever you want to use OpenCV, first make sure you are in the ```cv```  virtual environment:
```
$ workon cv
```
And from there you can fire up a Python shell and import the OpenCV bindings:
```
$ workon cv
$ python
>>> import cv2
>>> cv2.__version__
'3.0.0'
>>>
```
Or you can execute a Python script that imports OpenCV.<br/>

Once OpenCV has been installed, you can remove both the opencv-3.0.0  and opencv_contrib-3.0.0  directories, freeing up a bunch of space on your filesystem:
```
$ rm -rf opencv-3.0.0 opencv_contrib-3.0.0
```

### Errors in installation
If there are any errors after compiling the code above, where its suggests:
```ImportError: No module named cv2```
There could be two solutions:
-Either install openCV through python, by typing:
```
sudo apt-get install python-opencv
```
- or try redoing all the above mentioned steps.

## Circuit Assembly


## Coding and Software implementation

### Remove noise and detect edges
This project uses the the bilateral filter to remove noise from the frame captured by the webcam.There are four parameters that needs to be entered to apply this filter and these parameters include the source image,filter size,sigma space and colour.After removing the noise,the Canny function is applied to detect the edges from the image.There are three parameters that needs to be entered to apply this function and these parameters include the source image,minVal and maxVal.Minval is the first and lower threshold to detect the edge while Maxval represents the upper and maximum threshold.

### Representation of edges
An empty matrix is created to store the coordinates of the edges.A for loop is used to go through every row at intervals of 5 and a nested for loop is used to determine the height of the edge at every row.Once the coordinates for all the edges are obtained,a line is drawn coonecting all the heights of the edges and from the bottom of the frame at every row.

### Dividing the frame into chunks
The dimensions of the entire frame is 640 by 480.Therefore,if the edges are obtained from the rows at every 5 intervals,a total of 128 edges coordinates are expected to be obtained.The first to step to decide which direction the rover should move to avoid an obstacle is to divide the frame into chunks.If the frame is divided into three chunks,approximately 42 different edge coordinates are expected to be obtained in each chunk.The average edge coordinates is obtained from each chunk and a line is drawn from the midpoint of the frame towards each chunk.If an obstacle is detected at the center chunk,the longest line will be compared between the lines drawn towards the chunk at the sides and rover will decide on which direction to move.



