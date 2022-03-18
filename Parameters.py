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
temp_char = "warped city files/SPRITES/misc/testing.png"

player_group = pygame.sprite.Group()
tile_group = pygame.sprite.Group()
background_group = pygame.sprite.Group()
danger_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
lift_group = pygame.sprite.Group()
flag_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

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
# Layouts, in ascending number for stages
layout_list = []
LAYOUT1 = ["DBBBBBBBBBBBBBBBBBBBBBBBBBBBRBBBBBBBBBBBBBBBDDBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
           "D                           R  F            DD                   RL                   DL                 R",
           "D                                           DD                                        D   #               ",
           "D                            BBBBBBB        DD                   BB                   DL                 R",
           "D                              ^^^RL        DD                    F                   D                   ",
           "D                              ^^^          DD                                        DBBBBBBBBBBBBBBBBBBB",
           "D                              ^^^DD        DB         BBB       BB                   D             ^^^^^D",
           "D    BBBBBBBBBBBBBBBBBBBBBBBBBBBBBDD        DD         DDD       DD   E               D             ^^^^^D",
           "D                                 DD        DD                   DD                   D             ^^^^^D",
           "D                                 DD        DD                   DD           E       D             ^^^^^D",
           "D                                 DD        DD                   DD                   D             DDDDDD",
           "D       B             B           DD        DB                   DDDDDDDDDDDDDD       D                  D",
           "D                                 DD        DD       DD          DD                   D                  D",
           "D              E                  DD        DD       BD          DD                   D                  D",
           "D                                 DD                             DD                   D                  D",
           "D                                TDD                             DD                   D                  D",
           "D                                 DD                             DL                   D                  D",
           "D                                 DD                             DD                                      D",
           "D                                 DD                  #          DD                                      D",
           "D                            E    DD                             DD                              E       D",
           "D      F             E            DD    DDDDDBBBBBDDDDD          DD                                      D",
           "D                                 DD    PPPPPPPPPPPPPPP          DD      E                               D",
           "D     BBBB          BBBB          DD                             DD            E                         D",
           "D     P  P          P  P          DD    PPPPPPPPPPPPPPP          DD                   E       E          D",
           "D000000000000000000000000000000000DD00000000000000000000000000000DD00000000000000000000000000000000000000D"]
layout_list.append(LAYOUT1)

LAYOUT2 = ["DBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBDDBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
           "D                                                                                                        D",
           "D                                                                                                        D",
           "D                                                                                                        D",
           "D                                                                                                        D",
           "D                                                                                                        D",
           "D                                                                                                        D",
           "D                                                                                                        D",
           "D                                                                                                        D",
           "D                                                                                                        D",
           "D                                                                                                        D",
           "D                                                                                                        D",
           "D                                                                                                        D",
           "D                                                                                                        D",
           "D         E                                                                                              D",
           "D                                                                                                        D",
           "D                                                                                                        D",
           "D                                                                                                        D",
           "D                                                                                                        D",
           "D                                                                                                        D",
           "D      F                                                                                                 D",
           "D                                                                                                        D",
           "D     BBBB                                                                                               D",
           "D                                                                                                        D",
           "D00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000D"]
layout_list.append(LAYOUT2)
