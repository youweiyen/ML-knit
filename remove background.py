from PIL import Image

img = Image.open('pattern_5_7406.png')
image_data = Image.load()

height,width = image_data.size

for loop1 in range(height):
    for loop2 in range(width):
        r,g,b = image_data[loop1,loop2]
        image_data[loop1,loop2] = 0,g,b

img.save('changed.jpeg')
img.close()

#image.show()