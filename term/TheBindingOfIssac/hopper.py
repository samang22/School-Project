from pico2d import *
import math
import random
import config
import game_world
import ID
import game_framework

HOPPER_IMAGE_SIZE = 64
HOPPER_DRAW_SIZE = 128

HOPPER_LIFE_MAX = 10
HOPPER_BLEEDING_STANDARD = 5
#HOPPER_NEW_DESTINATION_COOLTIME = 1.3

class Hopper:
    def __init__(self, _x, _y):
        print("Creating Hopper")
        self.x = _x
        self.y = _y
        self.speed = 100
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

        self.ID = ID.HOPPER

        self.isEnd = False

        self.damage = 1

        self.frame = 0
        self._time = 0

    def draw(self):
        if self.isBleeding:
            self.image.clip_draw(self.frame * HOPPER_IMAGE_SIZE, 0,                 HOPPER_IMAGE_SIZE, HOPPER_IMAGE_SIZE, self.x, self.y)
        else:
            #self.image.clip_draw(self.frame * HOPPER_IMAGE_SIZE, HOPPER_IMAGE_SIZE,  HOPPER_DRAW_SIZE, HOPPER_DRAW_SIZE, self.x, self.y)
            self.image.clip_draw(self.frame * HOPPER_IMAGE_SIZE, HOPPER_IMAGE_SIZE,  HOPPER_IMAGE_SIZE, HOPPER_IMAGE_SIZE, self.x, self.y)
            #self.image.clip_draw(self.frame * HOPPER_IMAGE_SIZE, HOPPER_DRAW_SIZE,  HOPPER_IMAGE_SIZE, HOPPER_IMAGE_SIZE, self.x, self.y)
            #self.image.clip_draw(10, )

        # BB 그리기
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())

    def update(self):
        self.frame_count += 1
        if self.frame_count % 2 == 0:
            self.frame = (self.frame + 1) % 12
        #self.frame = (self.frame + 1) % 12


        if self.life <= HOPPER_BLEEDING_STANDARD:
            self.isBleeding = True

        if self.x == self.tx and self.y == self.ty:
            self.tx = self.x + 100 * math.cos(math.radians(random.randrange(0, 360 + 1)))
            self.ty = self.y + 100 * math.sin(math.radians(random.randrange(0, 360 + 1)))

        dx, dy = self.tx - self.x, self.ty - self.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        if dist > 0:
            self.x += game_framework.frame_time * self.speed * dx / dist
            self.y += game_framework.frame_time * self.speed * dy / dist
        
            if dx < 0 and self.x < self.tx: self.x = self.tx
            if dx > 0 and self.x > self.tx: self.x = self.tx
            if dy < 0 and self.y < self.ty: self.y = self.ty
            if dy > 0 and self.y > self.ty: self.y = self.ty

        # 방 밖으로 나가지 않게 하기
        if self.x < 70: 
            self.x = 75
            self.tx = self.x + 100 * math.cos(math.radians(random.randrange(0, 360 + 1)))
            self.ty = self.y + 100 * math.sin(math.radians(random.randrange(0, 360 + 1)))
        if self.x > 730: 
            self.x = 725
            self.tx = self.x + 100 * math.cos(math.radians(random.randrange(0, 360 + 1)))
            self.ty = self.y + 100 * math.sin(math.radians(random.randrange(0, 360 + 1)))
        if self.y > 430:
            self.y = 425
            self.tx = self.x + 100 * math.cos(math.radians(random.randrange(0, 360 + 1)))
            self.ty = self.y + 100 * math.sin(math.radians(random.randrange(0, 360 + 1)))
        if self.y < 70:
            self.y = 75
            self.tx = self.x + 100 * math.cos(math.radians(random.randrange(0, 360 + 1)))
            self.ty = self.y + 100 * math.sin(math.radians(random.randrange(0, 360 + 1)))

    def SetPos(self, _x, _y):
        self.x = _x
        self.y = _y

    def Hit(self, damage):
        self.life -= damage
        if self.life <= 0:
            self.isEnd = True

    def get_bb(self):
        return self.x - (HOPPER_IMAGE_SIZE / 2) + 10, self.y - (HOPPER_IMAGE_SIZE / 2),self.x + (HOPPER_IMAGE_SIZE / 2) - 10, self.y + (HOPPER_IMAGE_SIZE / 2)

    def GetID(self):
        return self.ID

    def GetIsEnd(self):
        return self.isEnd
    def GetDamage(self):
        return self.damage 
