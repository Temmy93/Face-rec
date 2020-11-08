import cv2
import face_recognition
import numpy as np
import os

face_cascade = cv2.CascadeClassifier('C:\\Users\TEMMY_TOBY\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')


path ='media/student_faces'
images = []
classNames = []
myList = os.listdir(path)
print(myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0] 
        encodeList.append(encode)
    return encodeList


encodeListKnown = findEncodings(images)
print('Encoding Complete')



cap = cv2.VideoCapture(0)



while True:
    success, img =cap.read()

    #scale_percent= 50
    #width = int(img.shape[1] * scale_percent/100)
    #height = int(img.shape[0] * scale_percent/100)
    #dsize =(width, height)
    #imgS =cv2.resize(img, dsize)

    #img = cv2.rectangle (img, (x,y), (x+w, y+h), (0,255,0), 3)
    #imgS = cv2.resize(img, (int (img.shape[1]), int(img.shape[0]/2)))
    imgS =cv2.resize(img, (0,0), None, 0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    #gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors =5)


    facesCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)


        if matches[matchIndex]:
            name =classNames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img,(x1,y1), (x2,y2),(0,255,0), 2)
            cv2.rectangle(img, (x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
            #cv2.rectangle(img, (x1,y1),(x2,y2), (255, 255, 0), 2)
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
    
    
    cv2.imshow('Webcam', img)
    cv2.waitKey(0)


