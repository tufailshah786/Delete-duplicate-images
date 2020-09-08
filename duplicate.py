import numpy as np
import cv2 as cv
import os
import shutil
import json

all_images = os.listdir('C:/python/duplicate/')
print (all_images)
to_remove = []
dict_dupes = {}
for i in range(len(all_images)):
    print(len(all_images)," i = ",i)
    all_images = os.listdir('C:/python/duplicate/')
    image = cv.imread('C:/python/duplicate/'+all_images[i],cv.COLOR_BGR2GRAY)
    for j in range(i, len(all_images), 1):
        print(len(all_images)," i  j = ",i, j)
        indexes = np.sort([i,j])
        image2 = cv.imread('C:/python/duplicate/'+all_images[j])
        if i!=j:
            if np.array_equal(image, image2):
                print (all_images[i],all_images[j]," are equal.",all_images[j],"  removed")
                image3=('C:/python/duplicate/'+all_images[j])
                #print(image3)
                #print(all_images[i])
                #print(all_images[j])
                #print(all_images)
                print(len(all_images))
                to_remove.append(all_images[j])
                os.remove(image3)
    #x=len(os.listdir('C:/python/duplicate/'))
        #y=(len(all_images))
        #if i==y :
        #  break  
    all_images = os.listdir('C:/python/duplicate/') 
    y=(len(all_images))
    print("i = ",i,"y = ",y)
    if i==y-1 :
     break  
print(to_remove) 
print("done")   
with open('C:/python/duplicate/deleted_images.txt', 'w') as f:
    f.write(json.dumps(to_remove))



              
