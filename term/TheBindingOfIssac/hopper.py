from pico2d import *
import math
import random

HOPPER_IMAGE_SIZE = 32
HOPPER_DRAW_SIZE = 128

HOPPER_LIFE_MAX = 10
HOPPER_BLEEDING_STANDARD = 5
#HOPPER_NEW_DESTINATION_COOLTIME = 1.3

class Hopper:
    def __init__(self):
        print("Creating Hopper")
        self.x = 400
        self.y = 300
        self.speed = 3
        self.frame = 0

        # 애니메이션이 너무 빨라 추가한 변수
        self.frame_count = 0
        self.image = load_image('../resource/Hopper.png')
        self.isDead = False
        #self.random_destination_x = 0
        #self.random_destination_y = 0

        self.life = HOPPER_LIFE_MAX
        self.isBleeding = False

        self.tx = self.x + 100 * math.cos(math.radians(random.randrange(0, 360 + 1)))
        self.ty = self.y + 100 * math.sin(math.radians(random.randrange(0, 360 + 1)))

    def draw(self):
        if self.isBleeding:
            self.image.clip_draw(self.frame * HOPPER_IMAGE_SIZE, 0,                 HOPPER_IMAGE_SIZE, HOPPER_IMAGE_SIZE, self.x, self.y)
        else:
            #self.image.clip_draw(self.frame * HOPPER_IMAGE_SIZE, HOPPER_IMAGE_SIZE,  HOPPER_DRAW_SIZE, HOPPER_DRAW_SIZE, self.x, self.y)
            self.image.clip_draw(self.frame * HOPPER_IMAGE_SIZE, HOPPER_IMAGE_SIZE,  HOPPER_IMAGE_SIZE, HOPPER_IMAGE_SIZE, self.x, self.y)
            #self.image.clip_draw(self.frame * HOPPER_IMAGE_SIZE, HOPPER_DRAW_SIZE,  HOPPER_IMAGE_SIZE, HOPPER_IMAGE_SIZE, self.x, self.y)
            #self.image.clip_draw(10, )

    def update(self):
        self.frame_count += 1
        if self.frame_count % 2 == 0:
            self.frame = (self.frame + 1) % 12
        #self.frame = (self.frame + 1) % 12


        if self.life <= HOPPER_BLEEDING_STANDARD:
            self.isBleeding = True

        if self.x == self.tx and self.y == self.ty:
            self.tx = self.x + 48 * math.cos(math.radians(random.randrange(0, 360 + 1)))
            self.ty = self.y + 48 * math.sin(math.radians(random.randrange(0, 360 + 1)))

        dx, dy = self.tx - self.x, self.ty - self.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        if dist > 0:
            self.x += self.speed * dx / dist
            self.y += self.speed * dy / dist
        
        if dx < 0 and self.x < self.tx: self.x = self.tx
        if dx > 0 and self.x > self.tx: self.x = self.tx
        if dy < 0 and self.y < self.ty: self.y = self.ty
        if dy > 0 and self.y > self.ty: self.y = self.ty

    def Hit(self):
        self.life -= 1