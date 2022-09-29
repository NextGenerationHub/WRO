# WRO Future Engineers  
# Next Generation
We are Hala W , Hala D and Taha the palestinian team members who build and Programmed our own self-driving car to participate in WRO competition .

# Some of the used equipments 
1. raspberry pi 4 : the car's main microcontroller.
2. raspberry pi camera : to recognize the traffic sign color.
3. DC motor(3v) : to drive the car.(on the Rear wheels)
4. servo motor : to control the direction.(on the front wheels)
5. motor driver : to control the DC motor.
6. light sensor : to recognize the orange and blue lines on the path.
7. ultrasonic sensor : to keep the car on the right path.

# Description
We programmed the car to start moving when the key is "ON" so that the raspberry is taken power from the power-bank , then the car will move forward until the light sensor senses the orange line (if it was clockwise) and blue (if it was anticlockwise) so the servo will moves in an angle and turn the car direction 90 degree
this is in the qualification stage .
for the final Stage the camera will see the traffic sign so when the traffic sign is red the car will go right but if its green the servo motor "steering" will go left.

# code explanation 
we have imported mutible libraries sucg as : "RPi.GPIO" "cv2" "numpy" "amutils" and "time".
1.for the motor driver PINS : 
1.1.in1 --> GPIO20 
1.2.in2 --> GPIO16
1.3.en_a --> GPIO21
2.and for the color sensor PINS : 
2.1.s2 --> GPIO27
2.2.s3 --> GPIO22
2.3.signal(out) --> GPIO17
2.4.NUM_CYCLES --> GPIO10
3.for the first ultrasonic sensor PINS:
3.1.trig --> GPIO5
3.2.echo --> GPIO6
4.for the Second ultrasonic sensor PINS:
4.1trig --> GPIO26
4.2echo --> GPIO19
5.for the frontal ultrasonic sensor PINS:
5.1trig --> GPIO2
5.2echo --> GPIO3
6.then for the servo motor PIN :
6.1.DATA --> GPIO23

*all the previous equipments were also connected to a 9V battery*
for more information about wires coniction , check the "diagram" picture.
for more information aboyt the code , check the "code" file.







 
 # 
