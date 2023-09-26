import pygame
from game import Game


# def main():
#     width = 800
#     height = 600
#     pygame.init()
#     screen = pygame.display.set_mode((width, height))
#     pygame.display.set_caption("Pong")
#     game = Game(width, height)
#
#     running = True
#     paused = False
#
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         keys = pygame.key.get_pressed()
#         game.update(keys)
#
#         if keys[pygame.K_r]:
#             game.reset()
#
#         if keys[pygame.K_ESCAPE]:
#             running = False
#
#         screen.fill((0, 0, 0))
#         game.draw(screen)
#         pygame.display.update()
#     pygame.quit()
#

def main():
    width = 800
    height = 600
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pong")
    game = Game(width, height)
    running = True
    paused = False
    font = pygame.font.Font(None, 36)
    pause_text = font.render("Juego en Pausa", True, (255, 255, 255))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game.reset()
        if keys[pygame.K_ESCAPE]:
            running = False
        if keys[pygame.K_p]:
            paused = not paused
        if not paused:
            game.update(keys)
        screen.fill((0, 0, 0))
        game.draw(screen)
        if paused:
            screen.blit(pause_text, (width // 2 - pause_text.get_width() // 2, height // 2 - pause_text.get_height() // 2))
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()




