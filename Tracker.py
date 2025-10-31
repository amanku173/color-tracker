import cv2
import numpy as np # importing open cv (for computer vision) and numpy for color manipulation and some additional maths

cam = cv2.VideoCapture(0)

track_green = False # sets our initial tracker to track blue

while True :
    ret, frame = cam.read()
    if not ret:
        break
    frame = cv2.flip(frame,1) # opens webcam and flips the image for convinience

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # convert BGR to HSV for tracking

    l=np.array([94,80,2])
    h=np.array([126,225,225])
    mask1=cv2.inRange(hsv, l , h) # determining hue , saturation , value for blue 

    l1=np.array([35,100,100])
    h2=np.array([70,225,225])
    mask2=cv2.inRange(hsv , l1 , h2) # determining hue , saturation , value for green

    if track_green:
        result=cv2.bitwise_and(frame, frame , mask = mask2) # to enable the tracker to track green
    else:
        result=cv2.bitwise_and(frame, frame, mask=mask1)

    cv2.imshow("webcam",frame)
    cv2.imshow("tracker",result) # shows webcam and tracker
        
    key = cv2.waitKey(1) & 0xFF # sets key value 

    if key == ord('q'):
        break

    elif key == ord('g'):
        track_green = not track_green # enables track_green in line no 24
       

cam.release()
cv2.destroyAllWindows()
