#!/usr/bin/env python3

import svg
from perlin_noise import PerlinNoise
import math

def dist(a1,b1,a2,b2):
    da = a2-a1
    db = b2-b1
    return math.sqrt(da*da + db*db)

elems = []
cells = 100
noise = PerlinNoise(octaves=10)
sw=500
cw=sw/cells
for x in range(0,cells):
    for y in range(0,cells):
        # radius is cell width / 2
        cx = cw*x + cw/2
        cy = cw*y + cw/2
        dm = dist(cx,cy,sw/2,sw/2)
        if dm > sw/2:
            continue
        dtm = ((sw/2-dm)/(sw/2)) 
        r = (cw/2) * noise([x/cells*2,y/cells/10*2]) * 1.75 * dtm * 8
        # print((dm-sw/2)/(sw/2))
        # r = (cw/2) * ((sw/2-dm)/(sw/2)) * 4
        elems.append(svg.Circle(
            cx=cx,cy=cy,r=r,
            stroke="white",fill="none",stroke_width=1)
        )
    
with open('grid.svg', 'w') as f:
    f.write(str(svg.SVG(width=sw,height=sw,elements=elems)))
```