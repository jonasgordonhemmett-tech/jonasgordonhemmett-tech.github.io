from PIL import Image

folderLocation = input("Folder: ")

sizes = (1600, 800, 400)
while True:
    imageLocation = input("Image Name (enter to exit): ")
    if not imageLocation:
        break

    img = Image.open("resources/" + folderLocation + "/" + imageLocation)


    for size in sizes:
        resized_img = img.resize((size, size), Image.Resampling.LANCZOS)

        resized_img.save("resources/" + folderLocation + "/" + imageLocation.replace("full","").split(".")[0] + str(size) + "." + imageLocation.split(".")[1])