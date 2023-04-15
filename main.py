import load_image

def main():
    resolution = load_image.img_shape("resources/Blacksun.jpg")
    print("Image size: ",resolution[0],"x",resolution[1]) #Verifico el tamaño de mi imagen
    pixel = load_image.img_pixel("resources/Blacksun.jpg") #Cargo los pixeles punto por punto
    load_image.filter("average", pixel, resolution)
    aver_value = int(pixel[0,0][1])+ int(pixel[0,0][1])
    a = pixel[0,0][0]
    print(aver_value)

if __name__ == "__main__":
    main()
