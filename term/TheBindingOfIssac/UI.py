from pico2d import *

NUMBER_IMAGE_HEIGHT = 26

class UI:
    def __init__(self):
        print("Creating UI")
        self.x = 400
        self.y = 300
        self.image = load_image('../resource/UI.png')
        self.bomb_num_image = load_image('../resource/Counter.png')
        self.life_num_image = load_image('../resource/Counter.png')
        self.key_num_image = load_image('../resource/Counter.png')

        self.bomb_num_x = 380
        self.bomb_num_y = 550
        self.key_num_x = 530
        self.key_num_y = 550
        self.life_num_x = 700
        self.life_num_y = 550



        self.bomb_num = 0
        self.life_num = 0
        self.key_num = 0
        self.arrow_kind = 0

    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, self.x, self.y)
        self.bomb_num_image.clip_draw(0,    NUMBER_IMAGE_HEIGHT * (9 - self.bomb_num),    45, 26, self.bomb_num_x,  self.bomb_num_y)
        self.life_num_image.clip_draw(0,    NUMBER_IMAGE_HEIGHT * (9 - self.life_num),    45, 26, self.life_num_x,  self.life_num_y)
        self.key_num_image.clip_draw(0,     NUMBER_IMAGE_HEIGHT * (9 - self.key_num),     45, 26, self.key_num_x,   self.key_num_y)
        

    def SetBombNum(self, _Num):
        self.bomb_num = _Num
    def SetLifeNum(self, _Num):
        self.life_num = _Num
    def SetKeyNum(self, _Num):
        self.key_num = _Num
    def SetArrowKind(self, _Kind):
        self.arrow_kind = _Kind

    def SetData(self, _Bomb, _Life, _Key, _Arrow):
        self.SetBombNum(_Bomb)
        self.SetLifeNum(_Life)
        self.SetKeyNum(_Key)
        self.SetArrowKind(_Arrow)


