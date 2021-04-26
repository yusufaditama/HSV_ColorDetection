import cv2
import numpy as np
import time
cap=cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX

import serial

#ser = serial.Serial('COM10', 9600)
#time.sleep(2)
#print("Connected to Arduino...")

def a(x):       #VARIABEL NAMPUNG DATA HSV
    pass

cv2.namedWindow('HSVsetup')
cv2.namedWindow('camera')

cv2.createTrackbar('hmin', 'HSVsetup',0,360,a)
cv2.setTrackbarPos('hmin','HSVsetup', 102)

cv2.createTrackbar('hmax', 'HSVsetup',360,360,a)
cv2.setTrackbarPos('hmax','HSVsetup', 130)

cv2.createTrackbar('smin', 'HSVsetup',0,255,a)
cv2.setTrackbarPos('smin', 'HSVsetup', 50)

cv2.createTrackbar('smax', 'HSVsetup',255,255,a)
cv2.setTrackbarPos('smax', 'HSVsetup', 255)

cv2.createTrackbar('vmin', 'HSVsetup',0,255,a)
cv2.setTrackbarPos('vmin', 'HSVsetup',50)

cv2.createTrackbar('vmax', 'HSVsetup',255,255,a)
cv2.setTrackbarPos('vmax', 'HSVsetup', 255)
while (cap.isOpened()):
    hmin=cv2.getTrackbarPos('hmin','HSVsetup')
    hmax=cv2.getTrackbarPos('hmax','HSVsetup')
    smin=cv2.getTrackbarPos('smin','HSVsetup')
    smax=cv2.getTrackbarPos('smax','HSVsetup')
    vmin=cv2.getTrackbarPos('vmin','HSVsetup')
    vmax=cv2.getTrackbarPos('vmax','HSVsetup')
    ret, frame=cap.read()
    camera = cv2.resize(frame, (240, 240))

    hsv=cv2.cvtColor(camera, cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,(hmin,smin,vmin),(hmax,smax,vmax))
    cv2.imshow('Thresholding',mask)
    cv2.imshow('camera', camera)
    cv2.imshow('hsv', hsv)
    k=cv2.waitKey(5) & 0xFF

    data_pixel=0
    data_baru=0
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            pixel = mask.item(i, j)
            if pixel >= 255:
                data_pixel = data_pixel + 1;
                #time.sleep(0.1)
                #print(data_pixel)
                #cv2.putText(camera, str(data_pixel), (20,20), font, 0.5, (255,255,255), 1)

           # if data_pixel >= 1000 and data_pixel <=2000:
            #    data_baru=0
             #   print(data_baru)
            #if data_pixel >= 3000:
             #   data_baru=1
              #  print(data_baru)

                #if data_pixel < 1000:
                    #ser.write(b'1')
                    #print("biru")
                    #cv2.putText(camera, "0", (20,20), font, 0.5, (255,255,255), 1)
                         #   GPIO.setup(27, GPIO.OUT)
                          #  GPIO.output(27, GPIO.LOW)
                #elif data_pixel >= 1000:
                    #ser.write(b'0')
                    #print("merah")
                    #cv2.putText(camera, "1", (20,20), font, 0.5, (255,255,255), 1)
                         #   GPIO.setup(17, GPIO.OUT)
                          #  GPIO.output(17, GPIO.HIGH)


    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
