from PIL import Image
import math

image = Image.open("images.jpeg")
data = image.load()
new_image = Image.new("RGB", (image.width, image.height))
new_data = new_image.load()

rotation = .5
center = (image.width/2,image.height/2)

cosine_theta = math.cos(-rotation)
sine_theta = math.sin(-rotation)

for y in range(image.height):
    for x in range(image.width):
        
        new_x = cosine_theta * x - sine_theta * y - cosine_theta * image.width/2 + sine_theta*image.height/2+image.width/2
        new_y = sine_theta * x + cosine_theta * y - sine_theta * image.width/2 - cosine_theta * image.height/2+image.height/2
        
        new_x //= 1
        new_y //= 1
        
        if 0<=new_x<image.width and 0<=new_y<image.height:
            new_data[x,y] = data[new_x,new_y]
            
        else:
            new_data[x,y] = (0,0,0)
        

new_image.save("rotation.png")
