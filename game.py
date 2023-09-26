import random
import pygame
from ball import Ball
from player import Player

class Game:
    def __init__(self, width, height):

        self.font = pygame.font.Font(None, 30)
        self.width = width
        self.height = height
        self.ball = Ball(width // 2, height // 2, 10, (255, 255, 255))
        self.players = [Player(0, height // 2 - 50, 10, 100, (255, 0, 0), pygame.K_w, pygame.K_s),
                        Player(width - 10, height // 2 - 50, 10, 100, (0, 0, 255), pygame.K_UP, pygame.K_DOWN)]
        self.player1_score = 0
        self.player2_score = 0

    def update(self, keys):
        self.ball.update(self.width, self.height)
        for player in self.players:
            player.update(keys, self.height)
        if self.ball.x + self.ball.radius > self.width:
            if not self.players[1].check_collision(self.ball):
                self.player1_score += 1
                self.reset_ball()
        if self.ball.x - self.ball.radius < 0:
            if not self.players[0].check_collision(self.ball):
                self.player2_score += 1
                self.reset_ball()
        if keys[pygame.K_r]:
            self.player1_score = 0
            self.player2_score = 0

    def draw(self, screen):
        self.ball.draw(screen)
        for player in self.players:
            player.draw(screen)
        score1 = self.font.render("Player 1: " + str(self.player1_score), True, (255, 255, 255))
        score2 = self.font.render("Player 2: " + str(self.player2_score), True, (255, 255, 255))
        screen.blit(score1, (10, 10))
        screen.blit(score2, (self.width - 150, 10))


    def reset_ball(self):
        self.ball.x = self.width // 2
        self.ball.y = self.height // 2
        self.ball.velocity_x = random.choice([0.25, -0.25])
        self.ball.velocity_y = random.choice([0.25, -0.25])

    def reset(self):
        self.ball.x = self.width // 2
        self.ball.y = self.height // 2
        self.ball.velocity = [random.choice([0.25, -0.25]), random.choice([0.25, -0.25])]
        self.player1_score = 0
        self.player2_score = 0
