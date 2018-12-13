from pico2d import *
import config
import game_world
import ID
import game_framework

FLY_IMAGE_SIZE = 64

class Fly:
    def __init__(self, _x, _y):
        print("Creating..")
        self.life = 2
        self.x = _x
        self.y = _y
        self.speed = 85
        self.frame = 0
        # 애니메이션이 너무 빨라 추가한 변수
        self.frame_count = 0
        self.image = load_image('../resource/Fly1.png')
        self.IsDead = False
        self.issac_x = 0
        self.issac_y = 0
        self.ID = ID.FLY
        self.isEnd = False

        self.damage = 1


    def draw(self):
        if self.IsDead:
            pass
        else:
            self.image.clip_draw(self.frame * FLY_IMAGE_SIZE, FLY_IMAGE_SIZE, FLY_IMAGE_SIZE, FLY_IMAGE_SIZE, self.x, self.y)
            #self.image.clip_draw(0, 0, FLY_IMAGE_SIZE, FLY_IMAGE_SIZE, self.x, self.y)
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())

    
    def update(self):
        self.frame_count += 1
        if self.frame_count % 2 == 0:
            self.frame = (self.frame + 1) % 5
        

        tx, ty = self.issac_x, self.issac_y 

        dx, dy = tx - self.x, ty - self.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        if dist > 0:
            self.x += game_framework.frame_time * self.speed * dx / dist
            self.y += game_framework.frame_time * self.speed * dy / dist
        
            if dx < 0 and self.x < tx: self.x = tx
            if dx > 0 and self.x > tx: self.x = tx
            if dy < 0 and self.y < ty: self.y = ty
            if dy > 0 and self.y > ty: self.y = ty

    def SetPos(self, _x, _y):
        self.x = _x
        self.y = _y

    def SetIssacPos(self, _x, _y):
        self.issac_x = _x
        self.issac_y = _y
    def get_bb(self):
        return self.x - (FLY_IMAGE_SIZE / 2) + 15, self.y - (FLY_IMAGE_SIZE / 2) + 15, self.x + (FLY_IMAGE_SIZE / 2) - 15, self.y + (FLY_IMAGE_SIZE / 2) - 15

    def GetID(self):
        return self.ID

    def Hit(self, damage):
        self.life -= damage
        if self.life <= 0:
            self.isEnd = True
    def GetIsEnd(self):
        return self.isEnd
    def GetDamage(self):
        return self.damage 
