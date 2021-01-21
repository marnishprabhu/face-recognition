import random
import os
import face_recognition as f
import cv2 as c
sampleNum = 0
ration_unique_id = (input("Enter the ration id "))
image_dir = 'Images1'
def checkforid(ration_unique_id):
    for root, dirs, files in os.walk(image_dir):
        for dir in dirs:
            if dir == ration_unique_id:
                return True
        return False
while True:
    if not ration_unique_id == "":
        ImagePath = 'Images1/' + ration_unique_id
        break

    for i in range(0, 30):
        n = random.randint(0, 9)
        ration_unique_id = ration_unique_id + (str(n))

    if not checkforid(ration_unique_id):
        ImagePath = 'Images1/' + ration_unique_id
        os.mkdir(ImagePath)
        break
    else:
        ration_unique_id =""

# if ration_unique_id=="":
#     ration_unique_id = createIDFolder()
#     isalreadypresent = checkforid(ration_unique_id)
#
#     if not isalreadypresent:
#       ImagePath = 'Images1/' + ration_unique_id
#       os.mkdir(ImagePath)
#     else:
#         createIDFolder()
# else:
#     ImagePath = 'Images1/' + ration_unique_id
name = (input("Enter the name"))
ImagePath = ImagePath+'/'+name

isImg = os.path.isdir(ImagePath)
if not isImg:
    os.mkdir(ImagePath)

else:
    print('The data is already present')
capture = c.VideoCapture(0)
capture.set(c.CAP_PROP_FRAME_WIDTH, 1240)
capture.set(c.CAP_PROP_FRAME_HEIGHT, 980)
def createDataset():
    global sampleNum, image
    while True:
        if(sampleNum==20):
            break
        success, image = capture.read()
        image = c.flip(image, 1)

        imgSmall = c.resize(image, (0, 0), None, 0.25, 0.25)
        imgSmall = c.cvtColor(imgSmall, c.COLOR_BGR2RGB)

        facesCurrentImage = f.face_locations(imgSmall)
        encodeCurrentFrame = f.face_encodings(imgSmall, facesCurrentImage)
        if encodeCurrentFrame.__len__()>0 and len(facesCurrentImage)>0:
            c.imwrite(ImagePath + "/" + name + "_"+sampleNum.__str__()+".jpg", image)
            sampleNum = sampleNum + 1
        c.imshow("image", image)
        c.waitKey(1)

    print('Data Created for '+name)
createDataset()


