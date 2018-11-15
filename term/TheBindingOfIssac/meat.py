from pico2d import *

MEAT_IMAGE_SIZE = 64
MEAT_LIFE_MAX = 10
MEAT_SLEEP_STANDARD = 5
MEAT_SLEEP_COUNT_MAX = 150

class Meat:
    def __init__(self):
        print("Creating..")
        self.x = 400
        self.y = 300
        self.speed = 1.5
        self.frame = 0
        # 애니메이션이 너무 빨라 추가한 변수
        self.frame_count = 0
        self.image = load_image('../resource/Meat.png')
        self.IsDead = False
        self.issac_x = 0
        self.issac_y = 0

        self.isSleep = False
        self.isLeft = False

        self.life = MEAT_LIFE_MAX
        self.sleep_count = 0

    def draw(self):
        if self.isSleep:
            self.image.clip_draw(self.frame * MEAT_IMAGE_SIZE, 0, MEAT_IMAGE_SIZE, MEAT_IMAGE_SIZE, self.x, self.y)
        else:
            if self.isLeft:
                self.image.clip_draw(self.frame * MEAT_IMAGE_SIZE, MEAT_IMAGE_SIZE, MEAT_IMAGE_SIZE, MEAT_IMAGE_SIZE, self.x, self.y)
            elif False == self.isLeft:
                self.image.clip_draw(self.frame * MEAT_IMAGE_SIZE, MEAT_IMAGE_SIZE * 2, MEAT_IMAGE_SIZE, MEAT_IMAGE_SIZE, self.x, self.y)

    def update(self):
        self.frame_count += 1
        if self.frame_count % 2 == 0:
            self.frame = (self.frame + 1) % 6
        if self.life <= MEAT_SLEEP_STANDARD:
            self.isSleep = True
        #self.frame = (self.frame + 1) % 6

        tx, ty = self.issac_x, self.issac_y 
        if tx > self.x:
            self.isLeft = False
        else:
            self.isLeft = True

        if self.isSleep:
            self.sleep_count += 1
            if self.sleep_count > MEAT_SLEEP_COUNT_MAX:
                self.sleep_count = 0
                self.isSleep = False
                self.life = MEAT_LIFE_MAX
            return

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

    def Hit(self):
        self.life -= 1
