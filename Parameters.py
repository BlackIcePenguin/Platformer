import pygame
import math
import random

pygame.init()

# Color Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GREEN = (11, 46, 2)
BROWN = (41, 21, 2)
YELLOW = (239, 184, 16)
MAGENTA = (204, 0, 153)
LIGHT_BROWN = (153, 102, 34)
SKY_BLUE = (179, 255, 255)
OCEAN_BLUE = (26, 117, 255)
PEACH = (255, 204, 153)
COLORS = [RED, GREEN, BLUE, WHITE]

# Create Math Constant
PI = math.pi

# To convert from Degrees to Radians -> angle * (pi / 180)

# Game Constants
FPS = 60
SCREEN_WIDTH = 1120
SCREEN_HEIGHT = 800
TILE_SIZE = 32
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# For use in respawning


# Cyberpunk assets: Artwork created by Luis Zuno @ansimuz
temp_char = "warped city files/SPRITES/player/PlayerInit.png"

player_group = pygame.sprite.Group()
tile_group = pygame.sprite.Group()
background_group = pygame.sprite.Group()
danger_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
lift_group = pygame.sprite.Group()
flag_group = pygame.sprite.Group()

active_flag = pygame.image.load('warped city files/SPRITES/misc/active_save_flag.png')
disabled_flag = pygame.image.load('warped city files/SPRITES/misc/non_active_save_flag.png')

# Setting up all of the movement lists
Walk_Right_List = []
for i in range(1, 17):
    image = pygame.image.load(f"warped city files/SPRITES/player/walk/walk-{i}.png")
    crop = image.subsurface((24, 14, 28, 53))
    Walk_Right_List.append(crop)
Walk_Left_List = [pygame.transform.flip(player, True, False) for player in Walk_Right_List]
Idle_List = []
for i in range(1, 5):
    image = pygame.image.load(f"warped city files/SPRITES/player/idle/idle-{i}.png")
    crop = image.subsurface((26, 16, 24, 51))
    Idle_List.append(crop)
Run_Right_List = []
for i in range(1, 9):
    image = pygame.image.load(f"warped city files/SPRITES/player/run/run-{i}.png")
    crop = image.subsurface((10, 16, 45, 51))
    Run_Right_List.append(crop)
Run_Left_List = [pygame.transform.flip(player, True, False) for player in Run_Right_List]
Air_List = []
for i in range(1, 5):
    image = pygame.image.load(f"warped city files/SPRITES/player/jump/jump-{i}.png")
    crop = image.subsurface((10, 14, 45, 53))
    Air_List.append(crop)
# Layout, current is for testing the character
LAYOUT01 = ["BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
            "L00000000P0P000000000000000000P0000",
            "L00000000P0P00000000000000000000000",
            "L0000000000000000000000000000000000",
            "L00000000000000000000000000000P000B",
            "L00000000P0P0000000000000000000000R",
            "L000000000000000000000000000000000R",
            "L0000000000000000000000000000T0000R",
            "L00000000P0P0000000000000000000000R",
            "L000000000000000000000000000000000R",
            "L000000000000000000000000000000000R",
            "L00000000T000000000000000T00000000R",
            "L0000000000000000000000000P0000000R",
            "LBB00000000000000T0000000000000000R",
            "L00000000000000000P000000000000000R",
            "L0000000000000000000000000P0000000R",
            "L00000T000000000000000000000000000R",
            "L000000P0000000000P000000000000000R",
            "L000000P000B000000000000D0P0000000R",
            "L000000P000P000000000^000000000000R",
            "L000000P000000000T000^000000000000R",
            "L000000P0000000000P00^00T000000000R",
            "L000000P000P000000000^000P00000000R",
            "L000000P00000000000000000000000000R",
            "BBBBBBBBB00000BBBBBBBBB00000BBBBBBB"]
LAYOUT2 = ["00000000000000000000000000000000000000000000000",
           "00000000000000000000000000000000000000000000000",
           "00000000000000000000000000000000000000000000000",
           "00000000000000000000000000000000000000000000000",
           "00000000000000000000000000T00000000000000000000",
           "00000000000000000000000000000000000000000000000",
           "00000000000000000000000000000000000000000000000",
           "00000000000000000000000000000000000000000000000",
           "00000000T000000000000000000000D0000000000000000",
           "00000000000000000000000000000000000000000000000",
           "00000000000000000000000000000000000000000000000",
           "0000D000000000000000000000000000000000000000000",
           "00000000000000000000000000000000000000000000000",
           "0000000000000000B000000000000000000000000000000",
           "00000000000000000000000000000000000000000000000",
           "000000000000000000000000000D0000000000000000000",
           "00000000000000000000000000000000000000000000000",
           "000000000000000BDDB0000000000000000000000000000",
           "00000BB000000000LR00000000BB0000000000000000000",
           "0000000000000000LR0000000000000000000F000000000",
           "R000000000000000LR00000000000000000000000000000",
           "R000000000000000LR00000000000000000000000000000",
           "R000000000000000LR0000000000000F000000000000000",
           "R000000000000000LR00000000000000000000000000000",
           "BBBBBBBBBBBBBBBB00BBBBBBBBBBBBBBBBBBBBBBBBBBBBB"]

LAYOUT = LAYOUT2

LAYOUT_LENGTH = len(LAYOUT[0])
LAYOUT_HEIGHT = len(LAYOUT)
