from swampy.TurtleWorld import *
import math

def square(t, length):
  for i in range(4):
    fd(t, length)
    lt(t)

def polyline(t, n, length, angle):
  """Draws n line segments with the given length and
  angle (in degrees) between them. t is a turtle.
  """
  for i in range(n):
    fd(t, length)
    lt(t, angle)

def polygon(t, n, length):
  angle = 360.0 / n
  polyline(t, n, length, angle)

def arc(t, r, angle):
  arc_length = 2. * math.pi * r * angle / 360 
  n = int (arc_length / 3) + 1
  step_length = arc_length / n
  step_angle = float(angle) / n
  polyline(t, n, step_length, step_angle)

def circle(t, r):
  arc(t, r, 360)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

arc(bob, 50, 270)


wait_for_user()

