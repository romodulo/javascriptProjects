import svg
from perlin_noise import PerlinNoise

sw = 500
# nc = None
cw = int(500/20)
# print(int(cw))



#Circle has a radius of 10



elems = [] #test-list
elements = [] 
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
cw = sw/20
for y in range(0,22):
    for x in range(0,22):
        # elements.append(svg.Circle(
        #     cx=cw*x, cy=cw*y, r=cw,
        #     stroke="red",
        #     stroke_width=1
        # ))
        print(str(cw*x+cw/2) + ", " + str(cw*y+cw/2))
        elements.append(svg.Circle(
            cx=cw*x+cw/2, cy=cw*y+cw/2, r=cw/2*noise([(cw*x+cw/2)/100, (cw*y+cw/2)/100]),
            stroke="white",
            stroke_width=1
        ))

        continue
# test loop
# for i in elems:
#     print(i)
# test loop
# for i in elements:
#     print(i)

canvas = svg.SVG(
    width = sw,
    height = sw,
    elements= elements
)

filename = "6th"

fileOpen = open(f"./svgsFolder/{filename}.svg", "w")
fileOpen.write(str(canvas))
fileOpen.close()

# print(noise([41.66, 41.66]))