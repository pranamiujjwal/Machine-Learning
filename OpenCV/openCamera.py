import cv2

def openCamera():
  """ open webcamera """
  camera=cv2.VideoCapture(0)
  print("Press q to quit..")
  while camera.isOpened():
    rate,frame = camera.read()
    if not rate:
      print("Can't receive frame (stream end?). Exiting ...")
      break
    cv2.imshow('output window',frame)
    if cv2.waitKey(1)==ord('q'):
      break
  camera.release()
  cv2.destroyAllWindows()

if __name__=="__main__":
  openCamera()
