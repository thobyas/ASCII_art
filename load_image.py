import cv2
import numpy as np

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
    matrix = np.zeros((3, 3))
    img_out = [[0 for j in range(3)] for i in range(3)]
    if type == "average":
        for i in range(3):
            for j in range(3):
                aver_value = (int(pixel[i,j][0]) + int(pixel[i,j][1]) + int(pixel[i,j][2]))/3
                aver_value = 3
                img_out[i][j] = [aver_value, aver_value, aver_value]
                datos = [[[1, 2, 3], [1, 2, 3]],[[4, 5, 6], [7, 8, 9]]]
                matrix = np.array(datos)
            #img_out.append(filter_img,0)
        else:
            pass
            #cv2.imshow('image',pixel)
            #cv2.waitKey(0)
    #cv2.imshow('hola',img_out)
    #cv2.waitKey(0)
    print(matrix)


