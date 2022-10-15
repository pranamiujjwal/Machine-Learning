import cv2
import face_recognition

def findFace(path):
  imageObj=cv2.imread(path)
  # change the BGR to RGB
  # imageObj=cv2.cvtColor(imageObj,cv2.COLOR_BGR2RGB)
  # finding the coodinates of faces in the image
  faceLoc=face_recognition.face_locations(imageObj)
  # creating rectangles around faces
  for i in range(len(faceLoc)):
    cv2.rectangle(imageObj,(faceLoc[i][3],faceLoc[i][0]),(faceLoc[i][1],faceLoc[i][2]),(0,255,0),2)
  cv2.imshow("Output Window",imageObj)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__=="__main__":
  path=input("Enter image path: ")
  findFace(path)
