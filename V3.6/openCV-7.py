import cv2
print(cv2.__version__)
width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,  frame = cam.read()
    frame[140:220, 280:350]=(0,0,0) #This is the rectangle
    cv2.rectangle(frame, (250, 140), (390, 220),(255,0,0), -1) #This is also a rectangle -1 for solid, positive num for empty shape
    cv2.circle(frame, (320,180), 25, (0, 0, 0), -1) #This is a circle. 25 is radius
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()