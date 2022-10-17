import os
import cv2
import pickle
import face_recognition

def ProcessFaces(path):
  """ Program to create a file full of known faces encodes """
  data={}
  filepath=os.path.join(path,"Known")
  if os.path.exists(filepath):
    with open(filepath,'rb') as file:
      data=pickle.loads(file.read())  #extract all nown encodes from the file
      file.close()
  i=0
  for filename in os.listdir(path):  #collect all files inside that dir
    fileName=filename.split(".")
    if fileName[-1] in ['jpg','png','jpeg']:
      print(f"processing: {fileName[0]}.{fileName[-1]} : ".ljust(40," "),end="")
      image=face_recognition.load_image_file(os.path.join(path,filename))
      image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
      encode=face_recognition.face_encodings(image)
      if len(encode)>0:
        data[fileName[0]]=encode   #generating a dictionary with key value 'i' and value a list[encode,name]
        print("completed;")
      else:
        print("not completed;")
    if len(data.keys())>0:
      f=open(filepath,'wb')
      f.write(pickle.dumps(data))
      f.close()


if __name__=="__main__":
  path=input("Enter the path of directory: ")
  ProcessFaces(path)
