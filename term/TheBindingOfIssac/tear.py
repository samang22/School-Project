from pico2d import *

TEAR_DIRECTION_UP = 1
TEAR_DIRECTION_DOWN = 2
TEAR_DIRECTION_LEFT = 3
TEAR_DIRECTION_RIGHT = 4

TEAR_SIZE = 64



class Tear:
    #tear_image = None
    def __init__(self):
        print("Creating Tear")
        self.x = 0
        self.y = 0
        self.speed = 4
        self.tear_frame = 0
        self.isPopping = False
        self.isPop = False
        self.direction = 0
        self.tear_image = load_image('../resource/Tear.png')
    def draw(self):
        #터지기 전
        if self.isPopping == False:
            self.tear_image.clip_draw(0                             , 0, TEAR_SIZE, TEAR_SIZE, self.x, self.y)
        # 터지는 중
        elif self.isPopping == True:
            self.tear_image.clip_draw(self.tear_frame * TEAR_SIZE   , 0, TEAR_SIZE, TEAR_SIZE, self.x, self.y)

    def update(self):
        if self.tear_frame > 10:
                self.isPop = True
        if self.isPopping == False:
            if self.direction == TEAR_DIRECTION_UP:
                self.y += self.speed
            elif self.direction == TEAR_DIRECTION_DOWN:
                self.y -= self.speed
            elif self.direction == TEAR_DIRECTION_LEFT:
                self.x -= self.speed
            elif self.direction == TEAR_DIRECTION_RIGHT:
                self.x += self.speed
        else:
            self.tear_frame += 1


    def SetXYDir(self, _x, _y, _dir):
        self.x, self.y, self.direction = _x, _y, _dir

    def GetIsPop(self):
        return self.isPop
    def SetPop(self):
        self.isPopping = True
    def GetX(self):
        return self.x
    def GetY(self):
        return self.y