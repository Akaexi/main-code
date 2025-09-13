import cv2
from cvzone.HandTrackingModule import HandDetector

import pyfirmata

comport = 'COM12'
board = pyfirmata.Arduino(comport)

led_1 = board.get_pin('d:8:o')
led_2 = board.get_pin('d:9:o')
led_3 = board.get_pin('d:10:o')
led_4 = board.get_pin('d:11:o')
led_5 = board.get_pin('d:12:o')

# Tambahkan pin servo (misal pin 6)
servo = board.get_pin('d:6:s')  # 's' untuk servo

def led(fingerUp):
    if fingerUp==[0,0,0,0,0]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)

    elif fingerUp==[0,1,0,0,0]:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp==[0,1,1,0,0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)    
    elif fingerUp==[0,1,1,1,0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp==[0,1,1,1,1]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    elif fingerUp==[1,1,1,1,1]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)

def move_servo(fingerUp):
    # Hitung jumlah jari yang terangkat
    count = sum(fingerUp)
    # Mapping jumlah jari ke sudut servo (0-180)
    angle = int((count / 5) * 180)
    servo.write(angle)

detector = HandDetector(detectionCon=0.8, maxHands=1)
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(frame)
    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)

        print(fingerUp)
        led(fingerUp)
        move_servo(fingerUp)  # Tambahkan ini untuk menggerakkan servo

        if fingerUp==[0,0,0,0,0]:
            cv2.putText(frame,'Finger count:0',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[0,1,0,0,0]:
            cv2.putText(frame,'Finger count:1',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)    
        elif fingerUp==[0,1,1,0,0]:
            cv2.putText(frame,'Finger count:2',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[0,1,1,1,0]:
            cv2.putText(frame,'Finger count:3',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[0,1,1,1,1]:
            cv2.putText(frame,'Finger count:4',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[1,1,1,1,1]:
            cv2.putText(frame,'Finger count:5',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA) 

    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break
                                                                            #fadhil code
video.release()
cv2.destroyAllWindows()
