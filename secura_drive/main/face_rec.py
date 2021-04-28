import os
import cv2
import face_recognition
import datetime

def getUsers(username):
    if(os.path.exists(username)):
        return True
    else:
        return False

def getUserList(): # gives list of all users from the log
    if(os.path.exists('log.txt')):
        file=open('log.txt','r')
        file_list=[]
        for i in file:
            file_list.append(i[:-1])
        if(len(file_list)==0):
            file.close()
            return([])
        else:
            file.close()
            return(file_list)
    else:
        print('Log File Absent')
        return False

def addUserLog(username): # adds a new user to the log of users
    if(os.path.exists('log.txt')):
        userList=getUserList()
        if(username in userList):
            print('username Already Exists')
            return False
    if(os.path.exists('log.txt')==False):
        file1 = open("log.txt", "w")
        file1.close()
    file1= open("log.txt", "a")
    username+='\n'
    file1.write(username)
    file1.close()
    return True

def containsFace(filename): # check if the added image contains only one face also rejects deepfakes
#     face_cascade=cv2.CascadeClassifier('assets/haarcascade_frontalface_default.xml')
#     img=cv2.imread(filename,0)
#     face_rect=face_cascade.detectMultiScale(img,scaleFactor=1.05,minNeighbors=5)
    image = face_recognition.load_image_file(filename)
    face_locations = face_recognition.face_locations(image)
    print(face_locations)
    if(len(face_locations)==1):
        return True
    else:
        return False
    
def save_user(imgPath,username,flag=False): # save the image and also update log if user is unique username
    if(not containsFace(imgPath) and not flag):
        print('Invalid Image! Please Retry')
        return False
    if(not addUserLog(username)and not flag):
        print('Invalid Username! Please Retry')
        return False
    img_name=datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")+'.jpg'
    if(not os.path.exists(username)):
        os.umask(0)
        os.mkdir(os.getcwd()+'\\'+username,mode=0o777)
    img_name=username+'\\'+img_name
    image = cv2.imread(imgPath)
    cv2.imwrite(img_name, image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    return True

def authenticateUser(imgPath,username): # checks match for uploaded pic with saved users
    if(username not in getUserList()):
        print('username not in Log')
        return False
    if(not containsFace(imgPath)):
        print('no face detected')
        return False
    if(not getUsers(username)):
        print('No face data Found')
        return False
    KNOWN_FACES_DIR=username
    TOLERANCE=0.475
    FRAME_THICKNESS=3
    FONT_THICKNESS=2
    MODEL='hog'
    known_faces=[]
    print('Loading Known Faces...')
    for name in os.listdir(KNOWN_FACES_DIR):
        image=face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}')
        face_encoding=face_recognition.face_encodings(image)[0]
        known_faces.append(face_encoding)
    image=face_recognition.load_image_file(imgPath)
    locations=face_recognition.face_locations(image,model=MODEL)
    encodings=face_recognition.face_encodings(image,locations)
    for face_encoding,face_location in zip(encodings,locations):
        results=face_recognition.compare_faces(known_faces,face_encoding,TOLERANCE)
        match=None
        if True in results:
            save_user(imgPath,username,flag=True)
            return True
        else:
            return False

# save_user('known_faces/gates(3).jfif','BillGates')
# authenticateUser('unknown_faces/Gates(2).jfif','BillGates')
# authenticateUser('unknown_faces/gates_fake.jpg','BillGates')