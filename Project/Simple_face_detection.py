###THIS SCRIPT RUNS A PROGRAM THAT ALLOWS US TO DETECT FACES USING OPEN CV 

##import the libraries 
import pathlib #to find the file 
import cv2

##we use casscade filters to detect faces inside images 
cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"

print(cascade_path) #this is the path where cv2 has the models 

##building a classifier to detect faces 
clf = cv2.CascadeClassifier(str(cascade_path)) ##this model is what is going to find faces in our image data 

##using a loop to keep it active all the time  and detect via camera in real time 
'''
##the file to activate the camera here (1 camera  = 0)
camera = cv2.VideoCapture(0) ##this will use the default laptop camera 

while True:
    _, frame = camera.read()  ##frame will contain the data from the camera 
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) ##first converting the images to gray scale 
    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors= 4, ##the higher the number the more strict the face finding criteria while the less the number the less strict(more likely to classify non faces as faces )
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    ) ##this is what is going to find the faces in the data 

    ##creating a rectangular colored box around the faces detected 
    for(x,y,width,height) in faces:
        cv2.rectangle(frame, (x,y),(x+width,y+height), (255,255,0), 2 )
      #plot a rectangle on the face in frame at position x,y until position x+width, y+height of color (255,255,0) ##BGR scale and a thickness of 2 
    cv2.imshow("Faces",frame) ##showing the colored frame now 

    if cv2.waitKey(1) == ord("q"): ##wait one milisecond and if the key pressed is q 
        break ##we will break out the loop 

camera.release() ##release the camera 
cv2.destroyAllWindows() ##destroy all the open cv2 windows 
'''


##using a loop to keep it active all the time  and detect from video data in mp4 
vidData = cv2.VideoCapture("SOMETHING NEW (FT. CRYSTAL MILLS).mp4")

while True:
    _, frame = vidData.read()  ##frame will contain the data from the camera 
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) ##first converting the images to gray scale 
    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors= 6, ##the higher the number the more strict the face finding criteria while the less the number the less strict(more likely to classify non faces as faces )
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    ) ##this is what is going to find the faces in the data 

    ##creating a rectangular colored box around the faces detected 
    for(x,y,width,height) in faces:
        cv2.rectangle(frame, (x,y),(x+width,y+height), (255,255,0), 2 )
      #plot a rectangle on the face in frame at position x,y until position x+width, y+height of color (255,255,0) ##BGR scale and a thickness of 2 
    cv2.imshow("Faces",frame) ##showing the colored frame now 

    if cv2.waitKey(1) == ord("q"): ##wait one milisecond and if the key pressed is q 
        break ##we will break out the loop 

vidData.release() ##release the camera 
cv2.destroyAllWindows() ##destroy all the open cv2 windows 













































