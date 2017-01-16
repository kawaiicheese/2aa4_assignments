class CircleT():
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r

    def xcoord(self):
        return self.x
    def ycoord(self):
        return self.y
    def radius(self):
        return self.r

    def area(self):
        return self.r**2*math.pi
    def circumference(self):
        return self.r*2*math.pi
    
    def insideBox(self, x0,y0,w,h):
        inside_H = (x0 < self.x - self.r) and (x0 + w < self.x + self.r)
        inside_V = (y0 < self.y + self.r) and (y0 - h < self.y - self.r)
        return inside_H and inside_V
    def intersect(self, c):
        #intersect includes the two circles touch
        distance = ((self.x-c.xcoord)**2 + (self.y-c.ycoord)**2)**0.5
        return distance <= (self.r + c.radius)
    
    def scale(self, k):
        self.r *= k
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
    
