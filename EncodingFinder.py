import face_recognition as f
import numpy as np
import cv2 as c
import os
import pickle as p

path = 'Images1'
image_dir = 'Images1'
ImageList = os.listdir(path)
Images = []
ImageName=[]
FullImageName = []
print('Getting Images')
print('Getting All the Encodes....')
print('Please Wait...')

encodeList = []

for root, dirs, files in os.walk(image_dir):

    for dir in dirs:
        a = os.listdir(image_dir+'/'+dir)
        for folder_name in a:
            b = os.listdir(image_dir + '/' + dir+'/'+folder_name)
            for image in b:
                FullImageName.append(image)
                path = image_dir + '/' + dir+'/'+folder_name

                currentImg = c.imread(f'{path}/{image}')
                currentImg = c.resize(currentImg, (0, 0), None, 0.25, 0.25)
                currentImg = c.cvtColor(currentImg, c.COLOR_BGR2RGB)

                encode = f.face_encodings(currentImg, model='large')[0]
                if len(encode)>0:
                    encodeList.append(encode)
                    Images.append(currentImg)
                    NameOfImg = os.path.splitext(image)[0]
                    if (NameOfImg.__contains__('_')):
                        NameOfImg = NameOfImg.split('_')[0]
                        ImageName.append(NameOfImg)

                    else:
                        ad = os.path.splitext(image)[0]
                        ImageName.append(NameOfImg)
                else:
                    print('removing...', image)
                    os.remove(path + '/' + image)
                    print('Removed', image)
                encode = []




    break

# print("All Images are imported")
# s= []
# print(ImageName)

# def findEncoding(Images):
#     print(ImageName)
#     # remove = []
#     i = 0
#     for img in Images:
#         try:
#
#             encode = f.face_encodings(img,model='large')[0]
#             encodeList.append(encode)
#         except:
#             # remove.append(i)
#             print('removing...',image)
#             os.remove(path + '/' + image)
#             print('Removed',image)
#
#             #
#             # print("There is an error in a file at index->" + i.__str__())
#             # print(ImageName[i])
#
#         # i = i+1
#     # remove.reverse()
#     # for i in remove:
#     #         print(i)
#     #         ImageName.pop(i)
#     return encodeList


encodeListForKnownFaces = encodeList
# print(ImageName)
# print('All Encodes are obtained')

with open('dataset_faces.dat', 'wb') as filedata:
    p.dump(encodeListForKnownFaces, filedata)

with open('imageName.dat', 'wb') as filedata:
    p.dump(ImageName, filedata)

# dataFrame = pa.DataFrame(encodeListForKnownFaces)
# # print(dataFrame[0][0])
# dataFrame.stack().reset_index()
# ad = dataFrame.to_csv('dataset_faces.csv')
# df = np.array(encodeListForKnownFaces)
#
# dataFrame = pa.DataFrame(ImageName)
# dataFrame.to_csv('imageName.csv')
# print(len(encodeListForKnownFaces))

#
# print(encodeListForKnownFaces.__len__())
# print(ImageName.__len__())
# print(ImageName)
# print(FullImageName)