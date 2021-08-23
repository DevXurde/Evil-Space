from .settings import *
from pygame.locals import *
import pygame

def pause_game():

    pause_display = pygame.display.set_mode((width, height))
    pause_display.fill((50,50,50))

    font = pygame.font.SysFont("ComicSans", 100)
    
    resume_render = font.render("Resume", True, (255,255,255))
    resume = pygame.Rect(
        width/2 - resume_render.get_width()/2,
        height/2 - resume_render.get_height()/2 - 75,
        resume_render.get_width(),
        resume_render.get_height()
    )

    menu_render = font.render("Menu", True, (255,255,255))
    menu_rect = pygame.Rect(
        width/2 - menu_render.get_width()/2,
        height/2 - menu_render.get_height()/2 + 75,
        menu_render.get_width(),
        menu_render.get_height()
    )


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == K_ESCAPE:
            if event.key == K_SPACE:
                return "resume"

    # Draw
    pause_display.blit(resume_render, (resume.x, resume.y))
    pause_display.blit(menu_render, (menu_rect.x, menu_rect.y))

    
    # mouse pos
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = list(pygame.mouse.get_pressed())
        

    if resume.collidepoint(mouse_pos):

        if mouse_pressed[0] == True:
            # Ask for resume
            return "resume"
    

    if menu_rect.collidepoint(mouse_pos):

        if mouse_pressed[0] == True:
            return "menu"

    pygame.display.update()