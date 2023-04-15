import load_image

def main():
    resolution = load_image.img_shape("resources/Blacksun.jpg")
    print("Image size: ",resolution[0],"x",resolution[1])
    pixel = load_image.img_pixel("resources/Blacksun.jpg")
    

if __name__ == "__main__":
    main()
