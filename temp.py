from twilio.rest import Client
import cv2
from selenium import webdriver
#import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
sum_eyes = 0
count = 0
while 1:
    sum_eyes=0 
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]       
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        for (ex,ey,ew,eh) in eyes:             
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            sum_eyes = ex+ey+ew+eh #sum length of edges too see it detects
    if sum_eyes==0: #if it doesn't detect
          count=count+1
          print("Not found")
          if count==100:  #if it doesn't detect 100 times which takes a few seconds, if you want increment it
                
                print("Wake UP!!!!!!!!!")
                driver = webdriver.Chrome()  
                url = "https://www.youtube.com/watch?v=4rsXvmv7ty0&list=PLDIoUOhQQPlVr3qepMVRsDe4T8vNQsvno"
                driver.get(url) #that opens pop music to wake you up
                print(driver.title)
# the following line needs your Twilio Account SID and Auth Token         
                client = Client("AC2d1e4d3012ba8e4cb4f21356772e971d", "3fb906f382a85ef77f0ee1ce88d24f92")
# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number    
                client.messages.create(to="+905313200699", 
                       from_="+12058436069", 
                       body="Wake Uppp")
    else:
          print("Found")
        

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
