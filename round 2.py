import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

def mask_creator(frame, key):
    lower = {'red':(166, 84, 141), 'green':(66, 122, 129), 'blue':(97, 100, 117), 'yellow':(23, 59, 119) }#'orange':(0, 50, 80)} #assign new item lower['blue'] = (93, 10, 0)
    upper = {'red':(186,255,255), 'green':(86,255,255), 'blue':(117,255,255), 'yellow':(54,255,255)}# 'orange':(20,255,255)}

    frame = imutils.resize(frame, width=600)

    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    kernel = np.ones((9,9),np.uint8)
    mask = cv2.inRange(hsv, lower[key], upper[key])
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    return mask

cap = cv2.VideoCapture(0)

# objective() returns the current objective color to pop
while (color=objective()!= 'done'):

    while True:
        ret, frame = cap.read()
        
        #mask_creator() create a 'mask_color' to detect objective 'color'
        mask_color = mask_creator(frame, color)
        #mask_pin variable for the detection of robot's pin
        mask_pin = mask_color(frame, pin_color)

        #finding the contors of the given color
        cnts_color = cv2.findContours(mask_color.copy(), cv2.RETR_EXTERNAL,
                                      cv2.CHAIN_APPROX_SIMPLE)[-2]
        #finding the contor of the robot pin
        cnt_pin = cv2.findCoutours(mask_pin.copy(), cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)[-2]
        

        
