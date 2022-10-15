import cv2

def OpenImage(path):
  """ Program to open Image using cv2 """
  imageObj=cv2.imread(path)
  cv2.imshow("Output Window",imageObj)  # it will display that image
  cv2.waitKey(0)  # hold the image until you close it
  cv2.destroyAllWindows

if __name__=="__main__":
  path=input("Enter image path: ")
  findFace(path)
