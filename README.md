# Obstacle_avoidance_opencv

## Introduction to the Workshop
The objective of this workshop is to build a rover (a robot with a set of moving wheels) and introduce Computer Vision using Raspberry Pi to the community in a fun and interactive way. This done by building an obstacle avoiding rover using OpenCV. A webcam will be fitted on a rover that will stream whatever it sees in its path into Python where we will process the capture with OpenCV to check for obstacles in its way and take evasive action. A full recap of OpenCV will take place during the workshop before combining both the efforts of OpenCV and the rover.

## Logic:<br/>
![image](https://user-images.githubusercontent.com/10446090/44290427-ba9ef900-a289-11e8-87fb-860ffe66dd9a.png)


## Introduction to Computer Vision
It is a field that deals with how computers can be made for gaining high-level understanding from digital images or videos. From the perspective of engineering, it seeks to automate tasks that a human can do.

## Installing Python and OpenCV using Anaconda
![image](https://user-images.githubusercontent.com/10446090/44288410-52e4b000-a281-11e8-90b8-5a59a31a2be1.png)

- A guide to installing Anaconda: https://conda.io/docs/user-guide/install/index.html <br/>
- Steps to install OpenCV using Anaconda : https://anaconda.org/conda-forge/opencv <br/>

## Installing Raspberry PI libraries

### Install Python 3 and PIP

![image](https://user-images.githubusercontent.com/10446090/44288044-051b7800-a280-11e8-8bad-761a46389f79.png) <br/>

Usually Python3 is pre-installed when you install Raspbian on your Raspberry PI. 
But, not all Python packages are available in the Raspbian archives, and those that are can sometimes be out-of-date. If you can't find a suitable version in the Raspbian archives, you can install packages from the Python Package Index (PyPI). To do so, use the pip tool.

**Pip** is installed by default in Raspbian Jessie (but not Raspbian Wheezy or Jessie Lite). You can install it with apt:

```
sudo apt-get install python3-pip
```

### OpenCV 
![image](https://user-images.githubusercontent.com/10446090/44288007-ed43f400-a27f-11e8-9abc-64c846021529.png) <br/>

OpenCV(Open Source Computer Vision) is a library of programming functions mainly aimed at real-time computer vision. <br/>

#### Expand filesystem
If you’re using a brand new install of Raspbian Jessie, then the first thing you should do is ensure your filesystem has been expanded to include all available space on your micro-SD card.

On the terminal type:  
```
sudo raspi-config
```
Select the first option “1. Expand Filesystem”, arrow down to “Finish”, and reboot your Pi. <br/>
After rebooting, your filesystem will have be expanded to include all available space on your micro-SD card.

#### Installing dependencies

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
#### Grab the OpenCV source

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

#### Setup Python
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
#### Compile and install OpenCV for the Raspberry Pi Zero
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
#### Finishing the install

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

#### Verifying your OpenCV install

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

#### Errors in installation
If there are any errors after compiling the code above, where its suggests:
```ImportError: No module named cv2```
There could be two solutions:
-Either install openCV through python, by typing:
```
sudo apt-get install python-opencv
```
- or try redoing all the above mentioned steps.

**SOURCE: https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/**

### Setting up the GPIO pins on a Raspberry PI
The newest version of Raspbian has the RPi.GPIO library pre-installed. You’ll probably need to update your library, so using the command 
line, run:

```
 sudo apt-get install rpi.gpio
```

If it isn’t already installed it will be installed. If it is already installed it will be upgraded if a newer version is available.
#### Using the RPi.GPIO Library
Now that you’ve got the package installed and updated, let’s take a look at some of the functions that come with it. Open the Leafpad text editor and save your sketch as “myInputSketch.py”. From this point forward, we’ll execute this script using the command line:

```
sudo python myInputSketch.py
```

All of the following code can be added to this same file. Remember to save before you run the above command. To exit the sketch and make changes, press Ctrl+C.

To add the GPIO library to a Python sketch, you must first import it: <br/>

```python
import RPi.GPIO as GPIO
```

Then we need to declare the type of numbering system we’re going to use for our pins: <br/>

```python
#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
#setup GPIO using Board numbering
GPIO.setmode(GPIO.BOARD)
```
#### Examples: 
https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins <br/>
https://www.raspberrypi-spy.co.uk/2012/05/install-rpi-gpio-python-library/

### Setting up the program to run on terminal, after boot
A simple way to see how you can setup to run python file on Raspberry Pi startup (using the terminal).

- Save the python file on home/pi
- On the terminal, navigate to  /home/pi
- now open a hidden file  .bashrc  ( type "sudo nano .bashrc" on terminal and press enter)
- At the end of the file type "python" followed by your file name (eg: python3 speechtotext)
- If you want the terminal to revert back to its normal format, either comment out the command on the .bashrc file or remove it (you can access the bash file in /home/pi).

## Circuit Assembly
![opencv_obstacle_avoid_bb](https://user-images.githubusercontent.com/32713072/44152058-6c95e9a6-a0b5-11e8-88ed-b0a5be95332e.jpg)






