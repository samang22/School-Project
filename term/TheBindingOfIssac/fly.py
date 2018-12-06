from pico2d import *

FLY_IMAGE_SIZE = 64

class Fly:
    def __init__(self):
        print("Creating..")
        self.x = 400
        self.y = 300
        self.speed = 2
        self.frame = 0
        # 애니메이션이 너무 빨라 추가한 변수
        self.frame_count = 0
        self.image = load_image('../resource/Fly1.png')
        self.IsDead = False
        self.issac_x = 0
        self.issac_y = 0

    def draw(self):
        if self.IsDead:
            pass
        else:
            self.image.clip_draw(self.frame * FLY_IMAGE_SIZE, FLY_IMAGE_SIZE, FLY_IMAGE_SIZE, FLY_IMAGE_SIZE, self.x, self.y)
            #self.image.clip_draw(0, 0, FLY_IMAGE_SIZE, FLY_IMAGE_SIZE, self.x, self.y)

    
    def update(self):
        self.frame_count += 1
        if self.frame_count % 2 == 0:
            self.frame = (self.frame + 1) % 5
        

        tx, ty = self.issac_x, self.issac_y 

        dx, dy = tx - self.x, ty - self.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        if dist > 0:
            self.x += self.speed * dx / dist
            self.y += self.speed * dy / dist
        
            if dx < 0 and self.x < tx: self.x = tx
            if dx > 0 and self.x > tx: self.x = tx
            if dy < 0 and self.y < ty: self.y = ty
            if dy > 0 and self.y > ty: self.y = ty

    def SetIssacPos(self, _x, _y):
        self.issac_x = _x
        self.issac_y = _y
    def get_bb(self):
        return self.x - (FLY_IMAGE_SIZE / 2), self.y - (FLY_IMAGE_SIZE / 2),self.x + (FLY_IMAGE_SIZE / 2),self.y + (FLY_IMAGE_SIZE / 2)
