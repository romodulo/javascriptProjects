import svg

sw = 500
# nc = None
cw = int(500/20)
print(int(cw))



#Circle has a radius of 10



elems = [] #test-list
elements = [] 
for x in range(0,100):
    for y in range(0,100):
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

fileOpen = open("test.svg", "w")
fileOpen.write(str(canvas))
fileOpen.close()