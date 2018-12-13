from pico2d import *
import config
import game_world
import ID
import game_framework

MEAT_IMAGE_SIZE = 64
MEAT_LIFE_MAX = 10
MEAT_SLEEP_STANDARD = 5
MEAT_SLEEP_COUNT_MAX = 150

class Meat:
    def __init__(self, _x, _y):
        print("Creating..")
        self.x = _x
        self.y = _y
        self.speed = 75
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
        self.isEnd = False

        self.ID = ID.MEAT

        self.damage = 1

    def draw(self):
        if self.isSleep:
            self.image.clip_draw(self.frame * MEAT_IMAGE_SIZE, 0, MEAT_IMAGE_SIZE, MEAT_IMAGE_SIZE, self.x, self.y)
        else:
            if self.isLeft:
                self.image.clip_draw(self.frame * MEAT_IMAGE_SIZE, MEAT_IMAGE_SIZE, MEAT_IMAGE_SIZE, MEAT_IMAGE_SIZE, self.x, self.y)
            elif False == self.isLeft:
                self.image.clip_draw(self.frame * MEAT_IMAGE_SIZE, MEAT_IMAGE_SIZE * 2, MEAT_IMAGE_SIZE, MEAT_IMAGE_SIZE, self.x, self.y)
        # BB 그리기
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())

    def update_frame(self):
        self._time += game_framework.frame_time
        fps = self.fps if hasattr(self, 'fps') else self._fps
        self.frame = round(self._time * fps) % self._count        


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

    def Hit(self, damage):
        self.life -= damage
        if self.life <= 0:
            self.isEnd = True

    def get_bb(self):
        return self.x - (MEAT_IMAGE_SIZE / 2) + 15, self.y - (MEAT_IMAGE_SIZE / 2) + 15,self.x + (MEAT_IMAGE_SIZE / 2) - 15,self.y + (MEAT_IMAGE_SIZE / 2) - 15

    def GetID(self):
        return self.ID
    def GetIsEnd(self):
        return self.isEnd

    def GetDamage(self):
        return self.damage 