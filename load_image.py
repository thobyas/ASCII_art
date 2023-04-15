import cv2
import numpy

def img_shape(pc_path):
#LOAD AN IMAGE USING 'IMREAD'
    img = cv2.imread(pc_path,0) #Leo la imagen en escala de grises con el paremetro en "0"
#DISPLAY
    resolution = img.shape
    #cv2.imshow('image',img)
    #cv2.waitKey(0)
    return resolution

def img_pixel(pc_path):
    img = cv2.imread(pc_path) #Leo la imagen
    #print(img)
    return img

def filter(type, pixel,size):  
    filter_img = []
    img_out = []
    if type == "average":
        for i in range(2):
            for j in range(1):
                #aver_value = (int(pixel[i,j][0]) + int(pixel[i,j][1]) + int(pixel[i,j][2]))/3
                aver_value = 3
                filter_img.append([aver_value, aver_value, aver_value])
            img_out.append(filter_img)
        else:
            pass
            #cv2.imshow('image',pixel)
            #cv2.waitKey(0)
    # cv2.imshow('hola',img_out)
    # cv2.waitKey(0)
    print(img_out)


