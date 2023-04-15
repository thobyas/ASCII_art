import cv2
import numpy

def img_shape(pc_path):
#LOAD AN IMAGE USING 'IMREAD'
    img = cv2.imread(pc_path,0) #Leo la imagen en escala de grises con el paremetro en "0"
#DISPLAY
    resolution = img.shape
    return resolution

def img_pixel(pc_path):
    img = cv2.imread(pc_path) #Leo la imagen
    print(img)
