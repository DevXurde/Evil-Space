import pygame.font
import os

pygame.font.init()

title = "Evil Space"
width, height = 1700, 900

run = True

FPS = 60

planets = []

player_speed = 10
bullets = []
bullet_ready = False


pause = False

enemies = []

def create_player(player_img):
    player = pygame.Rect(width/2, height/2, player_img.get_width(), player_img.get_height())
    return player

enemy_speed = 3
wavelength = 6


font = pygame.font.SysFont("ComicSans", 70)

score = 0
level = 0
lives = 5

kills = 0

lost = False
menu = True



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

highscore_text = "Highscore"


