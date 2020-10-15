#import facial recognition librarries and associate packages
import cv2
import numpy as np
import face_recognition

#load the image 
imgtee =face_recognition.load_image_file('toby/tee.jpg')
imgtee = cv2.cvtColor(imgtee, cv2.COLOR_BGR2RGB) #convert the test image from BGR to RGB


#load the test image
imgtest =face_recognition.load_image_file('toby/temmy.jpg')
imgtest = cv2.cvtColor(imgtest, cv2.COLOR_BGR2RGB) #convert the test image from BGR to RGB

#Get face locations and image encodings
faceLoc = face_recognition.face_locations(imgtee)[0] 
encodeTee = face_recognition.face_encodings(imgtee)[0]
cv2.rectangle(imgtee, (faceLoc[3], faceLoc[0]),(faceLoc[1], faceLoc[2]), (255, 255, 0), 2) #draw a coloured rectangle on the face in the image

#Get face locations and image encodings on the test image
faceLocTest = face_recognition.face_locations(imgtest)[0]
encodeTest = face_recognition.face_encodings(imgtest)[0]
cv2.rectangle(imgtest, (faceLoc[3], faceLoc[0]),(faceLoc[1], faceLoc[2]), (255, 255, 0), 2) #draw a coloured rectangle on the face in the image

#compare the faces in the image and the test image. 
results = face_recognition.compare_faces([encodeTee], encodeTest) #Get and store the results in the variable results
faceDis = face_recognition.face_distance([encodeTee], encodeTest) #Get and store the distance in the varaible faceDis

#print the result and face distance
print(results, faceDis)
cv2.putText(imgtest, f'{results} {round(faceDis[0])}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)

#display the images in a window
cv2.imshow ('TEE', imgtee)
cv2.imshow ('TEE TEST', imgtest)
cv2.waitKey(0)

