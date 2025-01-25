import cv2
print(cv2.__version__)
# Create a camera object
cam = cv2.VideoCapture(0)
# Create an infinite loop
while True:
    # Capture frame
    ignore, frame = cam.read()
    # Create different color frames
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    labFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    # Display the frames
    cv2.imshow('Original', frame)
    cv2.imshow('Grayscale', grayFrame)
    cv2.imshow('HSV', hsvFrame)
    cv2.imshow('LAB', labFrame)
    # Move windows to create a 2x2 grid
    cv2.moveWindow('Original', 0, 0)        # Top-left
    cv2.moveWindow('Grayscale', 640, 0)    # Top-right
    cv2.moveWindow('HSV', 0, 480)          # Bottom-left
    cv2.moveWindow('LAB', 640, 480)        # Bottom-right
    # Exit condition
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
# Release resources
cam.release()
cv2.destroyAllWindows()
