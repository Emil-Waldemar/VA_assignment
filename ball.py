
import random
import math
from tkinter import *

class Ball:

    def __init__(self,x,y,speed_x,speed_y, radius, color) -> None:
        self.x = x
        self.y = y
        self.x_speed = speed_x
        self.y_speed = speed_y
        self.radius = radius
        self.color = color
        self.area = math.pi * math.pow(self.radius,2)

    def move(self):

        # moving the ball
        self.x += self.x_speed
        self.y += self.y_speed
    

        # checking for collisions against the boarders
        if self.x + self.radius >= 600 or self.x - self.radius <= 0:
            self.x_speed = - self.x_speed
        
        if self.y + self.radius >= 900 or self.y - self.radius <= 0:
            self.y_speed = - self.y_speed
        
    def draw(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius,
                          self.x + self.radius, self.y + self.radius, 
                          fill=self.color, outline='black')

    