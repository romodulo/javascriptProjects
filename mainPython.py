import svg

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
# preliminary-data:
cw = sw/5
for y in range(0,5):
    for x in range(0,5):
        # elements.append(svg.Circle(
        #     cx=cw*x, cy=cw*y, r=cw,
        #     stroke="red",
        #     stroke_width=1
        # ))
        elements.append(svg.Circle(
            cx=cw*x+cw/2, cy=cw*y+cw/2, r=cw/2,
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

filename = "5th"

fileOpen = open(f"./svgsFolder/{filename}.svg", "w")
fileOpen.write(str(canvas))
fileOpen.close()