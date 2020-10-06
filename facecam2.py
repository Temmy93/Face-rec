import cv2, time

video =cv2.VideoCapture(0)
check,frame = video.read()

print(check)
print(frame)

time.sleep(5)

cv2.imshow("Capture", frame)
cv2.waitKey(0)

video.release()


