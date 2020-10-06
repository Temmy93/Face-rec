import cv2, time

video = cv2.VideoCapture(0)


a = 1

while True:
    a =a+1
    check, frame = video.read()
    print (frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capture", gray)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break



print(a)
#time.sleep(3)
video.release()
cv2.destroyAllWindows()

