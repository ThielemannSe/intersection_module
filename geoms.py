# Defining Basic Geometry Types

from shapely.geometry import LineString, Point, MultiLineString
import matplotlib.pyplot as plt
import math


class Point2D(Point):
    """ 
    Adding some required funcionality to shapely's point geometry by using
    inheritance. 
    """

    def substraction(self, other):
        return Point2D(self.x - other.x, self.y - other.y)

    def addition(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def scalarMultiplication(self, f):
        return Point2D(self.x * f, self.y * f)

    def plot(self):
        plt.scatter(self.x, self.y)

    def __repr__(self):
        return "Point2D ( {} {} )".format(self.x, self.y)


class Arc2D():

    def __init__(self, startpoint, endpoint, controlpoint, height):
        self.startpoint = startpoint
        self.endpoint = endpoint
        self.controlpoint = controlpoint
        self.height = height

    def distance(self):
        return self.startpoint.distance(self.endpoint)

    def getRadius(self):
        return ( 4 * self.height**2 + self.distance()**2 ) / (8 * self.height) 

    def getCenterpoint(self):
        d = self.distance()
        a = d / 2
        r = self.getRadius()
        h = math.sqrt(r * r - a * a)

        tempP = self.endpoint.substraction(self.startpoint).scalarMultiplication(a/d).addition(self.startpoint)
        c1 = Point2D((tempP.x + h * (self.endpoint.y - self.startpoint.y) /d), (tempP.y - h *(self.endpoint.x - self.startpoint.x)/d))
        c2 = Point2D((tempP.x - h * (self.endpoint.y - self.startpoint.y) /d), (tempP.y + h *(self.endpoint.x - self.startpoint.x)/d))

        if c1.distance(self.controlpoint) > c2.distance(self.controlpoint):
            return c1
        else:
            return c2

    def sample(self, steps=2):
        cp = self.getCenterpoint()
        angle = self.centerAngle()

        dx = self.startpoint.x - cp.x
        dy = self.startpoint.y - cp.y
        
        t = math.atan(dx/dy)

        # Second quadrant
        if dx >= 0 and dy <= 0:
            t += math.pi
        # Third quadrant
        elif dx <= 0 and dy <= 0:
            t += math.pi
        elif dx <= 0 and dy >= 0:
            t += math.pi * 2
        
        sample_points = [(self.startpoint.x, self.startpoint.y)]

        for i in range(1, steps):
            px = cp.x + self.getRadius() * math.sin((t - angle/steps * i))
            py = cp.y + self.getRadius() * math.cos((t - angle/steps * i))
            sample_points.append((px, py))

        sample_points.append((self.endpoint.x, self.endpoint.y))

        return sample_points



    @staticmethod
    def getAngle(p1, p2, unit="rad"):
        """
        Returning the angle between the y=axis and a line represented by two points.
        
        Params
        ------
        p1, p2: Point2D
        unit:   String

        Return
        ------
        angle: Float
        """

        t = math.atan((p2.x - p1.x)/(p2.y - p1.y))
        
        if unit == 'rad':
            return t
        elif unit=='deg':
            return t * 180/math.pi


    def centerAngle(self):
        return 2 * math.asin(self.distance()/(2*self.getRadius()))

    @staticmethod
    def angle(dx, dy):

        t = math.atan(dx/dy)

        # Second quadrant
        if dx >= 0 and dy <= 0:
            t += math.pi
        # Third quadrant
        elif dx <= 0 and dy <= 0:
            t += math.pi
        elif dx <= 0 and dy >= 0:
            t += math.pi * 2
    
        return t


    def sample(self, steps=2):
        cp = self.getCenterpoint()
        angle = self.centerAngle()

        # Start-angle
        dx_s = self.startpoint.x - cp.x
        dy_s = self.startpoint.y - cp.y
        t_start = self.angle(dx_s, dy_s)

        # End-angle
        dx_e = self.endpoint.x - cp.x
        dy_e = self.endpoint.y - cp.y
        t_end = self.angle(dx_e, dy_e)

        sample_points = [(self.startpoint.x, self.startpoint.y)]

        if t_start < t_end:
            for i in range(1, steps):
                
                px = cp.x + self.getRadius() * math.sin((t_start + angle/steps * i))
                py = cp.y + self.getRadius() * math.cos((t_start + angle/steps * i))
                sample_points.append((px, py))
        else:
            for i in range(1, steps):
                
                px = cp.x + self.getRadius() * math.sin((t_start - angle/steps * i))
                py = cp.y + self.getRadius() * math.cos((t_start - angle/steps * i))
                sample_points.append((px, py))

        sample_points.append((self.endpoint.x, self.endpoint.y))

        return sample_points

    def toCircleSegment(self):
        return CircleSegment2D(self.startpoint, self.endpoint, self.getCenterpoint())



class CircleSegment2D():

    def __init__(self, startpoint, endpoint, centerpoint):
        self.startpoint = startpoint
        self.endpoint = endpoint
        self.centerpoint = centerpoint
        self.radius = self.setRadius()
        self.start_anlge = self.setStartAngle()
        self.end_anlge = self.setEndAngle()
        self.orientation = self.setOrientation()

    def setRadius(self):
        self.radius = math.sqrt( (self.startpoint.x - self.endpoint.y)**2 + (self.startpoint.x - self.endpoint.y)**2 )

    def setStartAngle(self):
        return self.getAngle(self.centerpoint, self.startpoint)

    def setEndAngle(self):
        return self.getAngle(self.centerpoint, self.endpoint)

    def setOrientation(self):
        if start_angle < end_angle:
            return 'clockwise'
        else:
            return 'anti-clockwise'

    @staticmethod
    def getAngle(p1, p2):
        dx = p2.x - p1.x
        dy = p2.y - p1.y

        print(dy)
        print(dx)

        t = math.atan(dx/dy)

        # Second quadrant
        if dx >= 0 and dy <= 0:
            t += math.pi
        # Third quadrant
        elif dx <= 0 and dy <= 0:
            t += math.pi
        # Fouth quadrant
        elif dx <= 0 and dy >= 0:
            t += math.pi * 2

        return t


    def sample(self, steps=10):
        cp = self.getCenterpoint()
        angle = self.centerAngle()

        dx = self.startpoint.x - cp.x
        dy = self.startpoint.y - cp.y
        
        t = math.atan(dx/dy)

        # Second quadrant
        if dx >= 0 and dy <= 0:
            t += math.pi
        # Third quadrant
        elif dx <= 0 and dy <= 0:
            t += math.pi
        elif dx <= 0 and dy >= 0:
            t += math.pi * 2
        
        sample_points = [(self.startpoint.x, self.startpoint.y)]

        for i in range(1, steps):
            px = cp.x + self.getRadius() * math.sin((t - angle/steps * i))
            py = cp.y + self.getRadius() * math.cos((t - angle/steps * i))
            sample_points.append((px, py))

        sample_points.append((self.endpoint.x, self.endpoint.y))

        return sample_points