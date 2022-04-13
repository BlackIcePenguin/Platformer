from Parameters import *
from Sprites import Player, SpriteSheet, Tiles, SavePoint, Enemy

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

running = True
start_screen = True
end = False

tile_map = SpriteSheet("warped city files/ENVIRONMENT/tileset.png")

# Getting all of the sprites to work, looks messy cause of how much transforming and due to a non gird spritesheet
background0 = pygame.image.load('warped city files/ENVIRONMENT/background/skyline-a.png')
background0 = pygame.transform.scale2x(background0)
background0 = pygame.transform.scale2x(background0)
background1 = pygame.image.load('warped city files/ENVIRONMENT/background/skyline-b.png')
background1 = pygame.transform.scale2x(background1)
background1 = pygame.transform.scale2x(background1)
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
death_block = pygame.image.load("warped city files/SPRITES/misc/hurt_block.png")
booster_block = pygame.image.load("warped city files/SPRITES/misc/booster.png")
end_door = pygame.image.load("warped city files/SPRITES/misc/End_Door.png")
drone = pygame.image.load("warped city files/SPRITES/misc/drone/drone-1.png")

player = Player(temp_char)
player_group.add(player)

# Start one less than the level number, currently ascending 1->num
layout_number = 0


def generate_level(level):
    for entity in all_sprites:
        entity.kill()
    for entity in enemy_group:
        entity.kill()
    layout = level
    layout_length = len(layout[0])
    layout_height = len(layout)
    # For tiles with Collision
    for row_val in range(0, layout_length):
        for column_val in range(0, layout_height):
            if layout[column_val][row_val] == 'B':
                tile = Tiles(screen, block, TILE_SIZE * row_val, TILE_SIZE * column_val)
                tile_group.add(tile)
                all_sprites.add(tile)
            elif layout[column_val][row_val] == 'R':
                tile = Tiles(screen, right_wall, TILE_SIZE * row_val, TILE_SIZE * column_val)
                tile_group.add(tile)
                all_sprites.add(tile)
            elif layout[column_val][row_val] == 'L':
                tile = Tiles(screen, left_wall, TILE_SIZE * row_val, TILE_SIZE * column_val)
                tile_group.add(tile)
                all_sprites.add(tile)
            elif layout[column_val][row_val] == 'T':
                tile = Tiles(screen, trapezoid_plat, TILE_SIZE * row_val, TILE_SIZE * column_val)
                tile_group.add(tile)
                all_sprites.add(tile)
            elif layout[column_val][row_val] == 'D':
                tile = Tiles(screen, death_block, TILE_SIZE * row_val, TILE_SIZE * column_val)
                danger_group.add(tile)
                all_sprites.add(tile)
            elif layout[column_val][row_val] == '^':
                tile = Tiles(screen, booster_block, TILE_SIZE * row_val, TILE_SIZE * column_val)
                lift_group.add(tile)
                all_sprites.add(tile)
            elif layout[column_val][row_val] == 'E':
                enemy = Enemy(screen, drone, TILE_SIZE * row_val, TILE_SIZE * column_val, 64)
                enemy_group.add(enemy)

    # For tiles without Collision
    for row_val in range(0, layout_length):
        for column_val in range(0, layout_height):
            if layout[column_val][row_val] == 'P':
                background = Tiles(screen, pillar, TILE_SIZE * row_val, TILE_SIZE * column_val)
                background_group.add(background)
                all_sprites.add(background)
            elif layout[column_val][row_val] == 'F':
                flag1 = SavePoint(screen, TILE_SIZE * row_val, TILE_SIZE * column_val)
                flag_group.add(flag1)
                all_sprites.add(flag1)
            elif layout[column_val][row_val] == '#':
                background = Tiles(screen, end_door, TILE_SIZE * row_val, TILE_SIZE * column_val)
                door_group.add(background)
                all_sprites.add(background)


