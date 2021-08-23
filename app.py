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




title = "Evil Space"
width, height = 1700, 900

display = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)

clock = Clock()
FPS = 60









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
player_speed = 10
# PlayerBullet
bullet_img = pygame.image.load(
    os.path.join("assets", "bullet.png"))
bullets = []
bullet_ready = False






# Enemy
enemy_img = pygame.image.load(os.path.join("assets", "enemy.png")).convert_alpha()
enemies = []
enemy_speed = 3
wavelength = 6








# Fonts
font = pygame.font.SysFont("ComicSans", 70)








# Pause
pause_render = font.render("Pause", True, (255,255,255))
pause_rect = pygame.Rect(
    0 + 30,
    0 + 10,
    pause_render.get_width(),
    pause_render.get_height()
)
pause = False









# Level, Scores, Lives
score = 0
level = 0
lives = 10

kills = 0










# Game Over
game_over = False







# Read and Write highscore
class Highscore:
    def __init__(self) -> None:
        pass

    def get_highscore(self):
        with open("highscore.txt", "r") as highscore:
            highscore = highscore.read()

        return highscore

    def write_highscore(self, score):
        with open("highscore.txt", "w") as highscore:
            highscore.write(score)

        return True


highscore = Highscore()
highscore_text = "Highscore"







while 1:

    # Some Vars
    lives_render = font.render(f"Lives : {lives}", True, (255,255,255))
    level_render = font.render(f"Level : {level}", True, (255,255,255))
    score_render = font.render(f"Score : {int(score)}", True, (255,255,255))
    kills_render = font.render(f"Kills : {kills}", True, (255,255,255))


    clock.tick(FPS)




    # Draw
    display.fill((50,50,50))


    for planet in planets:
        display.blit(planet[0], (planet[1].x, planet[1].y))

        if planet[1].colliderect(blackhole):
            planets.remove([planet[0], planet[1]])
        



    for enemy in enemies:
        display.blit(enemy_img, (enemy.x, enemy.y))
        enemy.y += enemy_speed

        if enemy.y > height + enemy_img.get_height():
            remove_enemy = enemies.remove(enemy)
            if remove_enemy == None:
                lives -= 1

        if enemy.colliderect(player):
            remove_enemy = enemies.remove(enemy)
            if remove_enemy == None:
                lives -= 1
                kills += 1

        if enemy.y > 0:
            if enemy.colliderect(blackhole):
                enemies.remove(enemy)

    display.blit(player_img, (player.x, player.y))

    for bullet in bullets:
        display.blit(bullet_img, (bullet.x, bullet.y))
        bullet.y -= 10

        if bullet.y < 0:
            if bullet in bullets:
                bullets.remove(bullet)   
        else:
            for enemy in enemies:
                if bullet.colliderect(enemy):
                    enemy_remove = enemies.remove(enemy)
                    if bullet in bullets:
                        bullets.remove(bullet)
                    else:
                        pass

                    if enemy_remove == None:
                        kills += 1



    display.blit(blackhole_img, (blackhole.x, blackhole.y))

    display.blit(pause_render, (pause_rect.x, pause_rect.y))
    display.blit(lives_render, (pause_rect.x, pause_rect.y + 30 + lives_render.get_height()))

    display.blit(score_render, (width - score_render.get_width() - 30, pause_rect.y))
    display.blit(
        level_render,
        (width - score_render.get_width() - 30 ,pause_rect.y + 30 + level_render.get_height())
    )
    display.blit(
        kills_render,
        (width - kills_render.get_width() - 55 , pause_rect.y + 60 + level_render.get_height() + kills_render.get_height())
    )

    pygame.display.update()




    # Events
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pause = True
            
            if event.key == K_SPACE:
                bullet_ready = True
            


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

        level += 1 
        wavelength += 2
        enemy_speed += 1





    # LevelsETC
    score += 1/FPS
    if lives <= 0:
        game_over = True






    
    # Score
    if int(score) > int(highscore.get_highscore()):
        highscore.write_highscore(f"{int(score)}")







    # Bullet
    if bullet_ready:
        bullet = pygame.Rect(
            player.x + player_img.get_width()/2 - bullet_img.get_width()/2,
            player.y,
            bullet_img.get_width(),
            bullet_img.get_height()
        )
        
        bullets.append(bullet)
        bullet_ready = False





    # Buttons Clicks
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = list(pygame.mouse.get_pressed())
        
    if pause_rect.collidepoint(mouse_pos):
        if mouse_pressed[0] == True:
            pause = True 





    # Movement
    keys_pressed = pygame.key.get_pressed()
    
    if keys_pressed[K_a] and player.x > 0:
        player.x -= player_speed

    if keys_pressed[K_d] and player.x < width - player_img.get_height() - 10:
        player.x += player_speed

    if keys_pressed[K_w] and player.y > 0:
        player.y -= player_speed

    if keys_pressed[K_s] and player.y < height - player_img.get_height() - 10:
        player.y += player_speed


    # With keys

    elif keys_pressed[K_LEFT] and player.x > 0:
        player.x -= player_speed

    elif keys_pressed[K_RIGHT] and player.x < width - player_img.get_height() - 10:
        player.x += player_speed

    elif keys_pressed[K_UP] and player.y > 0:
        player.y -= player_speed

    elif keys_pressed[K_DOWN] and player.y < height - player_img.get_height() - 10:
        player.y += player_speed




    # Change POS
    if blackhole.y > height + blackhole_img.get_height():
        blackhole.y = -1000






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








    while game_over:
        over_display = pygame.display.set_mode((width, height))
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
                    print("Menu")


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




        pygame.display.update()


pygame.quit()