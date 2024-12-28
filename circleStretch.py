from PIL import Image
import math

im = Image.open("circle-limit-iii.jpg")
im2 = Image.open("circle-limit-iii.jpg")
px = im.load()
px2 = im2.load()

length,height = im.size
#assume perfect circle
r = length

for i in range(length): 
    for j in range(height):  
        xDist = i - r
        yDist = j - r
        d = math.hypot(xDist, yDist)  
        angle = math.atan2(yDist, xDist)

        #depending on if we hit the top/bottom or sides first, scale accordingly
        scale = max(abs(math.cos(angle)), abs(math.sin(angle)))
        d_in = d * scale

        # Coordinates in the input image
        x_in = math.floor(r + math.cos(angle) * d_in)
        y_in = math.floor(r + math.sin(angle) * d_in)

        px[i, j] = px2[x_in,y_in]

# Save result
im.save("out.jpg", "JPEG")