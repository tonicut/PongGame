import pygame
import random

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = random.choice([0.25, -0.25])
        self.speed_y = random.choice([0.25, -0.25])

    def update(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.y + self.radius > height or self.y - self.radius < 0:
            self.speed_y = -self.speed_y
        if self.x + self.radius > width or self.x - self.radius < 0:
            self.speed_x = -self.speed_x

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

