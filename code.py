import RPi.GPIO as GPIO
import cv2 as cv
import numpy as np
import imutils
import time

GPIO.setwarnings(False)

in1 = 20
in2 = 16
en_a = 21
s2 = 27
s3 = 22
signal = 17
NUM_CYCLES = 10
trig_right=5
echo_right=6
trig_left=26
echo_left=19
trig=2
echo=3
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en_a,GPIO.OUT)
q=GPIO.PWM(en_a,100)
GPIO.setup(12,GPIO.OUT)
servo1 = GPIO.PWM(12,50)
def camera():
  cap=cv.VideoCapture(0)

  cap.set(3,640)
  cap.set(4,480)

  while True:

    _, frame = cap.read()
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    lower_green=np.array([40,70,30])
    upper_green=np.array([80,255,255])

    lower_red=np.array([0,50,50])
    upper_red=np.array([10,255,255])

    mask1=cv.inRange(hsv,lower_green,upper_green)
    mask2=cv.inRange(hsv,lower_red,upper_red)

    cnts1=cv.findContours(mask1,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    cnts1=imutils.grab_contours(cnts1)

    cnts2=cv.findContours(mask2,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    cnts2=imutils.grab_contours(cnts2)

    for c in cnts1:
        area1=cv.contourArea(c)
        if area1>5000:
            cv.drawContours(frame,[c],-1,(0,255,0),3)
            M=cv.moments(c)
            cx=int(M["m10"]/M["m00"])
            cy=int(M["m01"]/M["m00"])

            cv.circle(frame,(cx,cy),7,(255,255,255),-1)
            cv.putText(frame,"green",(cx-20,cy-20),cv.FONT_HERSHEY_SIMPLEX,2.5,(255,255,255),3)
            servo1.ChangeDutyCycle(2)
    for c in cnts2:
        area2=cv.contourArea(c)

        if area2>5000:

            cv.drawContours(frame,[c],-1,(0,255,0),3)
            M=cv.moments(c)

            cx=int(M["m10"]/M["m00"])
            cy=int(M["m01"]/M["m00"])

            cv.circle(frame,(cx,cy),7,(255,255,255),-1)
            cv.putText(frame,"red",(cx-20,cy-20),cv.FONT_HERSHEY_SIMPLEX,2.5,(255,255,255),3)
            servo1.ChangeDutyCycle(2)
    cv.imshow("result",frame)
    k=cv.waitKey(5)
    if k==27:
        break
cap.release()
cv.destroyAllWindows()
def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(s2,GPIO.OUT)
  GPIO.setup(s3,GPIO.OUT)
  print("\n")
def loop():
  temp = 1
  while(1):  

    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.LOW)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start 
    red  = NUM_CYCLES / duration   
   
    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    blue = NUM_CYCLES / duration
    

    GPIO.output(s2,GPIO.HIGH)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    green = NUM_CYCLES / duration
    
    
      
    if green<6000 and blue<10000 and red>10000:
      print("orange")
      temp=1
      servo1.ChangeDutyCycle(2)
    elif red<6000 and  blue<5000 and green<4000:
      print("blue")
      temp=1
      servo1.ChangeDutyCycle(8)
  
def endprogram():
    GPIO.cleanup()
q.start(100)
servo1.start(0)
def ultra_right():
  GPIO.setup(trig_right,GPIO.OUT)
  GPIO.setup(echo_right,GPIO.IN)
  while True:
    GPIO.output(trig_right,True)
    time.sleep(0.00001)
    GPIO.output(trig_right,False)
  while GPIO.input(echo_right)==0:
    pulse_start_right=time.time()
  while GPIO.input(echo_right)==1:
    pulse_end_right=time.time()
  pulse_duration_right=pulse_end_right -pulse_start_right
  distance_right=(pulse_duration_right*34000)/2
  dist_right =round(distance_right,2)
  print("distance right:",dist_right)
  if dist_right<=25:
    servo1.ChangeDutyCycle(2)
    time.sleep(2)
    servo1.ChangeDutyCycle(7)
time.sleep(1)

def ultra_left():

  GPIO.setup(trig_left,GPIO.OUT)
  GPIO.setup(echo_left,GPIO.IN)
  while True:
    GPIO.output(trig_left,True)
    time.sleep(0.00001)
    GPIO.output(trig_left,False)
  while GPIO.input(echo_left)==0:
    pulse_start_left=time.time()
  while GPIO.input(echo_left)==1:
    pulse_end_left=time.time()
  pulse_duration_left=pulse_end_left -pulse_start_left
  distance_left=(pulse_duration_left*34000)/2
  dist_left =round(distance_left,2)
  print("distance left:",dist_left)
  if dist_left<=25:
    servo1.ChangeDutyCycle(8)
    time.sleep(2)
    servo1.ChangeDutyCycle(7)
    
time.sleep(1)

def ultra():

  GPIO.setup(trig,GPIO.OUT)
  GPIO.setup(echo,GPIO.IN)
  while True:
    GPIO.output(trig,True)
    time.sleep(0.00001)
    GPIO.output(trig,False)
  while GPIO.input(echo)==0:
    pulse_start=time.time()
  while GPIO.input(echo)==1:
    pulse_end=time.time()
  pulse_duration=pulse_end -pulse_start
  distance=(pulse_duration*34000)/2
  dist =round(distance,2)
  print("distance :",dist)
  if dist<=25:
    servo1.ChangeDutyCycle(
