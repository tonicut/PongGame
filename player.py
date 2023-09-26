import pygame

class Player:
    def __init__(self, x, y, width, height, color, up_key, down_key):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.up_key = up_key
        self.down_key = down_key

    def update(self, keys, height):
        if keys[self.up_key]:
            self.y -= 0.75
        if keys[self.down_key]:
            self.y += 0.75
        if self.y < 0:
            self.y = 0
        if self.y + self.height > height:
            self.y = height - self.height

    def check_collision(self, ball):
        if (ball.x - ball.radius <= self.x + self.width) and (ball.x + ball.radius >= self.x) and (ball.y - ball.radius <= self.y + self.height) and (ball.y + ball.radius >= self.y):
            return True
        else:
            return False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))