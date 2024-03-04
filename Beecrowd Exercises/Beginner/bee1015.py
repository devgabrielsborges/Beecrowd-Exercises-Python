from math import sqrt

xy1 = input().split()
xy2 = input().split()

x1 = float(xy1[0])
y1 = float(xy1[1])
x2 = float(xy2[0])
y2 = float(xy2[1])

d = f'{sqrt((x2 - x1)**2 + (y2 - y1)**2):.4f}'
print(d)
