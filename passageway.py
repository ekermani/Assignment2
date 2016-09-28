#!/usr/bin/env python

# MISSION: You have entered the library.  Find the book.  The book will be your guide.  You will receive a code to enter.  

import RPi.GPIO as GPIO
import time

# email setup
import subprocess
import smtplib
import socket
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import datetime
import urllib2

GPIO.setmode(GPIO.BOARD)
# input 1, button
GPIO.setup(7,GPIO.IN)
# LED1
GPIO.setup(11,GPIO.OUT)
# input 2, 
GPIO.setup(15,GPIO.IN)

while True:
  input = GPIO.input(7)
  input2 = GPIO.input(15)

# input 1/button
  if input == True:
    GPIO.output(11,GPIO.HIGH)
    status = 1

  # if input == False:
  # # else:
  #   GPIO.output(11,GPIO.LOW)
  #   status = 0
    print status

# GPIO.output(11,False)  
    
  if input2 == True:

    fromaddr = "tests4iot@gmail.com"
    toaddr = "tests4iot@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg ['Subject'] = "TOP SECRET MESSAGE"

    body = "Congratulations. You have successfully broken the initial code. The secret passcode is '90002027478398'. Destroy this message. Use the code to enter the door."
    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(fromaddr,'***')
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    status = 1
    # break

  # else:
  if input2 == False:
    status = 0
  print status

GPIO.cleanup()


