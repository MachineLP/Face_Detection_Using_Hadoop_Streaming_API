import cv2
import ImageSerialization as IS
import sys
import os
import uuid


def main():

    argv = sys.argv

    if(len(argv)<3):
        print('parameter missing.......')
        print('please use the following format to run the program')
        print('python DataPreProcessing.py <Input Images Directory> <Outputfile name>')
        sys.exit(0)
    else:
        input_dir = argv[1]
        output_file = argv[2]

    paths=getPath(input_dir)

    print(paths)
    ImageEncoding(paths,output_file)

    # target = open('SerializedImages.txt','r')
    #
    # for line in target:
    #     print(line.split('\t')[2])
    #     encoded = line.split('\t')[2]
    # #print(encoded)
    # ImageDecode(encoded)


def getPath(input_dir):
    paths=[]
    validExtension=['.jpg','.jpeg','.png','.bmp']
    for (curr_dir, dir_name, filename) in os.walk(input_dir):
        for files in filename:
            ext =files[files.rfind('.'):].lower()
            if ext in validExtension:
                paths.append(os.path.join(curr_dir,files))

    return paths




def ImageEncoding(paths,output_file):
    target = open(output_file, "w")

    for (i,path) in enumerate(paths):
        img_id = str(uuid.uuid4())
        img = cv2.imread(path,1)
        encoded = IS.b64ImgEncode(img)
        target.write('{}\t{}\t{}\n'.format(img_id,path,encoded))

    target.close()


def ImageDecode(encoded):

    decoded = IS.b64ImgDecode(encoded)
    print(decoded)

    cv2.imshow('decoded',decoded)
    cv2.waitKey(0)


main()


