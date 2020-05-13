from twilio.rest import Client
import cv2
from selenium import webdriver
#import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
count = 0
count2 = 0
sum_eyes = 0
min_of_sum = 0
detection = 0
while 1:
     
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    detection = min_of_sum
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]       
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        for (ex,ey,ew,eh) in eyes:             
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                
        sum_eyes = sum(eyes)
        min_of_sum = min(sum_eyes)
    if min_of_sum==detection:  #if min_of_sum stays same which means it doesnt detect eyes
          count2=count2+1
    if count2==200:  #if eyes cannot be detected 200 time which takes 6-7 seconds
          print("Wake UP!!!!!!!!!")
          driver = webdriver.Chrome()
          url = "https://www.youtube.com/watch?v=4rsXvmv7ty0&list=PLDIoUOhQQPlVr3qepMVRsDe4T8vNQsvno"
          driver.get(url)
          print(driver.title)
          # the following line needs your Twilio Account SID and Auth Token
          client = Client("AC2d1e4d3012ba8e4cb4f21356772e971d", "8567dc1fc2613abc5cf40aa04a4e909f")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
          client.messages.create(to="+905313200699", 
                       from_="+12058436069", 
                       body="Wake Uppp")

    count=count+1
    
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()






























