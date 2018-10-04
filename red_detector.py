import cv2
import numpy as np
import time
'''

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([20,50,50])
    upper_red = np.array([42,255,255])
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    blur_red = cv2.medianBlur(mask_red,5)

    cv2.imshow('mask_red',mask_red)
    cv2.imshow('blur_red',blur_red)
    cv2.imshow('frame',frame)
    

    if cv2.waitKey(1)  & 0xff==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
'''

'''
frame = cv2.imread('circles.jpg')
frame = cv2.medianBlur(frame,3)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
mask_red0 = cv2.inRange(hsv, lower_red, upper_red)

lower_red = np.array([160,50,50])
upper_red = np.array([179,255,255])
mask_red1 = cv2.inRange(hsv, lower_red, upper_red)
mask_red = cv2.addWeighted(mask_red0,1.0,mask_red1,1.0,0.0)

blur_redm = cv2.medianBlur(mask_red,15)
blur_redg = cv2.GaussianBlur(mask_red,(9,9),2,2)

# detect circles in the image
circles = cv2.HoughCircles(blur_redg, cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30)
# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
 
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		final=cv2.circle( frame,(x, y), r, (0, 255, 0), 4)
		#final=cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
cv2.imshow('final',final)
cv2.imshow('mask_red',mask_red)
#cv2.imshow('blur_redm',blur_redm)
#cv2.imshow('blur_redg',blur_redg)
#cv2.imshow('frame',frame)

'''

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.medianBlur(frame,3)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask_red0 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([160,50,50])
    upper_red = np.array([179,255,255])
    mask_red1 = cv2.inRange(hsv, lower_red, upper_red)
    mask_red = cv2.addWeighted(mask_red0,1.0,mask_red1,1.0,0.0)
    

    blur_redm = cv2.medianBlur(mask_red,15)
    blur_redg = cv2.GaussianBlur(mask_red,(9,9),2,2)
    # detect circles in the image
    circles = cv2.HoughCircles(blur_redg, cv2.HOUGH_GRADIENT,0.00000001,5,param1=50,param2=30,minRadius=0,maxRadius=0)
    # ensure at least some circles were found
    if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
     
            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                    # draw the circle in the output image, then draw a rectangle
                    # corresponding to the center of the circle
                    final=cv2.circle( frame,(x, y), r, (0, 255, 0), 4)
                    #final=cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    #cv2.imshow('final',final)

    cv2.imshow('mask_red',mask_red)
    cv2.imshow('blur_redm',blur_redm)
    cv2.imshow('blur_redg',blur_redg)
    cv2.imshow('frame',frame)
    
    

    if cv2.waitKey(1)  & 0xff==ord('q'):
        break
        
cap.release()

cv2.waitKey(0)
cv2.destroyAllWindows()
