import svg
from perlin_noise import PerlinNoise

sw = 500
# nc = None
cw = int(500/20)
# print(int(cw))



#Circle has a radius of 10



elems = [] #test-list
elements = [] 
def createBackground():
    for x in range(0,21):
        for y in range(0,21):
            elems.append((x,y)) 
            circlePX=x*cw
            circlePY=y*cw
            elements.append(svg.Circle(
                cx=circlePX, cy=circlePY, r=cw,
                # stroke="white", # creates a stroke (a.k.a a border)
                fill="black"
                # stroke_width=5 # stroke-width: self-explanatory
                ))
            # print(x,y)


noise = PerlinNoise()
nc=100
cw = sw/nc
multiplier = 10 # 2 works. 1.5 doesn'ts.
def run1stLoop():
    for x in range(0,nc):
        for y in range(0,nc):
            # elements.append(svg.Circle(
            #     cx=cw*x, cy=cw*y, r=cw,
            #     stroke="red",
            #     stroke_width=1
            # ))
            noiseValue = noise([1, y])
            elements.append(svg.Circle(
                cx=cw*x+cw/2, cy=cw*y+cw/2, r=cw/2*noiseValue*2,
                stroke="white",
                fill="none",
                stroke_width=1
            ))
            # print(str(cw*x+cw/2) + ", " + str(cw*y+cw/2) + ", " + str(noiseValue))
            continue
# test loop
# for i in elems:
#     print(i)
# test loop
# for i in elements:
#     print(i)


#create another set of circles:
def run2ndLoop():
    for x in range(0,nc):
        for y in range(0,nc):
            # elements.append(svg.Circle(
            #     cx=cw*x, cy=cw*y, r=cw,
            #     stroke="red",
            #     stroke_width=1
            # ))
            noiseValue = noise([(cw*x+cw/2)/100, (cw*y+cw/2)/100])
            elements.append(svg.Circle( # you are working on the 2nd loop layer
                cx=cw*x+cw/(2), cy=cw*y+cw/(2**10), r=cw/2*noiseValue*(2),
                stroke="skyblue",
                fill="none",
                stroke_width=1
            ))
            # print(str(cw*x+cw/2) + ", " + str(cw*y+cw/2) + ", " + str(noiseValue))
            continue
            #end of both for loops
run1stLoop()
# run2ndLoop()

canvas = svg.SVG(
    width = sw,
    height = sw,
    elements= elements
)

# initiate initial values
rotateValues = [it for it in range(1,11)]
# print(rotateValues)
# open a counter file
openCounterFile = "open(null)"

filename = "6th-modified-1_x-y-reversed-2"

fileOpen = open(f"./svgsFolder/{filename}.svg", "w")
fileOpen.write(str(canvas))
fileOpen.close()

# print(noise([41.66, 41.66]))