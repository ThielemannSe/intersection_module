from shapely.geometry import LineString, Point
import matplotlib.pyplot as plt
from geoms import Arc2D, Point2D
import geopandas as gpd
import math





p1 = Point2D(2, 0)
p2 = Point2D(2, 2)

p3 = Point2D(-3, 1)
p3.plot()

height = 0.5

arc = Arc2D(p1, p2, p3, height)

line = LineString(arc.sample(2000))
plt.plot(*line.coords.xy)

print(arc.isClockwise())

cp = arc.getCenterpoint()

# Plotting
cp.plot()
p1.plot()
p2.plot()
# circle = plt.Circle((cp.x, cp.y), arc.getRadius(), fill=False)
# plt.gca().add_patch(circle)
plt.show()




