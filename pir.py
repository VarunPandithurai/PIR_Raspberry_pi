Copyright (c) <2020> <copyright Varun Pandithurai>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


import RPi.GPIO as GPIO #Import GPIO library
import time #Import time library 

#Set GPIO pin numbering 
GPIO.setmode(GPIO.BOARD) 


pir = 26 #Associate pin 26 to pir 

print "Setting Input and Output Pins" 
GPIO.setup(pir, GPIO.IN) 
GPIO.setup(8, GPIO.IN) 
 

time.sleep(2) #Waiting 2 seconds for the sensor to initiate print "Detecting motion" 

while True: 
	if GPIO.input(pir): #Check whether pir is HIGH print "Motion Detected!" 
		print "Motion Detected"
		GPIO.output(8,1)



time.sleep(2) #D1- Delay to avoid multiple detection

time.sleep(0.1) #While loop delay should be less than detection(hardware) delay
