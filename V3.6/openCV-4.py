import cv2
print(cv2.__version__)
rows=int(input("Boss, how many rows ya want?"))
columns=int(input("What about the columns?"))
width=1280
height=720
cam=cv2.VideoCapture(1,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter(*'MJPG'))

while True:
    ignore, frame = cam.read()
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)
    if cv2.waitKey(1) & oxff ==ord('q'):
        break
cam.release()