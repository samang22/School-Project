from pico2d import *
import config
import ID
import game_framework

TEAR_DIRECTION_UP = 1
TEAR_DIRECTION_DOWN = 2
TEAR_DIRECTION_LEFT = 3
TEAR_DIRECTION_RIGHT = 4

TEAR_IMAGE_SIZE = 64



class Tear:
    FLY_FRONT, FLY_RIGHT, FLY_LEFT = range(3) 

    #tear_image = None
    def __init__(self):
        print("Creating Tear")
        self.x = 0
        self.y = 0
        self.speed = 175
        self.tear_frame = 0
        self.isPopping = False
        self.isPop = False
        self.direction = 0
        self.tear_image = load_image('../resource/Tear.png')
        self.damage = 3

        self.fly = Tear.FLY_FRONT
        self.ID = ID.TEAR
    def draw(self):
        #터지기 전
        if self.isPopping == False:
            self.tear_image.clip_draw(0                             , 0, TEAR_IMAGE_SIZE, TEAR_IMAGE_SIZE, self.x, self.y)
        # 터지는 중
        elif self.isPopping == True:
            self.tear_image.clip_draw(self.tear_frame * TEAR_IMAGE_SIZE   , 0, TEAR_IMAGE_SIZE, TEAR_IMAGE_SIZE, self.x, self.y)
        # BB 그리기
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())


    def update(self):
        if self.tear_frame > 10:
                self.isPop = True
        if self.isPopping == False:
            if self.direction == TEAR_DIRECTION_UP:
                self.y += self.speed * game_framework.frame_time
                if self.fly == Tear.FLY_LEFT:
                    self.x -= self.speed / 3 * game_framework.frame_time
                elif self.fly == Tear.FLY_RIGHT:
                    self.x += self.speed / 3 * game_framework.frame_time
            elif self.direction == TEAR_DIRECTION_DOWN:
                self.y -= self.speed * game_framework.frame_time
                if self.fly == Tear.FLY_LEFT:
                    self.x += self.speed / 3 * game_framework.frame_time
                elif self.fly == Tear.FLY_RIGHT:
                    self.x -= self.speed / 3 * game_framework.frame_time
            elif self.direction == TEAR_DIRECTION_LEFT:
                self.x -= self.speed * game_framework.frame_time
                if self.fly == Tear.FLY_LEFT:
                    self.y -= self.speed / 3 * game_framework.frame_time
                elif self.fly == Tear.FLY_RIGHT:
                    self.y += self.speed / 3 * game_framework.frame_time
            elif self.direction == TEAR_DIRECTION_RIGHT:
                self.x += self.speed * game_framework.frame_time
                if self.fly == Tear.FLY_LEFT:
                    self.y -= self.speed / 3 * game_framework.frame_time
                elif self.fly == Tear.FLY_RIGHT:
                    self.y += self.speed / 3 * game_framework.frame_time
        else:
            self.tear_frame += 1


    def SetXYDir(self, _x, _y, _dir):
        self.x, self.y, self.direction = _x, _y, _dir

    def GetIsEnd(self):
        return self.isPop
    def SetPop(self):
        self.isPopping = True
    def GetX(self):
        return self.x
    def GetY(self):
        return self.y
    def get_bb(self):
        if self.isPopping:
            return 0, 0, 0, 0
        else:
            return self.x - (TEAR_IMAGE_SIZE / 2) + 20, self.y - (TEAR_IMAGE_SIZE / 2) + 20, self.x + (TEAR_IMAGE_SIZE / 2) - 20, self.y + (TEAR_IMAGE_SIZE / 2) - 20
    def GetDamage(self):
        return self.damage

    def GetID(self):
        return self.ID

    def SetFly(self, _fly):
        self.fly = _fly
