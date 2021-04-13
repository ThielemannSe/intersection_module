from geoms import Point2D

start = Point2D(2, 1)
end = Point2D(1, 2)
center = Point2D(1, 1)

u = start.substraction(center)
v = end.substraction(center)

k = u.x * v.y - u.y * v.x

print(k)