import face_recognition as f
import numpy as np
import cv2 as c
import os
import pickle as p
import keyboard
from RationCardFiles import RationShopIntegrations as ration
from tkinter import messagebox
from tkinter import *
import matplotlib.pyplot as plt

path = 'Images1'
image_dir = 'Images1'
ImageList = os.listdir(path)
Images = []
ImageName=[]
encodeListForKnownFaces = []
import json
print('Enter q to stop and exit')




with open('dataset_faces.dat', 'rb') as filedata:

    encodeListForKnownFaces = p.load(filedata)

with open('imageName.dat', 'rb') as filedata:
    ImageName.append(p.load(filedata))

a = ImageName
ImageName = ImageName[0]
a = ImageName
s= []


cap = c.VideoCapture(0)

# cap = c.VideoCapture('http://192.168.43.1:4747/mjpegfeed?640x480')
cap.set(c.CAP_PROP_FRAME_WIDTH, 1240)
cap.set(c.CAP_PROP_FRAME_HEIGHT, 980)
NameIndexList = []


def showRationDetails(name,id,dirn,alreadyBouhtL):
    ration.main(name,id,dirn,alreadyBouhtL)

bought = []
id_Name = []

nameFol = []
dirN = ""
ration_materials = []
totalList = []

# with open('rationID.json', 'r') as file:
#     id_Name = json.load(file)

with open('ration_materials.json', 'r') as file:
    ration_materials = json.load(file)['materilas']

def findID(name):
    nameFol = []
    for root, dirs, files in os.walk('Images1'):
      for dir in dirs:
          a = os.listdir('Images1/' + dir)
          for NameFolder in  a:
              if(NameFolder.upper()==name):
                  dirN = dir
                  for Nf in a:
                      nameFol.append(Nf)

                  return nameFol,dirN
      break

while True:
    if keyboard.is_pressed('q'):
        break
    NameIndexList = []
    success,image = cap.read()
    in1 = image
    image = c.flip(image, 1)
    in1 = c.flip(in1, 1)
    imgSmall = c.resize(image, (0, 0), None, 0.25, 0.25)
    imgSmall = c.cvtColor(imgSmall, c.COLOR_BGR2RGB)

    facesCurrentImage = f.face_locations(imgSmall)
    encodeCurrentFrame = f.face_encodings(imgSmall, facesCurrentImage,model='large')
    landmarks = f.face_landmarks(imgSmall,facesCurrentImage)

    landmarks = landmarks[0]
    for part in landmarks:
        parts =  landmarks[part]
        for p in  parts:
            x, y = p
            x = x * 4
            y = y * 4
            c.circle(in1, (x, y), 4, (255, 0, 0), -1)
            # c.imshow("image", image)

    if landmarks is not  None:
       c.imwrite('Landmarks.png',in1)

    # print(landmarks.part(0).x)
    c.imshow("image", image)

    for encodefac,faceloc in zip(encodeCurrentFrame,facesCurrentImage):
        borrowed_items = []

        NameIndexList = []

        matches = f.compare_faces(encodeListForKnownFaces,encodefac)
        faceDis = f.face_distance(encodeListForKnownFaces ,encodefac)

        match = np.argmin(faceDis)
        currentName = ImageName[match].upper()


        for i in range (0,len(ImageName)):
            name = ImageName[i]
            if(name.upper()==currentName):
                NameIndexList.append(i)

        with open('rationID.json', 'r') as file:
            id_Name = json.load(file)

        if(len(NameIndexList)>1):

            count = 0
            NameIndexListLength = len(NameIndexList)
            # if (NameIndexListLength - count == 0 or NameIndexListLength - count < 2):

            for i in range(0, len(NameIndexList)):
                if (matches[NameIndexList[i]] == True):
                    count = count + 1

            with open('bought.json', 'r') as file:
                bought = json.load(file)['bought']['names']

            if (NameIndexListLength - count == 0 or (NameIndexListLength/2) < count):

                 if matches[match]:

                    name = ImageName[match].upper()
                    family_members,dirN = findID(name)

                    i = 0
                    totalList = []
                    for na in family_members:
                        for n1 in bought:

                          if n1.upper() == na.upper():

                              i =1
                              borrowed_items = id_Name['ration id'][dirN]
                              totalList = []
                              for k in ration_materials:
                                  if ration_materials[k]["available"]=="1":
                                      totalList.append(k)


                              if(len(totalList) == len(borrowed_items) or len(borrowed_items)>len(totalList)):

                                  root = Tk()
                                  # root = Toplevel()


                                  # root.withdraw()
                                  messagebox.showinfo("Error", "This ID is already purchased")
                                  print('Already Bought!!')
                                  root.destroy()
                                  # exit()
                              else:


                                  showRationDetails(name, id_Name, dirN,borrowed_items)

                              break
                    if i == 0:
                        showRationDetails(name,id_Name,dirN,borrowed_items)
                    i = 0
                    y1, x2, y2, x1 = faceloc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    c.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    c.rectangle(image,(x1,y2-35),(x2,y2),(0,255,0),c.FILLED)
                    # c.rectangle(image, (x1 - 10, y2 - 30), (x2 + 10, y2 + 30), (0, 255, 0), c.FILLED)

                    c.putText(image, name, (x1 -6, y2 -6), c.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                    print("Found a Face of " + name)

        else:

            if matches[match]:

                name = ImageName[match].upper()
                family_members, dirN = findID(name)

                i = 0
                # for n1 in bought:
                #     if(name ==n1.upper()):
                #         i = i+1
                # for na in family_members:
                #     if name == na.upper():
                #         i=i+1
                totalList = []
                for na in family_members:
                    for n1 in bought:

                        if n1.upper() == na.upper():
                            i = 1
                            borrowed_items = id_Name['ration id'][dirN]

                            for k in ration_materials:
                                if ration_materials[k]["available"] == "1":
                                    totalList.append(k)

                            if (len(totalList) == len(borrowed_items) or len(borrowed_items)>len(totalList)):
                                root = Tk()
                                # root = Toplevel()

                                messagebox.showinfo("Error", "This ID is already purchased")
                                print('Already Bought!!')
                                root.destroy()

                                # exit()
                            else:


                                showRationDetails(name, id_Name, dirN, borrowed_items)

                            break
                if i == 0:
                    showRationDetails(name, id_Name, dirN, borrowed_items)
                i = 0
                y1, x2, y2, x1 = faceloc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                c.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                c.rectangle(image,(x1,y2-35),(x2,y2),(0,255,0),c.FILLED)
                    # c.rectangle(image, (x1 - 10, y2 - 30), (x2 + 10, y2 + 30), (0, 255, 0), c.FILLED)

                c.putText(image, name, (x1-6, y2-6), c.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                print("Found a Face of " + name)

        borrowed_items = []



            # print(name)

    c.imshow("image",image)
    c.waitKey(1)
    key = c.waitKey(1)
    if (key == ord('1')):
        break
cap.release()
