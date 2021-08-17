import pygame
import pygame.display
import pygame.event
from pygame.time import Clock
import pygame.transform
import pygame.key
import pygame.font
import pygame.mouse
import sys
import os
import random

from pygame.locals import *

pygame.init()
pygame.font.init()






title = "Space Dodge"
width, height = 1700, 900


display = pygame.display.set_mode((width, height), RESIZABLE)
pygame.display.set_caption(title)

clock = Clock()









# Surfaces
blackhole_img = pygame.image.load(
    os.path.join("assets" ,"blackhole.png"))
blackhole = pygame.Rect(width/2 - blackhole_img.get_width()/2, -1000, blackhole_img.get_width(),blackhole_img.get_height())



# Planets
planets = []

# Earth
earth_img = pygame.image.load(
    os.path.join("assets", "planets","earth.png")).convert_alpha()
earth = pygame.Rect(
    width - earth_img.get_height() - 100, 100,
    earth_img.get_width(), earth_img.get_height())
planets.append([earth_img, earth])

# Mars
mars_img = pygame.image.load(
    os.path.join("assets", "planets","mars.png")).convert_alpha()
mars = pygame.Rect(
    100, 450,
    mars_img.get_width(), mars_img.get_height())
planets.append([mars_img, mars])

# Venus
venus_img = pygame.image.load(
    os.path.join("assets", "planets","venus.png")).convert_alpha()
venus = pygame.Rect(
    width/2 - venus_img.get_width(), 40,
    venus_img.get_width(), venus_img.get_height())
planets.append([venus_img, venus])

# jupiter
jupiter_img = pygame.image.load(
    os.path.join("assets", "planets","jupiter.png")).convert_alpha()
jupiter = pygame.Rect(
    width - jupiter_img.get_width() - 200, height - jupiter_img.get_height() - 100,
    jupiter_img.get_width(), jupiter_img.get_height())
planets.append([jupiter_img, jupiter])








# Player
player_img = pygame.image.load(
    os.path.join("assets","player.png")).convert_alpha()
player = pygame.Rect(width/2, height/2, player_img.get_width(), player_img.get_height())
# PlayerBullet
bullet_img = pygame.image.load(
    os.path.join("assets", "bullet.png"))

# Enemy
enemy_img = pygame.image.load(os.path.join("assets", "enemy.png")).convert_alpha()
enemies = []
enemy_speed = 3
wavelength = 6


pause = False





# Fonts
font = pygame.font.SysFont("ComicSans", 80)








# Pause
pause_render = font.render("Pause", True, (255,255,255))
pause_rect = pygame.Rect(
    0 + 10,
    0 + 10,
    pause_render.get_width(),
    pause_render.get_height()
)








while 1:

    

    clock.tick(60)

    # Draw
    display.fill((50,50,50))
    
    display.blit(pause_render, (pause_rect.x, pause_rect.y))

    for planet in planets:
        display.blit(planet[0], (planet[1].x, planet[1].y))

        if planet[1].colliderect(blackhole):
            planets.remove([planet[0], planet[1]])
        

    for enemy in enemies:
        display.blit(enemy_img, (enemy.x, enemy.y))
        enemy.y += enemy_speed

        if enemy.y > height + enemy_img.get_height():
            enemies.remove(enemy)

        if enemy.colliderect(player):
            enemies.remove(enemy)

        if enemy.y > 0:
            if enemy.colliderect(blackhole):
                enemies.remove(enemy)


    display.blit(player_img, (player.x, player.y))
    
    display.blit(blackhole_img, (blackhole.x, blackhole.y))
    # blackhole.y += 10




    # Events
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pause = True
            
            if event.key == K_SPACE:
                pygame.quit()
                exit()

        if event.type == VIDEORESIZE:
            width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

    # If enemies == 0
    if len(enemies) == 0:
        for i in range(wavelength):
            enemy = pygame.Rect(
                random.randrange(0, width - enemy_img.get_width()),
                random.randrange(-1000, 0-enemy_img.get_height()),
                enemy_img.get_width(),
                enemy_img.get_height()
            )
            enemies.append(enemy)






    # Buttons Clicks
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = list(pygame.mouse.get_pressed())
        
    if pause_rect.collidepoint(mouse_pos):
        if mouse_pressed[0] == True:
            pause = True 





    # Movement
    keys_pressed = pygame.key.get_pressed()
    
    if keys_pressed[K_a] and player.x > 0:
        player.x -= 10
    if keys_pressed[K_d] and player.x < width - player_img.get_height() - 10:
        player.x += 10

    if keys_pressed[K_w] and player.y > 0:
        player.y -= 10
    
    if keys_pressed[K_s] and player.y < height - player_img.get_height() - 10:
        player.y += 10

    # Change POS
    if blackhole.y > height + blackhole_img.get_height():
        blackhole.y = -1000

    pygame.display.update()






    # Pause
    while pause:
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

            # if event.type == KEYDOWN:
            #     if event.key == K_SPACE:
            #         pause = False

        # Draw
        pause_display.blit(resume_render, (resume.x, resume.y))
        pause_display.blit(menu_render, (menu_rect.x, menu_rect.y))

        
        # mouse pos
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = list(pygame.mouse.get_pressed())
            

        if resume.collidepoint(mouse_pos):

            if mouse_pressed[0] == True:
                pause = False
        

        if menu_rect.collidepoint(mouse_pos):

            if mouse_pressed[0] == True:
                print("Menu")

        pygame.display.update()



pygame.quit()