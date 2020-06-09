import pygame
import random


class Snake(object):
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.dir = "right"
        self.hitbox = [self.x, self.y, self.width, self.height]
        self.body = []
        self.body.append(self.hitbox)

    def draw(self, win, color):
        for segment in self.body:
            pygame.draw.rect(win, color, segment)
            pygame.draw.rect(win, (255, 0, 0), segment, 1)


    def shiftDim(self):
        for i in range(len(self.body) - 1):
                curr = len(self.body) - (i + 1)
                prev = len(self.body) - (i + 2)
                self.body[curr][0] = self.body[prev][0]
                self.body[curr][1] = self.body[prev][1]
                self.body[curr].clear()
                for dim in self.body[prev]:
                    self.body[curr].append(dim)


    def move(self):
        if self.dir == "left":
            if len(self.body) > 1:
                self.shiftDim()
            self.x -= self.vel
            self.body[0][0] = self.x
        elif self.dir == "right":
            if len(self.body) > 1:
                self.shiftDim()
            self.x += self.vel
            self.body[0][0] = self.x
        elif self.dir == "up":
            if len(self.body) > 1:
                self.shiftDim()
            self.y -= self.vel
            self.body[0][1] = self.y
        else:
            if len(self.body) > 1:
                self.shiftDim()
            self.y += self.vel
            self.body[0][1] = self.y

    def grow(self):
        index = len(self.body) - 1
        segment = [self.body[index][0], self.body[index][1], self.body[index][2], self.body[index][3]]
        self.body.append(segment)

class Fruit():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dim = [self.x, self.y, self.width, self.height]

    def draw(self, win, color):
        pygame.draw.rect(win, color, self.dim)

    def eat(self, width, height):
        self.x = int(random.randrange(0, width, self.width))
        self.y = int(random.randrange(0, height, self.height))
        self.dim[0] = self.x
        self.dim[1] = self.y