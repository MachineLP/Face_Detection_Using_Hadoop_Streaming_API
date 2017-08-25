import json

import ImageSerialization as IS
import os
import sys
import cv2

def getPath():
    dir_path =sys.argv[1]
    paths=[]
    for (curr_dir, dir_name, filename) in os.walk(dir_path):
        for files in filename:
            file_name = files[:files.rfind('.')].lower()
            if "part" in file_name:
                paths.append(os.path.join(curr_dir, files))

    return paths


def fileread(paths):

    for path in paths:
        target = open(path,'r')

        for line in target:
            Orig_img_path = line.split('\t')[1]
            rect = line.split('\t')[2]
            decoded =json.loads(rect)
            if(len(decoded)>0):
                img = cv2.imread(Orig_img_path)
                for i in range(len(decoded)):
                    cv2.rectangle(img,(decoded[i][0],decoded[i][1]),(decoded[i][0]+decoded[i][2],decoded[i][1]+decoded[i][3]),(0,255,0))
            cv2.imshow('faces',img)
            cv2.waitKey(0)





def main():
    paths=getPath()
    fileread(paths)




main()