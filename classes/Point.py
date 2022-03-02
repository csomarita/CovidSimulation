import math
import random

class Point(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  @staticmethod
  def distance(p1, p2):
    return math.sqrt(
        pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2)
    )

  @staticmethod
  def randomPoint(radius, center):
    random_angle = 2 * math.pi * random.random()
    random_radius = radius * math.sqrt(random.random())
    return Point(
      random_radius * math.cos(random_angle) + center.x,
      random_radius * math.sin(random_angle) + center.y
    )