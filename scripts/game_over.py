from .settings import *
from pygame.locals import *
import pygame
from .menu import menu_screen

highscore = Highscore()

def gameover(score, kills, display):
    while 1:
        over_display = display
        over_display.fill((50,50,50))

        game_over_font = pygame.font.SysFont("ComicSans", 130)
        font = pygame.font.SysFont("ComicSans", 100)

        game_over_render = game_over_font.render("Game Over", True, (255,255,255))
        

        menu_render = font.render("Space To Menu", True, (255,255,255))
        menu_rect = pygame.Rect(
            width/2 - menu_render.get_width()/2,
            height/2 - menu_render.get_height()/2 - 80 ,
            menu_render.get_width(),
            menu_render.get_height()
        )
        score_render = font.render(f"Score : {int(score)}", True, (255,255,255))
        kills_render = font.render(f"Kills : {kills}", True, (255,255,255))
        highscore_render = font.render(f"{highscore_text} : {highscore.get_highscore()}", True, (255,255,255))




        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return "menu"


        # Draw
        over_display.blit(game_over_render, (width/2 - game_over_render.get_width()/2, 50))
        over_display.blit(menu_render, (menu_rect.x, menu_rect.y))
        
        over_display.blit(
            score_render,
            (
                width/2 - score_render.get_width()/2,
                height/2 - score_render.get_height()/2 + 40
            )
        )
        
        over_display.blit(
            kills_render,
            (
                width/2 - kills_render.get_width()/2,
                height/2 - kills_render.get_height()/2 + 60 + score_render.get_height()
            )
        )

        over_display.blit(
            highscore_render,
            (
                width/2 - highscore_render.get_width()/2,
                height/2 - highscore_render.get_height()/2 + 140 + kills_render.get_height()
            )
        )

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if menu_rect.collidepoint(mouse_pos):
            if mouse_pressed[0] == True:
                return "menu"

        pygame.display.update()


def gameover_screen(score, kills, display):
    gameover_result = gameover(score, kills, display)
    if gameover_result == "menu":
        menu_result = menu_screen(display)
        return menu_result

