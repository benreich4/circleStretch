from PIL import Image
import math

im = Image.open("circle-limit-iii.jpg")
im2 = Image.open("circle-limit-iii.jpg")
px = im.load()
px2 = im2.load()

length,height = im.size
#assume perfect circle
r = length / 2.0

#scaling power. Lower is compressing center and higher expands center.
p = 1.25

def scale_factor(angle, d):
    #max distance at this angle
    md = r/max(abs(math.cos(angle)), abs(math.sin(angle)))
    #percentage of distance to edge along this angle
    perc = (d/md)
    #scale factor raised to the stretching power
    return perc**p

for i in range(length): 
    for j in range(height):  
        xDist = i - r
        yDist = j - r
        d = math.hypot(xDist, yDist)  
        angle = math.atan2(yDist, xDist)

        #depending on if we hit the top/bottom or sides first, scale accordingly
        scale = scale_factor(angle,d)
        d_in = r * scale

        # Coordinates in the input image
        x_in = math.floor(r + math.cos(angle) * d_in)
        y_in = math.floor(r + math.sin(angle) * d_in)
        if(x_in >= 0 and y_in >= 0 and x_in < length and y_in < height):
            px[i, j] = px2[x_in,y_in]

# Save result
im.save("out.jpg", "JPEG")