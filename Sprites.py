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
        self.change_x = 0
        self.change_y = 0
        self.frame = 0
        self.frame_rate = 180
        self.walk = False
        self.run = False
        self.idle = True

    def update(self):
        current_time = pygame.time.get_ticks()
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        keys = pygame.key.get_pressed()
        self.idle = True
        self.walk = False
        self.run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    break
                if event.key == pygame.K_RIGHT:
                    self.run = False
                    self.walk = True
                    self.idle = False
        if keys[pygame.K_LSHIFT and (pygame.K_RIGHT or pygame.K_LEFT)]:
            self.run = True
            self.walk = False
            self.idle = False

        if keys[pygame.K_RIGHT]:
            self.change_x = 4
        elif keys[pygame.K_LEFT]:
            self.change_x = -4
        elif keys[pygame.K_UP]:
            self.change_y = -4
        elif keys[pygame.K_DOWN]:
            self.change_y = 4
        else:
            self.change_x = 0
            self.change_y = 0
        if self.rect.left + self.change_x <= 0 or self.rect.right + self.change_x >= SCREEN_WIDTH:
            self.change_x = 0
        if self.rect.top + self.change_y <= 0 or self.rect.bottom + self.change_y >= SCREEN_HEIGHT:
            self.change_y = 0

        if current_time - self.prev_update > self.frame_rate:
            self.prev_update = current_time
            self.frame += 1
        if self.run:
            pass
        elif self.walk:
            if keys[pygame.K_RIGHT]:
                if self.frame > len(Walk_Right_List):
                    self.frame = 0
                self.image = Walk_Right_List[self.frame]
                self.rect = self.image.get_rect()
        elif self.idle:
            if self.frame > len(Idle_List) - 1:
                self.frame = 0
            self.image = Idle_List[self.frame]
            self.rect = self.image.get_rect()

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

    def update(self):
        pass



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


