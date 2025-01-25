#Understanding Pictures and Images as Data Arrays
import cv2
print(cv2.__version__)
import numpy as np
while True:
    frame=np.zeros([250,250, 3],dtype=np.uint8)
    # frame[:,0:125]=255 #gray
    frame[:,:]=(0,0,255) #red
    frame[:,0:125]=(0,255,0) #left half green
    cv2.imshow('My Window', frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break