sw = 500
cw = 500/20

def Circle(*opt_arguments):
    pass
    #Circle has a radius of 10




elems = []
circles = [] #for test purposes
for x in range(0,20):
    for y in range(0,20):
        elems.append((x,y))
        ciX=x*cw
        ciY=y*cw
        circles.append(Circle(ciX,ciY))
        print(x,y)
# for i in elems:
#     print(i)