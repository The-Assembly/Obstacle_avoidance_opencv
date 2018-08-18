from time import sleep
from gpiozero import Robot
import curses

screen = curses.initscr()
curses.cbreak()
screen.keypad(1)

x = 1

a = 1
b = 0.9
c = 0.8
d = 0.7
e = 0.6
f = 0.5
g = 0.4


key = ''
r = Robot(left=(23, 24), right=(11,9))

def forward(): #... add onto the left 
    m1_speed = a*x #0.865
    m2_speed = a*x #1
    r.value = (m1_speed, m2_speed)

def backward(): 
    r.reverse()

def right():
    r.right(speed=1*x)
    print ("Going right")
    sleep(1.2) #0.5
    forward()

 
def left(): 
    r.left(speed=1*x)
    print ("Going left")
    sleep(1.2) #0.5
    forward()

def stop():
    m1_speed = 0.0
    m2_speed = 0.0
    r.value = (m1_speed, m2_speed)
    print('going off')
   
while key != ord('q'):  # press <Q> to exit the program
    key = screen.getch()  # get the key
    screen.addch(0, 0, key)  # display it on the screen
    screen.refresh()

    # the same, but for <Up> and <Down> keys:
    if key == curses.KEY_UP:
        screen.addstr(0, 0, "Up")
        forward()

    elif key == curses.KEY_DOWN:
        screen.addstr(0, 0, "down")
        backward()

    elif key == curses.KEY_LEFT:
        screen.addstr(0, 0, "Left")
        left()
        
    elif key == curses.KEY_RIGHT:
        screen.addstr(0, 0, "Right")
        right()


curses.endwin()
         
