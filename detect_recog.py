import cv2
import numpy as np
import pyautogui
from time import sleep
from PIL import Image
import os
import sqlite3
import glob

#location of opencv haarcascade <change according to your file location>
face_cascade = cv2.CascadeClassifier("E:\\face_recognization\\opencv\\sources\\data\haarcascades\\haarcascade_frontalface_default.xml") 
cap = cv2.VideoCapture(0)   # 0 = main camera , 1 = extra connected webcam and so on.
rec = cv2.face.LBPHFaceRecognizer_create()

'''
def insertOrUpdate(Id, Name):
    conn = sqlite3.connect("E:\\Git Folders\\OpenCV_Screen_Locking\\FaceData.db")
    cmd = "SELECT * FROM Data WHERE ID = "+ str(Id)
    cursor = conn.execute(cmd)
    isRecordExit = 0
    for row in cursor:
        isRecordExit = 1

    if(isRecordExit == 1):
        cmd = "UPDATE Data SET Name" + str(Name) + "WHERE ID =" + str(Id)

    else:
        cmd = "Insert into Data(ID,Name) Values (" +str(Id) + "," +str(Name)+ ")"

    conn.execute(cmd)
    conn.commit()
    conn.close()



#recogizer module
def getProfile(id):

    conn = sqlite3.connect("E:\\Git Folders\\OpenCV_Screen_Locking\\FaceData.db")
    cmd = "SELECT * FROM Data WHERE ID =" + str(id)

    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile


def getID(path1):

    imagePaths = [os.path.join(path1, f) for f in os.listdir(path1)]

    for imagepath in imagePaths:

        faceImg = Image.open(imagepath).convert("L")
        faceNp = np.array(faceImg, 'uint8')

        ID = int(os.path.split(imagepath)[-1].split('.')[1])

        return ID'''


def recog():
    
    
    rec.read("E:\\Git Folders\\OpenCV_Screen_Locking\\recognize\\training.yml")  #yml file location

    
    '''Id = pyautogui.prompt(text="""
    Enter User ID.\n\nnote: numeric data only.""", title='ChikonEye', default='none')'''
    #check for user input
    
    #Id = 1 #set id variable to zero

    font = cv2.FONT_HERSHEY_SIMPLEX 
    
    while True:  
        ret, frame = cap.read() #Capture image by image 
    
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

            
            cv2.waitKey(100)

            cv2.imshow("Face", frame)

            #***detect
            id, conf = rec.predict(roi_gray)
            #cv2.putText(np.array(roi_gray), str(id), font, 1, col, strk)
            #print(id) #prints the id's
            #value = profile[1]
    

            list_img =[]
            directory = "E:\\Git Folders\\OpenCV_Screen_Locking\\dataSet"
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith('.jpg'):
                        print (list_img.append(file))

            for sample in range(1, 31):
                final_add = str(id) + "User." + "1." + str(sample) + ".jpg"
            print(final_add)
            
            #img = glob.glob('E:\\Git Folders\\OpenCV_Screen_Locking\\dataSet\\*.jpg')[0].split("\\")[-1]
            
            #img_id = img.split(".")[1]
            
            #final_id = int(img_id)
            
            if(final_add not in file):

                print("UnAuthorized")
                #execute lock command
                pyautogui.hotkey('win', 'r')   #win + run key combo
                pyautogui.typewrite("cmd\n")   # type cmd and 'Enter'= '\n'
                sleep(0.500)       #a bit delay <needed!>
                #windows lock code to command prompt and hit 'Enter'
                pyautogui.typewrite("rundll32.exe user32.dll, LockWorkStation\n")    

            
            else:

                print("Authorized")

                

            '''if id == 1:      #if authorized person 
                print("Authorized Person\n") #do nothing

            #if sees unauthorized person
            elif id != 1: 

                print("UnAuthorized")
                #execute lock command
                pyautogui.hotkey('win', 'r')   #win + run key combo
                pyautogui.typewrite("cmd\n")   # type cmd and 'Enter'= '\n'
                sleep(0.500)       #a bit delay <needed!>
                #windows lock code to command prompt and hit 'Enter'
                pyautogui.typewrite("rundll32.exe user32.dll, LockWorkStation\n")''' 


        
    
        cv2.imshow('Face', frame)

        #check if user wants to quit the program (pressing 'q')
        if cv2.waitKey(10) == ord('q'):
            op = pyautogui.confirm("Close the Program 'Recognition'?") 
            if op == 'OK':
                print("Out")
                break
            
                

    cap.release()
    cv2.destroyAllWindows() #remove all windows we have created




#create dataset and train the model
def data_Train():
    sampleNum = 0
    #print("Starting training")
    id = pyautogui.prompt(text="""
    Enter User ID.\n\nnote: numeric data only.""", title='ChikonEye', default='none')
    #check for user input
    
    """
    if id >  :
        print(id)
        pyautogui.alert(text='WRONG INPUT',title='ChikonEye',button='Back')
        recog()
    """

    #if user input is 1 2 or 3  max 5 here <you can change that.>
    if id != '1' and id != '2' and id != '3' and id != '4' and id != '5':
        pyautogui.alert(text='WRONG INPUT',title='ChikonEye',button='Back')
        recog()

    else:
        #let, the input is okay
        while True:
            
            
            ret, img = cap.read()  
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for(x, y, w, h) in faces: #find faces
                sampleNum = sampleNum + 1  #increment sample num till 21
                cv2.imwrite("E:\\Git Folders\\OpenCV_Screen_Locking\\dataSet\\User." + str(id) + "." + str(sampleNum) + ".jpg", gray[y: y+h, x: x+w]) 
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)

                cv2.waitKey(100)

            cv2.imshow('Face', img)  #show image while capturing
            cv2.waitKey(1)
            if(sampleNum > 30): 
                break   
            
    trainer() #Train the model based on the new images

    recog() #starts recognizing
            


#Trainer 
def trainer():
    faces = []   #empty list for faces
    Ids = [] #empty list for IDs

    path = "E:\\Git Folders\\OpenCV_Screen_Locking\\dataSet"

    #gets image id with path
    def getImageWithID(path):

        

        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
        
    
        for imagePath in imagePaths:
            
            faceImg = Image.open(imagePath).convert('L')
            
            #cv2.imshow('faceImg', faceImg)
            faceNp = np.array(faceImg, 'uint8')

            ID = int(os.path.split(imagePath)[-1].split('.')[1])
            #print(ID)
            faces.append(faceNp)
            Ids.append(ID)

            cv2.waitKey(10)

        return np.array(Ids), faces


    ids, faces = getImageWithID(path)

    #print(ids, faces)
    rec.train(faces, ids)

    #create a yml file at the folder. WIll be created automatically.
    rec.save("E:\\Git Folders\\OpenCV_Screen_Locking\\recognize\\training.yml")   
    pyautogui.alert("Done Saving.\nPress OK to continue")
    cv2.destroyAllWindows()
    

#Options checking
opt =pyautogui.confirm(text= 'Chose an option', title='ChikonEye', buttons=['START', 'Train', 'Exit'])
if opt == 'START':
    #print("Starting the app")
    recog()
    
if opt == 'Train':
    opt = pyautogui.confirm(text="""
    Please look at the Webcam.\nTurn your head a little while capturing.\nPlease add just one face at a time.
    \nClick 'Ready' when you're ready.""", title='ChikonEye', buttons=['Ready', 'Cancel'])
        
    if opt == 'Ready':
            #print("Starting image capture + Training")
            data_Train()
    if opt == 'Cancel':
        print("Cancelled")
        recog()
        

if opt == 'Exit':
    print("Quit the app")
    
