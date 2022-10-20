import cv2
import numpy
import pickle
import face_recognition

def FindKnownFaces(filePath,imagePath):\
  """ Program to recognize face in given image with known face encodes from a file """
  with open(filePath,'rb') as file:
    data=pickle.loads(file.read())  #extract all nown encodes from the file
    file.close()
  image=face_recognition.load_image_file(imagePath)
  image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
  image1faceLoc=face_recognition.face_locations(image) #testface location
  image1_encoding=face_recognition.face_encodings(image) #test face encodes
  #comparing both image encodes for similarities
  for i in range(len(image1_encoding)):
    result=face_recognition.compare_faces(list(data.values()),image1_encoding[i])
    if i<len(image1faceLoc):
      facedistance=face_recognition.face_distance(list(data.values()),image1_encoding[i])
      if any(result):
        idx=numpy.argmin(facedistance)
        cv2.rectangle(image,(image1faceLoc[i][3],image1faceLoc[i][0]),(image1faceLoc[i][1],image1faceLoc[i][2]),(0,255,0),2)
        cv2.putText(image,list(data.keys())[idx],(image1faceLoc[i][3],image1faceLoc[i][0]),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
      else:
        cv2.rectangle(image,(image1faceLoc[i][3],image1faceLoc[i][0]),(image1faceLoc[i][1],image1faceLoc[i][2]),(0,0,255),1)
        cv2.putText(image,"",(image1faceLoc[i][3],image1faceLoc[i][0]),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)
  cv2.imshow("Output Image",image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__=="__main__":
  filePath=input("Enter file path: ")
  imagePath=input("Enter image path: ")
  FindKnownFaces(filePath,imagePath)
