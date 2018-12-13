from pico2d import *
import ID

NUMBER_IMAGE_HEIGHT = 26

class UI:
    TEAR = 3
    TRIPLE = 4
    RAZOR = 5    

    def __init__(self):
        print("Creating UI")
        self.x = 400
        self.y = 300
        self.image = load_image('../resource/UI.png')
        self.bomb_num_image = load_image('../resource/Counter.png')
        self.life_num_image = load_image('../resource/Counter.png')
        self.key_num_image = load_image('../resource/Counter.png')

        self.tear_image = load_image('../resource/Tear_Item.png')
        self.triple_image = load_image('../resource/Triple_Item.png')
        self.razor_image = load_image('../resource/Razor_Item.png')

        self.bomb_num_x = 380
        self.bomb_num_y = 550
        self.key_num_x = 530
        self.key_num_y = 550
        self.life_num_x = 700
        self.life_num_y = 550

        self.weapon_x  = 205
        self.weapon_y  = 550


        self.bomb_num = 0
        self.life_num = 0
        self.key_num = 0
        self.weapon_kind = UI.TEAR

        self.ID = ID.UI

    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, self.x, self.y)
        self.bomb_num_image.clip_draw(0,    NUMBER_IMAGE_HEIGHT * (9 - self.bomb_num),    45, 26, self.bomb_num_x,  self.bomb_num_y)
        self.life_num_image.clip_draw(0,    NUMBER_IMAGE_HEIGHT * (9 - self.life_num),    45, 26, self.life_num_x,  self.life_num_y)
        self.key_num_image.clip_draw(0,     NUMBER_IMAGE_HEIGHT * (9 - self.key_num),     45, 26, self.key_num_x,   self.key_num_y)
        if self.weapon_kind == UI.TEAR:
            self.tear_image.clip_draw(0, 0, 32, 32, self.weapon_x, self.weapon_y)
        elif self.weapon_kind == UI.TRIPLE:
            self.triple_image.clip_draw(0, 0, 32, 32, self.weapon_x, self.weapon_y)
        elif self.weapon_kind == UI.RAZOR:
            self.razor_image.clip_draw(0, 0, 32, 32, self.weapon_x, self.weapon_y)
        
    def update(self):
        pass

    def SetBombNum(self, _Num):
        self.bomb_num = _Num
    def SetLifeNum(self, _Num):
        self.life_num = _Num
    def SetKeyNum(self, _Num):
        self.key_num = _Num
    def SetWeaponKind(self, _Kind):
        self.weapon_kind = _Kind

    def SetData(self, _Bomb, _Life, _Key, _Weapon):
        self.SetBombNum(_Bomb)
        self.SetLifeNum(_Life)
        self.SetKeyNum(_Key)
        self.SetWeaponKind(_Weapon)
    def GetID(self):
        return self.ID

