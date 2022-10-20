import cv2
import face_recognition

def DetectLiveFace():
  """ detetct live faces on webcam """
  camera=cv2.VideoCapture(0)
  print("Press q to quit..")
  while camera.isOpened():
    rate,frame = camera.read()
    if not rate:
      print("Can't receive frame (stream end?). Exiting ...")
      break
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faceLoc=face_recognition.face_locations(gray)
    for i in range(len(faceLoc)):
      cv2.rectangle(frame,(faceLoc[i][3],faceLoc[i][0]),(faceLoc[i][1],faceLoc[i][2]),(0,255,0),2)
    cv2.imshow('output window',frame)
    if cv2.waitKey(1)==ord('q'):
      break
  camera.release()
  cv2.destroyAllWindows()

if __name__=="__main__":
  DetectLiveFace()
