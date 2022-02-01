import pygame
import random
from Parameters import *
from Sprites import Player, SpriteSheet, Tiles

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

running = True

player_group = pygame.sprite.Group()
tile_group = pygame.sprite.Group()
background_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

tile_map = SpriteSheet("warped city files/ENVIRONMENT/tileset.png")

# Getting all of the sprites to work, looks messy cause of how much transforming and due to a non gird spritesheet
right_wall = tile_map.image_at((16, 16, 16, 48))
right_wall = pygame.transform.scale2x(right_wall)
left_wall = tile_map.image_at((112, 16, 16, 48))
left_wall = pygame.transform.scale2x(left_wall)
trapezoid_plat = tile_map.image_at((104, 176, 47, 16), -1)
trapezoid_plat = pygame.transform.scale2x(trapezoid_plat)
block = tile_map.image_at((336, 16, 16, 16))
block = pygame.transform.scale2x(block)
pillar = tile_map.image_at((192, 16, 16, 48))
pillar = pygame.transform.scale2x(pillar)

player = Player(temp_char)
player_group.add(player)
# all_sprites.add(player)

# For tiles with Collision
for row_val in range(0, LAYOUT_LENGTH):
    for column_val in range(0, LAYOUT_HEIGHT):
        if LAYOUT[column_val][row_val] == 'B':
            tile = Tiles(screen, block, TILE_SIZE * row_val, TILE_SIZE * column_val)
            tile_group.add(tile)
            all_sprites.add(tile)
        elif LAYOUT[column_val][row_val] == 'R':
            tile = Tiles(screen, right_wall, TILE_SIZE * row_val, TILE_SIZE * column_val)
            tile_group.add(tile)
            all_sprites.add(tile)
        elif LAYOUT[column_val][row_val] == 'L':
            tile = Tiles(screen, left_wall, TILE_SIZE * row_val, TILE_SIZE * column_val)
            tile_group.add(tile)
            all_sprites.add(tile)
        elif LAYOUT[column_val][row_val] == 'T':
            tile = Tiles(screen, trapezoid_plat, TILE_SIZE * row_val, TILE_SIZE * column_val)
            tile_group.add(tile)
            all_sprites.add(tile)


# For tiles without Collision
for row_val in range(0, LAYOUT_LENGTH):
    for column_val in range(0, LAYOUT_HEIGHT):
        if LAYOUT[column_val][row_val] == 'P':
            background = Tiles(screen, pillar, TILE_SIZE * row_val, TILE_SIZE * column_val)
            background_group.add(background)
            all_sprites.add(background)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    floor = False
    r_wall = False
    l_wall = False
    roof = False

    for item in tile_group:
        if pygame.sprite.collide_rect(player, item):
            if item.rect.top <= player.rect.bottom + player.change_y:
                player.rect.y -= player.change_y
                player.falling = False
                player.change_y = 0

            elif item.rect.bottom >= player.rect.top + player.change_y:
                player.rect.y += player.change_y
                player.change_y = 0

            if item.rect.right >= player.rect.left + player.change_x:
                player.rect.x += player.change_x
                player.change_x = 0
            elif item.rect.left <= player.rect.right + player.change_x:
                player.rect.x += player.change_x
                player.change_x = 0

    screen.fill(OCEAN_BLUE)
    background_group.draw(screen)
    tile_group.draw(screen)
    player_group.draw(screen)

    if player.update() == 3:
        break
    all_sprites.update()
    pygame.display.flip()

    clock.tick(FPS)

# Runs when main game loop ends
pygame.quit()
