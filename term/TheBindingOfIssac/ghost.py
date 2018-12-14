from pico2d import *
import config
import game_world
import ID
import game_framework

GHOST_IMAGE_SIZE = 128
GHOST_LIFE_MAX = 40

class Ghost:
    GHOST_UP, GHOST_RIGHT, GHOST_LEFT, GHOST_DOWN = range(4)

    def __init__(self, _x, _y):
        print("Creating..")
        self.x = _x
        self.y = _y
        self.speed = 30
        self.fast_speed = 300
        self.frame = 0
        # 애니메이션이 너무 빨라 추가한 변수
        self.frame_count = 0
        self.image = load_image('../resource/ghost.png')
        self.issac_x = 0
        self.issac_y = 0

        self.direction = Ghost.GHOST_RIGHT

        self.life = GHOST_LIFE_MAX
        self.sleep_count = 0
        self.isFast = False
        self.isEnd = False

        self.ID = ID.GHOST

        self.damage = 2

    def draw(self):
        self.image.clip_draw(self.frame * GHOST_IMAGE_SIZE, self.direction * GHOST_IMAGE_SIZE, GHOST_IMAGE_SIZE, GHOST_IMAGE_SIZE, self.x, self.y)
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
        #self.frame = (self.frame + 1) % 6

        tx, ty = self.issac_x, self.issac_y 
        
        if tx + 50 > self.x and tx - 50 < self.x:
            self.isFast = True
        if ty + 50 > self.y and ty - 50 < self.y:
            self.isFast = True
        else:
            self.isFast = False
        
        if (tx - self.x) > 0:
            if (tx - self.x) ** 2 > (ty - self.y) ** 2:
                self.direction = Ghost.GHOST_RIGHT
            else:
                if (ty - self.y) > 0:
                    self.direction = Ghost.GHOST_UP
                else:
                    self.direction = Ghost.GHOST_DOWN
        else:
            if (tx - self.x) ** 2 > (ty - self.y) ** 2:
                self.direction = Ghost.GHOST_LEFT
            else:
                if (ty - self.y) > 0:
                    self.direction = Ghost.GHOST_UP
                else:
                    self.direction = Ghost.GHOST_DOWN
                

        dx, dy = tx - self.x, ty - self.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        if dist > 0:
            if self.isFast:
                self.x += game_framework.frame_time * self.fast_speed * dx / dist
                self.y += game_framework.frame_time * self.fast_speed * dy / dist
            else:
                self.x += game_framework.frame_time * self.speed * dx / dist
                self.y += game_framework.frame_time * self.speed * dy / dist
                
            if dx < 0 and self.x < tx: self.x = tx
            if dx > 0 and self.x > tx: self.x = tx
            if dy < 0 and self.y < ty: self.y = ty
            if dy > 0 and self.y > ty: self.y = ty

        # 방 밖으로 나가지 않게 하기
        if self.x < 75: self.x = 75
        if self.x > 725: self.x = 725
        if self.y > 425: self.y = 425
        if self.y < 75: self.y = 75


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
        return self.x - (GHOST_IMAGE_SIZE / 2) + 15, self.y - (GHOST_IMAGE_SIZE / 2) + 15,self.x + (GHOST_IMAGE_SIZE / 2) - 15,self.y + (GHOST_IMAGE_SIZE / 2) - 15

    def GetID(self):
        return self.ID
    def GetIsEnd(self):
        return self.isEnd

    def GetDamage(self):
        return self.damage 