from ColabTurtle.Turtle import *

class shapes(object):
  vertices=0;
  sides=0;
  def __init__(self,v,s):
    self.vertices=v;
  
  
class polygons(shapes):
  def __init__(self,v,s):
    self.sides=s
    super().__init__(self,v)
  def display(self):
    print("The number of vertices in a rectangle is");
    print(self.vertices);
    print("The number of sides in a rectangle is");
    print(self.sides);
    print("Area= ",);
    print(self.area);
    print("Perimeter=");
    print(self.perimeter);


class rectangles(polygons): 
  
  def __init__(self,v,s, length,breadth):
    self.length=length;
    self.breadth=breadth;
    self.area=0;
    self.perimeter=0;
    polygons.__init__(self,v,s)
    rectangles.area(self);
    rectangles.perimeter(self);
  def get_length(self):
      return self.length;
  def get_breadth(self):
      return self.breadth;
  def area (self):
    self.area=self.length*self.breadth;
    return self.area;
  def perimeter(self):
    self.perimeter=2*(self.length+self.breadth);
    return self.perimeter;
  def draw(self):
  
    initializeTurtle()
    forward(self.breadth)
    right(90)
    forward(self.length)
    right(90)
    forward(self.breadth)
    right(90)
    forward(self.length)
  def display(self):
    super().display();
   
    
class circle(shapes):
  def __init__(self,v,s,r):
    self.radius=r;
    self.vertices=v;
    self.sides=s;
    circle.area(self);
    circle.perimeter(self);
  def area(self):
    self.area=3.14*self.radius*self.radius;
  def perimeter(self):
    self.perimeter=2*3.14*self.radius;
  def display(self):
    print("Radius-")
    print(self.radius)
    print("Area-")
    print(self.area)
    print("Perimeter-")
    print(self.perimeter)
    
class square (polygons): 
  def __init__(self,v,s,length):
    self.length=length;
    self.area=0;
    self.perimeter=0;
    polygons.__init__(self,v,s)
    square.area(self);
    square.perimeter(self);
  def get_length(self):
      return self.length;
  def area (self):
    self.area=self.length*self.length;
    return self.area;
  def perimeter(self):
    self.perimeter=4*(self.length);
    return self.perimeter;
  def draw(self):
    initializeTurtle()
    forward(self.length)
    right(90)
    forward(self.length)
    right(90)
    forward(self.length)
    right(90)
    forward(self.length)
  def display(self):
    super().display();

class triangle(polygons):
  def __init__(self,v,s,side):
    self.side=side;
    self.perimeter=0;
    polygons.__init__(self,v,s);
    triangle.perimeter(self);
  def perimeter(self):
    self.perimeter=3*self.side;
    return self.perimeter;
  def display(self):
    super().display()
  def draw(self):
    initializeTurtle()

    forward(self.side);
    left(120)
    forward(self.side);
    left(120)
    forward(self.side);

class hexagon(polygons):
   def __init__(self,v,s,side):
    self.side=side;
    self.perimeter=0;
    polygons.__init__(self,v,s);
    hexagon.perimeter(self);
   def perimeter(self):
    self.perimeter=6*self.side;
    return self.perimeter;
   def draw(self):
    initializeTurtle()
    left(60)
    forward(self.side);
    left(60)
    forward(self.side);
    left(60)
    forward(self.side);
    left(60)
    forward(self.side);
    left(60)
    forward(self.side);
    left(60)
    forward(self.side);
class star(polygons):
   def __init__(self,v,s,side):
    self.side=side;
    self.perimeter=0;
    polygons.__init__(self,v,s);
    star.perimeter(self);
   def perimeter(self):
    self.perimeter=5*self.side;
    return self.perimeter;
   def draw(self):
    initializeTurtle()
    left(144)
    forward(self.side);
    left(144)
    forward(self.side);
    left(144)
    forward(self.side);
    left(144)
    forward(self.side);
    left(144)
    forward(self.side);
class nonagons(polygons):
   def __init__(self,v,s,side):
    self.side=side;
    self.perimeter=0;
    polygons.__init__(self,v,s);
    nonagons.perimeter(self);
   def perimeter(self):
    self.perimeter=9*self.side;
    return self.perimeter;
   def draw(self):
    initializeTurtle()
    left(40)
    forward(self.side);
    left(40)
    forward(self.side);
    left(40)
    forward(self.side);
    left(40)
    forward(self.side);
    left(40)
    forward(self.side);
    left(40)
    forward(self.side);
    left(40)
    forward(self.side);
    left(40)
    forward(self.side);
    left(40)
    forward(self.side);
class decagons(polygons):
   def __init__(self,v,s,side):
    self.side=side;
    self.perimeter=0;
    polygons.__init__(self,v,s);
    decagons.perimeter(self);
   def perimeter(self):
    self.perimeter=10*self.side;
    return self.perimeter;
   def draw(self):
    initializeTurtle()
    left(36)
    forward(self.side);
    left(36)
    forward(self.side);
    left(36)
    forward(self.side);
    left(36)
    forward(self.side);
    left(36)
    forward(self.side);
    left(36)
    forward(self.side);
    left(36)
    forward(self.side);
    left(36)
    forward(self.side);
    left(36)
    forward(self.side);  
    left(36)
    forward(self.side); 

print("RECTANGLE");
rect=rectangles(4,4,40,50);
print("Lenght=");
print(rect.get_length());
print("Breadth=");
print(rect.get_breadth());
rect.draw();
rect.display();

print("Circle");
cir=circle(0,0,10);
cir.display();

print("Square");
sq=square(4,4,40);
print("Side=");
print(rect.get_length());
sq.draw();
sq.display();

print("Triangle");
tri=triangle(3,3,40);
tri.draw();
print("Perimeter=")
print(tri.perimeter);



print("Hexagon");
hex=hexagon(6,6,40);
hex.draw();
print("Perimeter=")
print(hex.perimeter);

print("Nonagons");
nona=nonagons(9,9,40);
nona.draw();
print("Perimeter=")
print(nona.perimeter);


print("Decagons");
dec=decagons(9,9,40);
dec.draw();
print("Perimeter=")
print(dec.perimeter);

print("STAR");
dex=star(10,10,60);
dex.draw();
print("Perimeter=")
print(dex.perimeter);




