import cv2
import numpy as np
import imutils

def mask_maker(frame, key):
    lower = {'red':(166, 84, 141), 'green':(66, 122, 129), 'blue':(97, 100, 117), 'yellow':(23, 59, 119) }#'orange':(0, 50, 80)} #assign new item lower['blue'] = (93, 10, 0)
    upper = {'red':(186,255,255), 'green':(86,255,255), 'blue':(117,255,255), 'yellow':(54,255,255)}# 'orange':(20,255,255)}

    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    kernel = np.ones((9,9),np.uint8)
    mask = cv2.inRange(hsv, lower[key], upper[key])
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    return mask

cap = cv2.VideoCapture(0)

cnts = 0
radius=0
'''
while(cnts==0 & radius<10):
    ret2, frame = cap.read()
    mask = mask_maker(frame, 'red')
    cnts = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        #chosen_square = cv2.circle(mask.copy(), (x,y),radius+3,[255,255,255],-1)
        
        ret3, total_black = cv2.threshold(mask.copy(), 0, 255, cv2.THRESH_BINARY_INV)
        chosen_square=cv2.circle(total_black.copy(), (x,y),radius+3,[255,255,255],-1)
        cv2.imshow('chosen-square',chosen_square)
        cv2.imshow('frame',frame)
'''
    
while True:
    ret, frame = cap.read()

    mask = mask_maker(frame, 'red')
    #selected_mask = cv2.bitwise_and(mask,mask, mask= chosen_square)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                      cv2.CHAIN_APPROX_SIMPLE)[-2]

    #c = max(cnts, key=cv2.contourArea)
    for i,c in enumerate(cnts):
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    
        # only proceed if the radius meets a minimum size. Correct this value for your obect's size
        if radius > 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius), [0,255,0], 2)
            print(i,' : [',int(x),",",int(y),']', 'radius = ', radius)
            cv2.putText(frame,"red ball", (int(x-radius),int(y-radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,[0,255,255],2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

