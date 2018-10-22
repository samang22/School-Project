from pico2d import *


BOMB_SIZE = 64
BOMB_EXPLOSION_SIZE = 192



class Bomb:
    def __init__(self):
        print("Creating Bomb")
        self.x = 0
        self.y = 0
        self.bomb_frame = 0
        self.bomb_explosion_frame = 0
        self.bomb_image = load_image('../resource/Bomb.png')
        self.bomb_explosion_image = load_image('../resource/BombExplosion.png')
        self.isExplode = False
        self.isEnd = False
        self.count = 0
    def draw(self):
        #터지기 전
        if self.isExplode == False:
            self.bomb_image.clip_draw(self.bomb_frame * BOMB_SIZE, 0, BOMB_SIZE, BOMB_SIZE, self.x, self.y)
        # 터지는 중
        elif self.isExplode == True:
            self.bomb_explosion_image.clip_draw(self.bomb_explosion_frame * BOMB_EXPLOSION_SIZE, 0, BOMB_EXPLOSION_SIZE, BOMB_EXPLOSION_SIZE, self.x, self.y)

    def update(self):
        self.count +=1
        if self.bomb_frame >= 12:
            self.isExplode = True
        if self.bomb_explosion_frame >= 11:
            self.isEnd = True
        if self.isExplode == False:
            if self.count % 2 == 0:
                self.bomb_frame += 1
        else:
            if self.count % 2 == 0:
                self.bomb_explosion_frame += 1


    def SetXY(self, _x, _y,):
        self.x, self.y = _x, _y

    def GetIsEnd(self):
        return self.isEnd
    def GetX(self):
        return self.x
    def GetY(self):
        return self.y