from .settings import *
from pygame.locals import *
import pygame
import pygame.display
import sys
from .settings import run

highscore = Highscore()


def menu_screen(display):
    while menu:
        menu_display = display
        menu_display.fill((50, 50, 50))

        title_font = pygame.font.SysFont("ComicSans", 200)
        font = pygame.font.SysFont("ComicSans", 120)

        play_render = font.render("Play", True, (255, 255, 255))
        play_rect = pygame.Rect(
            width/2 - play_render.get_width()/2,
            height/2 - play_render.get_height()/2 - 50,
            play_render.get_width(),
            play_render.get_height()
        )
        title_render = title_font.render(title, True, (255, 255, 255))
        highscore_render = font.render(
            f"Highscore : {highscore.get_highscore()}", True, (255, 255, 255))

        # Draw
        for planet in planets:
            menu_display.blit(planet[0], (planet[1].x, planet[1].y))

        menu_display.blit(play_render, (play_rect.x, play_rect.y))
        menu_display.blit(
            title_render, (width/2 - title_render.get_width()/2, 20))
        menu_display.blit(highscore_render, (width/2 - highscore_render.get_width() /
                            2, height/2-highscore_render.get_height()/2 + 50))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return True

        pygame.display.update()