def start():
    start1 = start_font.render(f'Welcome to my Platformer!', True, BLUE)
    start2 = start_font.render(f'Move with either the arrow keys or A and D', True, WHITE)
    start3 = start_font.render(f'Space, Up arrow, or W to jump', True, WHITE)
    start4 = start_font.render(f'Hold S or down arrow for a second to toggle screen scrolling', True, WHITE)
    start5 = start_font.render(f'Flags are your respawn points', True, WHITE)
    start6 = start_font.render(f'By moving into walls you will cling onto them, which returns your jump', True, WHITE)
    start7 = start_font.render(f'You can jump in the air if you have not used your jump', True, WHITE)
    start8 = start_font.render(f'Use Q and E to manually scroll', True, WHITE)
    start9 = start_font.render(f'There are 3 levels to beat', True, GREEN)
    start0 = start_font.render(f'Press any key to start', True, GREEN)

    screen.blit(background0, (0, 0))
    screen.blit(background1, (503, 0))
    screen.blit(background0, (1000, 0))
    screen.blit(start1, [290, 50])
    screen.blit(start2, [185, 200])
    screen.blit(start3, [265, 250])
    screen.blit(start4, [95, 300])
    screen.blit(start5, [270, 450])
    screen.blit(start6, [60, 500])
    screen.blit(start7, [120, 550])
    screen.blit(start8, [270, 350])
    screen.blit(start9, [290, 710])
    screen.blit(start0, [320, 760])
    pygame.display.flip()
    waiting = True
    while waiting:
        for z in pygame.event.get():
            if z.type == pygame.QUIT:
                return False
            if z.type == pygame.KEYDOWN:
                return True


while start_screen:
    if start():
        start_screen = False
        break
    else:
        running = False
        pygame.quit()
        break
generate_level(layout_list[layout_number])


