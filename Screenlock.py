import numpy as np  #numpy library as np
import cv2       #openCv library
import pyautogui  #pyautogui 
from time import sleep  #time library 

pyautogui.FAILSAFE = False   #pyautogui failsafe to false (see doc)

#location of opencv haarcascade <change according to your file location>
face_cascade = cv2.CascadeClassifier('E:\\face_recognization\\opencv\\sources\\data\haarcascades\\haarcascade_frontalface_default.xml') 
cap = cv2.VideoCapture(0)   # 0 = main camera , 1 = extra connected webcam and so on.
rec = cv2.face.EigenFaceRecognizer_create()


rec.read("E:\\Git Folders\\OpenCV_Screen_Locking\\recognize\\training.yml")  #yml file location <change as yours>
id = 0  #set id variable to zero

font = cv2.FONT_HERSHEY_COMPLEX 
col = (255, 0, 0)
strk = 2 
while True:  #This is a forever loop
    ret, frame = cap.read() #Capture frame by frame 
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #change color from BGR to Gray
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #print(faces)
    for(x, y, w, h) in faces:
        #print(x, y, w, h)
        roi_gray = gray[y: y+h, x: x+w]  #region of interest is face

        #*** Drawing Rectangle ***
        color = (255, 0, 0)
        stroke = 2
        end_cord_x = x+w
        end_cord_y = y+h
        cv2.rectangle(frame, (x,y), (end_cord_x, end_cord_y), color, stroke)

        #***detect
        id, conf = rec.predict(roi_gray)
        #cv2.putText(np.array(roi_gray), str(id), font, 1, col, strk)
        print(id) #prints the id's

        profile = getProfile(id)
            
        if(value == 1):
                print("Authorized")

        else:
            print("UnAuthorized")
            #execute lock command
            pyautogui.hotkey('win', 'r')   #win + run key combo
            pyautogui.typewrite("cmd\n")   # type cmd and 'Enter'= '\n'
            sleep(0.500)       #a bit delay <needed!>
            #windows lock code to command prompt and hit 'Enter'
            pyautogui.typewrite("rundll32.exe user32.dll, LockWorkStation\n")    

        
        '''if id == 1:      #if authorized person 

            print("Authorized Person\n") #do nothing

        elif id != 1: 
            #execute lock command
            print("UnAuthorized")


            pyautogui.hotkey('win', 'r')   #win + run key combo
            pyautogui.typewrite("cmd\n")   # type cmd and 'Enter'= '\n'
            sleep(0.500)       #a bit delay <needed!>
            #windows lock code to command prompt and hit 'Enter'
            pyautogui.typewrite("rundll32.exe user32.dll, LockWorkStation\n") '''


        
    
    cv2.imshow('ChikonEye', frame)

    #check if user wants to quit the program (pressing 'q')
    if cv2.waitKey(10) == ord('q'):
        x = pyautogui.confirm("Close the Program 'Screen_locking'?") 
        if x == 'OK':
            break

cap.release()
cv2.destroyAllWindows() #remove all windows we have created
