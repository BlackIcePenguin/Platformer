import pygame
import math
import random

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

# Cyberpunk assets: Artwork created by Luis Zuno @ansimuz
temp_char = "warped city files/SPRITES/player/idle/idle-1.png"

# Setting up all of the movement lists
Walk_Right_List = []
for i in range(1, 17):
    image = pygame.image.load(f"warped city files/SPRITES/player/walk/walk-{i}.png")
    Walk_Right_List.append(image)
Walk_Left_List = [pygame.transform.flip(player, True, False) for player in Walk_Right_List]
Idle_List = []
for i in range(1, 5):
    image = pygame.image.load(f"warped city files/SPRITES/player/idle/idle-{i}.png")
    Idle_List.append(image)
print(Idle_List)

# Layout, current is for testing the character
LAYOUT = ["BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
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
          "L000000P000B00000000000000P0000000R",
          "L000000P000P0000000000000000000000R",
          "L000000P000000000T0000000000000000R",
          "L000000P0000000000P00000T000000000R",
          "L000000P000P0000000000000P00000000R",
          "L000000P00000000000000000000000000R",
          "BBBBBBBBB00000BBBBBBBBB00000BBBBBBB"]

LAYOUT_LENGTH = len(LAYOUT[0])
LAYOUT_HEIGHT = len(LAYOUT)
