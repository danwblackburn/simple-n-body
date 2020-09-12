from graphics import Circle
from graphics import GraphWin
from graphics import Point
from graphics import Text

import time
import math
import numpy as np

G = 10

class Planet(Circle):
    
    def __init__(self, Point, radius, mass, color):
        super().__init__(Point, radius)
        self.mass = mass
        self.velocity = [0.0, 0.0]
        self.color = color
        self.setFill(color)


def main():
    win = GraphWin("Window", 1024, 760)
    win.setBackground("white")
    
    earth = Planet(Point(500,500), 10, 20.0, "blue")
    earth.draw(win)
    earth.velocity = [100, -30]

    mars = Planet(Point(200, 300), 7, 15.0, "red")
    mars.draw(win)
    mars.velocity = [50, 100]

    jupiter = Planet(Point(100,100), 20, 40.0, "green")
    jupiter.draw(win)
    jupiter.velocity = [100, -50]

    sun = Planet(Point(380,380), 40, 1000.0, "yellow")
    sun.draw(win)
    sun.velocity = [-5, 0]

    label = Text(Point(60,10), "Current Veloctiy: Unkown")
    label.draw(win)


    planets = [mars, earth, jupiter, sun]
    count = 0
    while(True):

        dT = .01
        for planet in planets:
            F = getNetForce(planet, planets)
            ax = -F[0] / planet.mass 
            ay = -F[1] / planet.mass 
            planet.velocity[0] += ax * dT
            planet.velocity[1] += ay * dT


        for planet in planets:
            planet.move(planet.velocity[0] * dT , planet.velocity[1]* dT)
            if count == 10:
                win.plot(planet.getCenter().x, planet.getCenter().y, color=planet.color)
        
        if count == 10:
            count = 0
        count += 1

        txt = "vel: {:0.2f}, {:0.2f}".format(planet.velocity[0], planet.velocity[0])
        label.setText(txt)


def getNetForce(planet, planets):
    F = np.array([0.0, 0.0])
    for neighbor in planets:
        if(planet != neighbor):
            F = np.add(F, np.array(getForce(planet, neighbor)))
    return F
    

def getForce(planetA, planetB):
    dist = getDistance(planetA.getCenter(), planetB.getCenter())
    F = G * planetA.mass * planetB.mass / (pyth(dist) ** 2.0)
    return [i * F for i in dist]

def getDirection(dist):
    norm = pyth(dist)
    direction = [dist[0] / norm, dist[1] / norm]
    return direction

def getDistance(a, b):
    return [a.x - b.x, a.y - b.y]

def pyth(dist):
    return math.sqrt(dist[0]**2 + dist[1]**2)

main()