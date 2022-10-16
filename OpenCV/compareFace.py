import cv2
import face_recognition

def compareFaces(path0,path1):
  """ Program to compare faces in two images """
  
  image=face_recognition.load_image_file(path0)   #load the image
  image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB) #convert it
  image0_encoding=face_recognition.face_encodings(image)[0] #finding encodes for the known images

  image1=face_recognition.load_image_file(path1)   #load image1
  image1=cv2.cvtColor(image1,cv2.COLOR_BGR2RGB) #convert image1
  image1faceLoc=face_recognition.face_locations(image1) #testface location
  image1_encoding=face_recognition.face_encodings(image1) #test face encodes
  
  #comparing both image encodes for similarities
  for i in range(len(image1_encoding)):
    result=face_recognition.compare_faces([image0_encoding],image1_encoding[i])
    if i<len(image1faceLoc):
      facedistance=face_recognition.face_distance([image0_encoding],image1_encoding[i])
      print(result,facedistance)
      if result[0] == True and round(facedistance[0])<0.5:
        fileName=path0.split("\\")[-1]
        fileName=fileName.split(".")[0]
        cv2.rectangle(image1,(image1faceLoc[i][3],image1faceLoc[i][0]),(image1faceLoc[i][1],image1faceLoc[i][2]),(0,255,0),2)
        cv2.putText(image1,fileName,(image1faceLoc[i][3],image1faceLoc[i][0]),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
      else:
        cv2.rectangle(image1,(image1faceLoc[i][3],image1faceLoc[i][0]),(image1faceLoc[i][1],image1faceLoc[i][2]),(0,0,255),2)
        cv2.putText(image1,"Unknown",(image1faceLoc[i][3],image1faceLoc[i][0]),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)
  cv2.imshow("Output Image",image1)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
      
if __name__=="__main__":
  path0=input("Enter image0 path: ")
  path1=input("Enter image1 path: ")
  compareFaces(path0,path1)
