import pygame
from pygame import fastevent
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
from scripts.settings import *
from scripts.pause import pause_game
from scripts.game_over import gameover_screen
from scripts.menu import menu_screen

pygame.init()
pygame.font.init()




display = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)

clock = Clock()




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
# player = pygame.Rect(width/2, height/2, player_img.get_width(), player_img.get_height())
player = create_player(player_img)
# PlayerBullet
bullet_img = pygame.image.load(
    os.path.join("assets", "bullet.png"))





# Enemy
enemy_img = pygame.image.load(os.path.join("assets", "enemy.png")).convert_alpha()



# Pause
pause_render = font.render("Pause", True, (255,255,255))
pause_rect = pygame.Rect(
    0 + 30,
    0 + 10,
    pause_render.get_width(),
    pause_render.get_height()
)




highscore = Highscore()


menu_result = menu_screen(display)
if menu_result:
    lost = False
    run = True
else:
    run = False

while run:

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
        lost = True
        

    if lost:
        run = False

        gameover_result = gameover_screen(score, kills, display)
        if gameover_result:
            lost = False

            from scripts.settings import *
            enemies.clear()
            bullets.clear()

            player = create_player(player_img)

            run = True






    
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






    # Pause
    while pause:
        pause_game_result = pause_game()
        if pause_game_result == "resume":
            pause = False

        if pause_game_result == "menu":
            pause = False
            menu_result = menu_screen()
            if menu_result:
                run = True

pygame.quit()