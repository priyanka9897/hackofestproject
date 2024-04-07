import numpy as np
import cv2
import time


from pushbullet import Pushbullet
import pygame
#input real time audio


#giving the alert message

API_KEY ="o.dEkGxHdToZWefHTjCSqBGIXFxhMUqD0k"
file ="alertmsg.txt"

with open(file, mode='r') as f:
    text = f.read()
    pb =Pushbullet(API_KEY)
    push = pb.push_note('She needs help', text)
    
time.sleep(10)

#playing alert sound
pygame.mixer.init()
pygame.mixer.music.load('sound1.wav')
pygame.mixer.music.play()

input('enter to exit the sound : ')


#video streaming
cap=cv2.VideoCapture(0)


while True :
    _, frame=cap.read()
    

    cv2.imshow('livestream',frame)

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows    



