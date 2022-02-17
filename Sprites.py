import pygame
import random
from Parameters import *
pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, image_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT - self.rect.height
        self.prev_update = pygame.time.get_ticks()
        self.rect.x = 240
        self.rect.y = SCREEN_HEIGHT - 150
        self.x_init = self.rect.x
        self.y_init = self.rect.y
        self.change_x = 0
        self.change_y = 0
        self.frame = 0
        self.frame_rate = 180
        self.walk = False
        self.run = False
        self.right = True
        self.left = False
        self.jumping = False
        self.falling = False
        self.moving = True
        self.air_L = False
        self.scroll_x = False
        self.scroll_y = False
        self.danger = False

    def update(self):
        current_time = pygame.time.get_ticks()
        if not self.scroll_x:
            self.rect.x += self.change_x
        if not self.scroll_y:
            self.rect.y += self.change_y

        # pygame.draw.rect(self.image, WHITE, [0, 0, self.rect.width, self.rect.height])

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    break

        if keys[pygame.K_SPACE]:
            self.change_y = -10
        if keys[pygame.K_LSHIFT]:
            self.run = True

        if keys[pygame.K_LCTRL]:
            self.walk = True

        if keys[pygame.K_UP] and not self.jumping and not self.falling:
            self.jumping = True
            self.change_y = -10
        else:
            self.jumping = False
        self.change_y += 0.3
        if self.change_y <= 0:
            self.jumping = False
            self.falling = True
        if self.change_y >= 10:
            self.change_y = 10

        if keys[pygame.K_DOWN]:
            self.jumping = False

        if keys[pygame.K_RIGHT]:
            self.change_x = 2
            self.right = True
            self.left = False
            self.moving = True
            self.walk = True
            if self.rect.right + self.change_x >= SCREEN_WIDTH * 0.8:
                self.scroll_x = True
            else:
                self.scroll_x = False

        elif keys[pygame.K_LEFT]:
            self.change_x = -2
            self.right = False
            self.left = True
            self.moving = True
            self.walk = True
            if self.rect.left + self.change_x <= SCREEN_WIDTH * 0.2:
                self.scroll_x = True
            else:
                self.scroll_x = False

        else:
            self.change_x = 0

        if self.scroll_x:
            if self.left:
                if self.rect.left + self.change_x > SCREEN_WIDTH * 0.2:
                    self.scroll_x = False
            if self.right:
                if self.rect.right + self.change_x < SCREEN_WIDTH * 0.8:
                    self.scroll_x = False

        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    self.run = False
                if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                    self.walk = False

        if self.rect.left + self.change_x <= 0 or self.rect.right + self.change_x >= SCREEN_WIDTH:
            self.change_x = 0
        if self.rect.top + self.change_y <= 0 or self.rect.bottom + self.change_y >= SCREEN_HEIGHT:
            self.change_y = 0
            self.danger = True
        else:
            self.danger = False

        if self.run:
            self.change_x *= 2

        if current_time - self.prev_update > self.frame_rate:
            self.prev_update = current_time
            self.frame += 1
        if self.falling or self.jumping:
            if self.frame > len(Air_List) - 1:
                self.frame = 0
            self.image = Air_List[self.frame]
        elif self.run:
            if self.right:
                if self.frame > len(Run_Right_List) - 1:
                    self.frame = 0
                self.image = Run_Right_List[self.frame]
            elif self.left:
                if self.frame > len(Run_Left_List) - 1:
                    self.frame = 0
                self.image = Run_Left_List[self.frame]
        elif self.walk:
            if self.right:
                if self.frame > len(Walk_Right_List) - 1:
                    self.frame = 0
                self.image = Walk_Right_List[self.frame]
            elif self.left:
                if self.frame > len(Walk_Left_List) - 1:
                    self.frame = 0
                self.image = Walk_Left_List[self.frame]
        else:
            if self.frame > len(Idle_List) - 1:
                self.frame = 0
            self.image = Idle_List[self.frame]

        self.walk = False
        self.run = False

        return 0


class Tiles(pygame.sprite.Sprite):
    def __init__(self, display, tile_type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.display = display
        self.image = tile_type
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_shift = self.rect.width
        self.y_shift = self.rect.height
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y


class SavePoint(pygame.sprite.Sprite):
    def __init__(self, display, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.display = display
        self.image = disabled_flag
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0
        self.active = False

    def store_state(self):
        if self.active:
            self.image = active_flag
        if not self.active:
            self.image = disabled_flag

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        self.store_state()


class SpriteSheet:

    def __init__(self, filename):
        """Load the sheet."""
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

    def image_at(self, rectangle, color_key=None):
        """Load a specific image from a specific rectangle."""
        """rectangle is a tuple with (x, y, x+offset, y+offset)"""
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if color_key is not None:
            if color_key == -1:
                color_key = image.get_at((0,0))
            image.set_colorkey(color_key, pygame.RLEACCEL)
        return image

    def images_at(self, rects, color_key=None):
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at(rect, color_key) for rect in rects]

    def load_strip(self, rect, image_count, color_key=None):
        """Load a whole strip of images, and return them as a list."""
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, color_key)

    def load_grid_images(self, num_rows, num_cols, x_margin=0, x_padding=0,
                         y_margin=0, y_padding=0):
        """Load a grid of images.
        x_margin is the space between the top of the sheet and top of the first
        row. x_padding is space between rows. Assumes symmetrical padding on
        left and right.  Same reasoning for y. Calls self.images_at() to get a
        list of images.
        """

        sheet_rect = self.sheet.get_rect()
        sheet_width, sheet_height = sheet_rect.size

        # To calculate the size of each sprite, subtract the two margins,
        #   and the padding between each row, then divide by num_cols.
        # Same reasoning for y.
        x_sprite_size = (sheet_width - 2 * x_margin - (num_cols - 1) * x_padding) / num_cols
        y_sprite_size = (sheet_height - 2 * y_margin - (num_rows - 1) * y_padding) / num_rows

        sprite_rects = []
        for row_num in range(num_rows):
            for col_num in range(num_cols):
                # Position of sprite rect is margin + one sprite size
                #   and one padding size for each row. Same for y.
                x = x_margin + col_num * (x_sprite_size + x_padding)
                y = y_margin + row_num * (y_sprite_size + y_padding)
                sprite_rect = (x, y, x_sprite_size, y_sprite_size)
                sprite_rects.append(sprite_rect)

        return self.images_at(sprite_rects)


