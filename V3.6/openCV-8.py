import cv2
print(cv2.__version__)
width=640
height=370
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,  frame = cam.read()
    #Create a region of interest.
    frameROI=frame[150:210,250:390]
    cv2.imshow('my ROI', frameROI)
    cv2.moveWindow('my ROI', 650, 0) #This makes sure it's not underneath the normal window.
    #Gray scale has 1 data point per pixel. Normal has 3 data points per pixel. More quickly able to analize it.
    
    #normal stuff
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()