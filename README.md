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

# About code 
we have imported mutible libraries sucg as : "RPi.GPIO" "cv2" "numpy" "imutils" and "time".

# Usage
The first library we used is "RPi.GPIO", to to control the raspberry PINS connections.
The second library we used is "cv2", wich is the main library to control the car actions.
The third library we used is "numpy", to make the camera recognize the color of the traffic signs on the track.
The fourth library we used is "imutils", it supports the other libraries work perfictly . 
The last library we used is "time", to organize the car movement on the track . 
# RASPBERRY PI PINS connections 
1. for the motor driver PINS :                                                                                                                                       
1.1. in1 --> GPIO20 .                                                                                                                                                 
1.2. in2 --> GPIO16.                                                                                                                                             
1.3. en_a --> GPIO21.                                                                                                                          
2. and for the color sensor PINS :                                               
2.1. s2 --> GPIO27.                                                                                                                 
2.2. s3 --> GPIO22.                                                                                                                                           
2.3. signal(out) --> GPIO17.                                                                                                                    
2.4. NUM_CYCLES --> GPIO10.                                                                                                                       
3. for the first ultrasonic sensor PINS:                                                                                                                   
3.1. trig --> GPIO5.                                                                                                                     
3.2. echo --> GPIO6.                                                                                                                                            
4. for the Second ultrasonic sensor PINS:                                                                                                                          
4.1. trig --> GPIO26.                                
4. 2echo --> GPIO19.
5. for the frontal ultrasonic sensor PINS:
5.1. trig --> GPIO2.
5.2. echo --> GPIO3.
6. then for the servo motor PIN :
6.1. DATA --> GPIO23.

*all the previous equipments were also connected to a 9V battery*
For more information about wires coniction , check the "diagram" picture.
For more information about the code , check the "code" file.

# Construction Process
At first, we start collecting the hardware that we need to build the car and after that we looked hard for then we begin the building process that we thought its going to be not that hard but surprisingly there were a lot of challenges that faced us like the power supply issue, we couldn't find the suitable power bank for our micro controler .
Another proplem we faced during our work is that the raspberry went down , all our hard work just disappeared , but we fixed that proplem very quickly by formating and rebooting the raspberry , and we got our work back .
Accidetally, during the expiriminting , we destroyed our servo , it was a very bad break for our team , we almost gave up , but we put ourselves together back ,
and bought a new one at the end .
In the end , our team was very strong against all the troubles he faced , we cuoldnt go through any of these troubles with out the help of our coach and our families.

# Motivation
Our first and main reason to participate in this compittition is our passion to become a programmers , computer engineers or anything related to this field .
So each one of us had a his own self MOTIVATION that came from our ampission .
We worked really hard under tough and chalenging circumstances to raech this point and avhieve what we are looking for .