while running:

    player_respawn_flag = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_p:
                pass
    # Adds the extending hit box to make sure the player can collide properly
    if player.left:
        player_collide = pygame.Rect(player.rect.x + player.change_x, player.rect.y + player.change_y,
                                     player.rect.width - player.change_x, player.rect.height + 3)
    else:
        player_collide = pygame.Rect(player.rect.x + player.change_x, player.rect.y + player.change_y,
                                     player.rect.width + player.change_x, player.rect.height + 3)
    # All of the collision, was hard to get right
    for item in tile_group:
        tile_rect = pygame.Rect.copy(item.rect)
        if pygame.Rect.colliderect(tile_rect, player_collide):
            if tile_rect.midleft <= player_collide.midright:
                if player.change_x > 0:
                    player.change_x = 0
            if tile_rect.midright >= player_collide.midleft:
                if player.change_x < 0:
                    player.change_x = 0
            if tile_rect.bottom >= player_collide.top:
                if player.change_y < 0:
                    player.change_y = 0
            if tile_rect.top <= player_collide.bottom:
                while pygame.Rect.colliderect(player.rect, tile_rect):
                    player.rect.y -= 1
                if player.change_y > 0:
                    player.change_y = 0
                player.falling = False
    if player.rect.right > SCREEN_WIDTH:
        while player.rect.right > SCREEN_WIDTH:
            player.rect.x -= 1
    elif player.rect.left < 0:
        while player.rect.left < 0:
            player.rect.x += 1
    # The lift item code, kinda wonky, was the initial try at collision
    for item in lift_group:
        if pygame.sprite.collide_rect(player, item):
            if item.rect.top <= player_collide.bottom + player.change_y:
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

    # Defining the rules for the scrolling
    if player.cam_unlock and not player.danger:
        if player.scroll_x:
            if not player.idle:
                for item in all_sprites:
                    item.change_x = -player.change_x
                for item in enemy_group:
                    item.rect.x += -player.change_x
                    item.rect_init += -player.change_x
            else:
                pass
        elif not player.scroll_x:
            for item in all_sprites:
                item.change_x = 0
            for item in enemy_group:
                item.rect.x += 0
                item.rect_init += 0
        if player.scroll_y:
            for item in all_sprites:
                item.change_y = -player.change_y
    elif not player.cam_unlock:
        for item in all_sprites:
            item.change_x = 0
        for item in enemy_group:
            item.rect.x += 0
            item.rect_init += 0

    if player.move_cam:
        if player.cam_direct == 0:
            if player.rect.x + 5 < SCREEN_WIDTH * 0.8:
                for item in all_sprites:
                    item.rect.x += 5
                for item in enemy_group:
                    item.rect.x += 5
                    item.rect_init += 5
                player.rect.x += 5
        if player.cam_direct == 1:
            if player.rect.x - 5 > SCREEN_WIDTH * 0.2:
                for item in all_sprites:
                    item.rect.x -= 5
                for item in enemy_group:
                    item.rect.x -= 5
                    item.rect_init -= 5
                player.rect.x -= 5

    # Sets flags as the active one and does collision for them
    for item in flag_group:
        if pygame.sprite.collide_rect(player, item) and not item.active:
            for flag in flag_group:
                flag.active = False
            item.active = True
        if item.active:
            player.x_init = item.rect.x
            player.y_init = item.rect.top
    # Code to send player back when they "die"
    for item in danger_group:
        if pygame.sprite.collide_rect(player, item):
            player.rect.x = player.x_init
            player.rect.y = player.y_init

    # Drawing all of the images and sprites
    screen.fill(OCEAN_BLUE)
    screen.blit(background0, (0, 0))
    screen.blit(background1, (503, 0))
    screen.blit(background0, (1000, 0))
    background_group.draw(screen)
    enemy_group.draw(screen)
    # These were to test the hit box, keeping in sake of potential future debugging
    # pygame.draw.rect(screen, YELLOW, player_collide, width=0)
    # pygame.draw.rect(screen, RED, player.rect, width=0)
    tile_group.draw(screen)
    lift_group.draw(screen)
    danger_group.draw(screen)
    flag_group.draw(screen)
    door_group.draw(screen)

    player_group.draw(screen)
    # Updating the enemies and player
    for instance in enemy_group:
        instance.update()
    # Running the player update, the equals 3 just makes sure that the quit key works in the loop
    if player.update() == 3:
        break
    # Checking for the enemy collision
    for instance in enemy_group:
        if pygame.sprite.collide_rect(instance, player):
            if instance.rect.centery <= player.rect.bottom:
                player.danger = True
            elif instance.rect.centery > player.rect.bottom:
                player.change_y = -10
            else:
                pass

    for door in door_group:
        if pygame.sprite.collide_rect(door, player):
            layout_number += 1
            if layout_number >= 3:
                end = True
                running = False
                break
            else:
                generate_level(layout_list[layout_number])
                player.rect.x = 240
                player.rect.y = SCREEN_HEIGHT - 150

    # The respawning code, works when the player activates the danger state, i.e. Dies
    if player.danger:
        if 0 < player.x_init < SCREEN_WIDTH and 0 < player.y_init < SCREEN_HEIGHT:
            player.rect.x = player.x_init
            player.rect.y = player.y_init
        else:
            if player.x_init < 0:
                shift_x_change = (SCREEN_WIDTH * 0.1) - player.x_init
                for flag in flag_group:
                    if flag.active:
                        player.rect.y = flag.rect.y
                for item in all_sprites:
                    item.change_x = shift_x_change
                for item in enemy_group:
                    item.rect.x += shift_x_change
                    item.rect_init += shift_x_change
                player_respawn_flag = True
            elif player.x_init > SCREEN_WIDTH:
                shift_x_change = (SCREEN_WIDTH * 0.9) - player.x_init
                for item in all_sprites:
                    item.change_x = shift_x_change
                for item in enemy_group:
                    item.rect.x += shift_x_change
                    item.rect_init += shift_x_change
                player_respawn_flag = True
    # Updates everything else
    all_sprites.update()
    # Tells the game where to send the player
    if player_respawn_flag:
        for flag in flag_group:
            if active_flag:
                player.x_init = flag.rect.x
                player.y_init = flag.rect.top
        player.rect.x = player.x_init
        player.rect.y = player.y_init
    pygame.display.flip()

    clock.tick(FPS)

if end:
    for sprite in all_sprites:
        sprite.kill()
    for sprite in enemy_group:
        sprite.kill()
    player.kill()

    end1 = start_font.render(f'Congratulations! You beat the Game', True, GREEN)
    end2 = start_font.render(f'Press any key to quit', True, GREEN)
    screen.blit(background0, (0, 0))
    screen.blit(background1, (503, 0))
    screen.blit(background0, (1000, 0))
    screen.blit(end1, [360, 350])
    screen.blit(end2, [445, 450])
    pygame.display.flip()
    waiting1 = True
    while waiting1:
        for m in pygame.event.get():
            if m.type == pygame.QUIT:
                waiting1 = False
            if m.type == pygame.KEYDOWN:
                waiting1 = False

# Runs when main game loop ends
pygame.quit()
