from pico2d import *
import tear
import razor
import bomb
import config
import game_world
import ID
import game_framework

ISSAC_IMAGE_SIZE = 64
ISSAC_IMAGE_WIDTH = 57
ISSAC_IMAGE_HEAD_HEIGHT = 51

ISSAC_IMAGE_STOP = 4
ISSAC_IMAGE_DOWN = 3
ISSAC_IMAGE_RIGHT = 2
ISSAC_IMAGE_LEFT = 1

ISSAC_DIRECTION_UP = 4
ISSAC_DIRECTION_DOWN = 3
ISSAC_DIRECTION_RIGHT = 2
ISSAC_DIRECTION_LEFT = 1
ISSAC_DIRECTION_UP_RIGHT = 5
ISSAC_DIRECTION_UP_LEFT = 6
ISSAC_DIRECTION_DOWN_RIGHT = 7
ISSAC_DIRECTION_DOWN_LEFT = 8

ISSAC_TEAR_SHOOT_COOLTIME = 5

ISSAC_SHOOT_DOWN = 0
ISSAC_SHOOT_RIGHT = 2
ISSAC_SHOOT_UP = 4
ISSAC_SHOOT_LEFT = 6


RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP, W_DOWN, A_DOWN, S_DOWN, D_DOWN, SHIFT_DOWN, E_DOWN, SPACE_DOWN, SPACE_UP = range(16) 


ISSAC_HIT_COUNT = 20

ITEM_IMAGE_SIZE = 32


key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,

    (SDL_KEYDOWN, SDLK_w): W_DOWN,
    (SDL_KEYDOWN, SDLK_a): A_DOWN,
    (SDL_KEYDOWN, SDLK_s): S_DOWN,
    (SDL_KEYDOWN, SDLK_d): D_DOWN,

    (SDL_KEYDOWN, SDLK_LSHIFT): SHIFT_DOWN,
    (SDL_KEYDOWN, SDLK_e): E_DOWN,

    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN, 
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP 

    #(SDL_KEYUP, SDLK_w): W_UP,
    #(SDL_KEYUP, SDLK_a): A_UP,
    #(SDL_KEYUP, SDLK_s): S_UP,
    #(SDL_KEYUP, SDLK_d): D_UP,
}

class Issac:
    HEART = 0
    BOMB = 1
    KEY = 2
    TEAR = 3
    TRIPLE = 4
    RAZOR = 5    


    def __init__(self):
        print("Creating..")
        self.x = 400
        self.y = 300
        self.speed = 150
        self.head_frame = 0
        self.body_frame = 0
        self.tear_image_head = load_image('../resource/Issac.png')
        self.triple_image_head = load_image('../resource/Issac_Triple.png')
        self.razor_image_head = load_image('../resource/Issac_Razor.png')
        self.image_body = load_image('../resource/Issac.png')

        self.hit_image_head = load_image('../resource/issac_hit.png')
        self.hit_image_body = load_image('../resource/issac_hit.png')

        self.tear_image = load_image('../resource/Tear_Item.png')
        self.triple_image = load_image('../resource/Triple_Item.png')
        self.razor_image = load_image('../resource/Razor_Item.png')


        self.head_state = 5
        self.body_state = ISSAC_IMAGE_DOWN
        
        self.direction = ISSAC_DIRECTION_DOWN
        self.isMove = False

        self.isLeft = False
        self.isRight = False
        self.isUp = False
        self.isDown = False

        self.tearlist = []
        self.tear_shoot_cooltime_count = 0 
        self.isCoolTime = False
        self.eye_flicker = 0

        self.bomb_num = 5
        self.bomblist = []

        self.life = 9
        self.key_num = 0
        self.weapon_kind = Issac.RAZOR

        self.ID = ID.ISSAC

        self.isHit = False
        self.hit_count = ISSAC_HIT_COUNT

        self.isGetItem = False
        self.get_item_frame = 0

        self.isSpaceDown = False
        self.slow = False

    def draw(self):
        if self.isGetItem:
            self.image_body.clip_draw(self.get_item_frame * ISSAC_IMAGE_WIDTH, 0, ISSAC_IMAGE_WIDTH, ISSAC_IMAGE_SIZE, self.x , self.y + 16)
            if self.weapon_kind == Issac.TEAR:
                self.tear_image.clip_draw(0, 0, ITEM_IMAGE_SIZE, ITEM_IMAGE_SIZE, self.x , self.y + 40)
            elif self.weapon_kind == Issac.TRIPLE:
                self.triple_image.clip_draw(0, 0, ITEM_IMAGE_SIZE, ITEM_IMAGE_SIZE, self.x, self.y + 40)
            elif self.weapon_kind == Issac.RAZOR:
                self.razor_image.clip_draw(0, 0, ITEM_IMAGE_SIZE, ITEM_IMAGE_SIZE, self.x, self.y + 40)

        else:


            if not self.isHit: 
                # 몸
                if self.isMove == False:
                    self.image_body.clip_draw(0,                                    self.body_state * ISSAC_IMAGE_SIZE, ISSAC_IMAGE_WIDTH, ISSAC_IMAGE_SIZE, self.x, self.y)
                else:
                    self.image_body.clip_draw(self.body_frame * ISSAC_IMAGE_WIDTH,  self.body_state * ISSAC_IMAGE_SIZE, ISSAC_IMAGE_WIDTH, ISSAC_IMAGE_SIZE, self.x, self.y)
                # 머리
                if self.weapon_kind == Issac.TEAR:
                    self.tear_image_head.clip_draw(self.head_frame * ISSAC_IMAGE_WIDTH, 5 * ISSAC_IMAGE_SIZE, ISSAC_IMAGE_WIDTH, ISSAC_IMAGE_SIZE, self.x, self.y + 18)
                elif self.weapon_kind == Issac.TRIPLE:
                    self.triple_image_head.clip_draw(self.head_frame * ISSAC_IMAGE_WIDTH, 5 * ISSAC_IMAGE_SIZE, ISSAC_IMAGE_WIDTH, ISSAC_IMAGE_SIZE, self.x, self.y + 18)
                if self.weapon_kind == Issac.RAZOR:
                    self.razor_image_head.clip_draw(self.head_frame * ISSAC_IMAGE_WIDTH, 5 * ISSAC_IMAGE_SIZE, ISSAC_IMAGE_WIDTH, ISSAC_IMAGE_SIZE, self.x, self.y + 18)
            else:
                # 몸
                if self.isMove == False:
                    self.hit_image_body.clip_draw(0,                                    self.body_state * ISSAC_IMAGE_SIZE, ISSAC_IMAGE_WIDTH, ISSAC_IMAGE_SIZE, self.x, self.y)
                else:
                    self.hit_image_body.clip_draw(self.body_frame * ISSAC_IMAGE_WIDTH,  self.body_state * ISSAC_IMAGE_SIZE, ISSAC_IMAGE_WIDTH, ISSAC_IMAGE_SIZE, self.x, self.y)
                # 머리
                self.hit_image_head.clip_draw(self.head_frame * ISSAC_IMAGE_WIDTH, 5 * ISSAC_IMAGE_SIZE, ISSAC_IMAGE_WIDTH, ISSAC_IMAGE_SIZE, self.x, self.y + 18)




        # 눈물(총알)
        if len(self.tearlist) > 0:
            for t in self.tearlist:
                t.draw()

        # 폭탄
        if len(self.bomblist) > 0:
            for b in self.bomblist:
                b.draw()
        # BB 그리기
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())
    
    def update(self):
        # 아이템 획득 모션
        if self.isGetItem:
            if self.slow:
                self.get_item_frame += 1
                self.slow = False
            else:
                self.slow = True
            if self.get_item_frame > 7:
                self.get_item_frame = 0
                self.isGetItem = False


        else:
            #self.head_frame = (self.frame + 1) % 8
            self.body_frame = (self.body_frame + 1) % 8
        if self.isMove == True:
            if self.isLeft == True and self.isRight == False:
                self.x -= self.speed * game_framework.frame_time
                if self.x < 75: self.x = 75
            if self.isLeft == False and self.isRight == True:
                self.x += self.speed * game_framework.frame_time
                if self.x > 725: self.x = 725
            if self.isUp == True and self.isDown == False:
                self.y += self.speed * game_framework.frame_time
                if self.y > 425: self.y = 425
            if self.isUp == False and self.isDown == True:
                self.y -= self.speed * game_framework.frame_time
                if self.y < 75: self.y = 75
        
        ## 눈물(총알)
        #if len(self.tearlist) > 0:
        #    for t in self.tearlist:
        #        t.update()
        ## 폭탄
        #if len(self.bomblist) > 0:
        #    for b in self.bomblist:
        #        b.update()

        self.Check_Tear_Collision_Map()
        self.Delete_Tear()
        self.Delete_Bomb()
        self.Shoot_Cooltime_Count()
        if self.isLeft == False and self.isRight == False and self.isUp == False and self.isDown == False:
            self.Move_Stop()
 

        # 피격
        if self.isHit:
            self.hit_count -= 1
            if self.hit_count == 0:
                self.hit_count = ISSAC_HIT_COUNT
                self.isHit = False

    def handle_event(self, e):
        if (e.type, e.key) in key_event_table:
            key_event = key_event_table[(e.type, e.key)]
            if key_event == RIGHT_DOWN:
                self.Move_Right()
            elif key_event == LEFT_DOWN: 
                self.Move_Left()
            elif key_event == UP_DOWN:   
                self.Move_Up()
            elif key_event == DOWN_DOWN:   
                self.Move_Down()
            
            elif key_event == W_DOWN: 
                if self.weapon_kind == Issac.TEAR or self.weapon_kind == Issac.TRIPLE: 
                    self.Shoot_Up()
                elif self.weapon_kind == Issac.RAZOR:
                    self.Shoot_Razor_Up()
            elif key_event == A_DOWN: 
                if self.weapon_kind == Issac.TEAR or self.weapon_kind == Issac.TRIPLE: 
                    self.Shoot_Left()
                elif self.weapon_kind == Issac.RAZOR:
                    self.Shoot_Razor_Left()
            elif key_event == S_DOWN: 
                if self.weapon_kind == Issac.TEAR or self.weapon_kind == Issac.TRIPLE: 
                    self.Shoot_Down()
                elif self.weapon_kind == Issac.RAZOR:
                    self.Shoot_Razor_Down()
            elif key_event == D_DOWN: 
                if self.weapon_kind == Issac.TEAR or self.weapon_kind == Issac.TRIPLE: 
                    self.Shoot_Right()
                elif self.weapon_kind == Issac.RAZOR:
                    self.Shoot_Razor_Right()

            elif key_event == RIGHT_UP:  
                self.Move_Right_Off()
            elif key_event == LEFT_UP:   
                self.Move_Left_Off()
            elif key_event == UP_UP:     
                self.Move_Up_Off()
            elif key_event == DOWN_UP:   
                self.Move_Down_Off()
            elif key_event == E_DOWN or key_event == SHIFT_DOWN:
                self.Plant_Bomb()
            elif key_event == SPACE_DOWN:
                self.isSpaceDown = True
            elif key_event == SPACE_UP:
                self.isSpaceDown = False
        else:
            a = e

    def Move_Up(self):
        self.body_state = ISSAC_IMAGE_DOWN
        self.direction = ISSAC_DIRECTION_UP
        self.isMove = True
        self.isUp = True
        self.isDown = False
    def Move_Up_Off(self):
        self.isUp = False

    def Move_Down(self):
        self.body_state = ISSAC_IMAGE_DOWN
        self.direction = ISSAC_DIRECTION_DOWN
        self.isMove = True
        self.isDown = True
        self.isUp = False
    def Move_Down_Off(self):
        self.isDown = False
        #self.isMove = False

    def Move_Left(self):
        self.body_state = ISSAC_IMAGE_LEFT
        self.direction = ISSAC_DIRECTION_LEFT
        self.isMove = True
        self.isLeft = True
        self.isRight = False
    def Move_Left_Off(self):
        self.isLeft = False
        #self.isMove = False

    def Move_Right(self):
        self.body_state = ISSAC_IMAGE_RIGHT
        self.direction = ISSAC_DIRECTION_RIGHT
        self.isMove = True
        self.isLeft = False
        self.isRight = True
    def Move_Right_Off(self):
        self.isRight = False
        #self.isMove = False

    def Move_Stop(self):
        self.isMove = False
        self.isDown = False
        self.isUp = False
        self.isLeft = False
        self.isRight = False


    def Shoot(self, _Dir):
        if self.weapon_kind == Issac.TEAR or self.weapon_kind == Issac.TRIPLE: 
            if self.isCoolTime == False:
                if _Dir == tear.TEAR_DIRECTION_UP:
                    self.Shoot_Up();
                elif _Dir == tear.TEAR_DIRECTION_DOWN:
                    self.Shoot_Down();
                elif _Dir == tear.TEAR_DIRECTION_LEFT:
                    self.Shoot_Left();
                elif _Dir == tear.TEAR_DIRECTION_RIGHT:
                    self.Shoot_Right();
                self.isCoolTime = True
        elif self.weapon_kind == Issac.RAZOR:
                if _Dir == tear.TEAR_DIRECTION_UP:
                    self.Shoot_Razor_Up()
                elif _Dir == tear.TEAR_DIRECTION_DOWN:
                    self.Shoot_Razor_Down()
                elif _Dir == tear.TEAR_DIRECTION_LEFT:
                    self.Shoot_Razor_Left()
                elif _Dir == tear.TEAR_DIRECTION_RIGHT:
                    self.Shoot_Razor_Right()


    def Shoot_Cooltime_Count(self):
        if self.isCoolTime == True:
            if self.eye_flicker == 0:
                self.head_frame += 1
                self.eye_flicker += 1
            elif self.eye_flicker == 1:
                self.head_frame -= 1
                self.eye_flicker += 1
            self.tear_shoot_cooltime_count += 1
        if self.tear_shoot_cooltime_count >= ISSAC_TEAR_SHOOT_COOLTIME:
            self.tear_shoot_cooltime_count = 0
            self.isCoolTime = False
            self.eye_flicker = 0


    def Shoot_Up(self):
        temp_tear = tear.Tear()
        temp_tear.SetXYDir(self.x, self.y + 10, tear.TEAR_DIRECTION_UP)
        if self.weapon_kind == Issac.TRIPLE:
            temp_tear1 = tear.Tear()
            temp_tear1.SetXYDir(self.x, self.y + 10, tear.TEAR_DIRECTION_UP)
            temp_tear1.SetFly(1)
            temp_tear2 = tear.Tear()
            temp_tear2.SetXYDir(self.x, self.y + 10, tear.TEAR_DIRECTION_UP)
            temp_tear2.SetFly(2)
            self.tearlist.append(temp_tear1)
            self.tearlist.append(temp_tear2)
            game_world.add_object(temp_tear1, game_world.LAYER_ISSAC)
            game_world.add_object(temp_tear2, game_world.LAYER_ISSAC)
        self.tearlist.append(temp_tear)
        game_world.add_object(temp_tear, game_world.LAYER_ISSAC)
        self.head_frame = ISSAC_SHOOT_UP
    def Shoot_Down(self):
        temp_tear = tear.Tear()
        temp_tear.SetXYDir(self.x, self.y + 10, tear.TEAR_DIRECTION_DOWN)
        if self.weapon_kind == Issac.TRIPLE:
            temp_tear1 = tear.Tear()
            temp_tear1.SetXYDir(self.x, self.y + 10, tear.TEAR_DIRECTION_DOWN)
            temp_tear1.SetFly(1)
            temp_tear2 = tear.Tear()
            temp_tear2.SetXYDir(self.x, self.y + 10, tear.TEAR_DIRECTION_DOWN)
            temp_tear2.SetFly(2)
            self.tearlist.append(temp_tear1)
            self.tearlist.append(temp_tear2)
            game_world.add_object(temp_tear1, game_world.LAYER_ISSAC)
            game_world.add_object(temp_tear2, game_world.LAYER_ISSAC)
        self.tearlist.append(temp_tear)
        game_world.add_object(temp_tear, game_world.LAYER_ISSAC)
        self.head_frame = ISSAC_SHOOT_DOWN
    def Shoot_Left(self):
        temp_tear = tear.Tear()
        temp_tear.SetXYDir(self.x, self.y + 10 + 10, tear.TEAR_DIRECTION_LEFT)
        if self.weapon_kind == Issac.TRIPLE:
            temp_tear1 = tear.Tear()
            temp_tear1.SetXYDir(self.x, self.y + 10, tear.TEAR_DIRECTION_LEFT)
            temp_tear1.SetFly(1)
            temp_tear2 = tear.Tear()
            temp_tear2.SetXYDir(self.x, self.y + 10, tear.TEAR_DIRECTION_LEFT)
            temp_tear2.SetFly(2)
            self.tearlist.append(temp_tear1)
            self.tearlist.append(temp_tear2)
            game_world.add_object(temp_tear1, game_world.LAYER_ISSAC)
            game_world.add_object(temp_tear2, game_world.LAYER_ISSAC)
        self.tearlist.append(temp_tear)
        game_world.add_object(temp_tear, game_world.LAYER_ISSAC)
        self.head_frame = ISSAC_SHOOT_LEFT
    def Shoot_Right(self):
        temp_tear = tear.Tear()
        temp_tear.SetXYDir(self.x, self.y + 10, tear.TEAR_DIRECTION_RIGHT)
        if self.weapon_kind == Issac.TRIPLE:
            temp_tear1 = tear.Tear()
            temp_tear1.SetXYDir(self.x, self.y + 10, tear.TEAR_DIRECTION_RIGHT)
            temp_tear1.SetFly(1)
            temp_tear2 = tear.Tear()
            temp_tear2.SetXYDir(self.x, self.y + 10, tear.TEAR_DIRECTION_RIGHT)
            temp_tear2.SetFly(2)
            self.tearlist.append(temp_tear1)
            self.tearlist.append(temp_tear2)
            game_world.add_object(temp_tear1, game_world.LAYER_ISSAC)
            game_world.add_object(temp_tear2, game_world.LAYER_ISSAC)
        self.tearlist.append(temp_tear)
        game_world.add_object(temp_tear, game_world.LAYER_ISSAC)
        self.head_frame = ISSAC_SHOOT_RIGHT

    def Shoot_Razor_Up(self):
        temp_razor = razor.Razor(razor.Razor.RAZOR_DIRECTION_UP, self.x, self.y + 10)
        game_world.add_object(temp_razor, game_world.LAYER_ISSAC)
        self.head_frame = ISSAC_SHOOT_UP
    def Shoot_Razor_Down(self):
        temp_razor = razor.Razor(razor.Razor.RAZOR_DIRECTION_DOWN, self.x, self.y + 10)
        game_world.add_object(temp_razor, game_world.LAYER_ISSAC)
        self.head_frame = ISSAC_SHOOT_DOWN
    def Shoot_Razor_Left(self):
        temp_razor = razor.Razor(razor.Razor.RAZOR_DIRECTION_LEFT, self.x, self.y + 10)
        game_world.add_object(temp_razor, game_world.LAYER_ISSAC)
        self.head_frame = ISSAC_SHOOT_LEFT
    def Shoot_Razor_Right(self):
        temp_razor = razor.Razor(razor.Razor.RAZOR_DIRECTION_RIGHT, self.x, self.y + 10)
        game_world.add_object(temp_razor, game_world.LAYER_ISSAC)
        self.head_frame = ISSAC_SHOOT_RIGHT

    def Check_Tear_Collision_Map(self):
        for t in self.tearlist:
            if t.GetX() < 75 or t.GetX() > 725 or t.GetY() < 75 or t.GetY() > 425:
                t.SetPop()

    def Delete_Tear(self):
        for t in self.tearlist:
            if t.GetIsEnd() == True:
                self.tearlist.remove(t)
                print("Delete Tear")
                break

    def Plant_Bomb(self):
        if self.bomb_num > 0:
            tempbomb = bomb.Bomb()
            tempbomb.SetXY(self.x, self.y)
            self.bomblist.append(tempbomb)
            game_world.add_object(tempbomb, game_world.LAYER_ISSAC)
            self.bomb_num -= 1

    def Delete_Bomb(self):
        for b in self.bomblist:
            if b.GetIsEnd() == True:
                self.bomblist.remove(b)
                print("Delete Bomb")
                break

    
    def Hit(self, _damage):
        if self.hit_count != ISSAC_HIT_COUNT:
            return
        self.life -= _damage
        if self.life < 0:
            self.life = 0
        self.isHit = True
        print("issac hit")

    def GetLifeNum(self):
        return self.life
    def GetBombNum(self):
        return self.bomb_num
    def GetKeyNum(self):
        return self.key_num
    #def GetArrowKind(self):
    #    return self.weapon_kind
    def GetX(self):
        return self.x
    def GetY(self):
        return self.y

    def get_bb(self):
        return self.x - (ISSAC_IMAGE_SIZE / 2) + 5, self.y - (ISSAC_IMAGE_SIZE / 2) + 15, self.x + (ISSAC_IMAGE_SIZE / 2) - 5, self.y + (ISSAC_IMAGE_SIZE / 2) + 15

    def GetID(self):
        return self.ID

    def SetPos(self, _x, _y):
        self.x = _x
        self.y = _y

    def GetConsumableItem(self, _kind):
        if _kind == Issac.HEART:
            self.life += 2
            if self.life > 9:
                self.life = 9
        elif _kind == Issac.KEY:
            self.key_num += 1
            if self.key_num > 9:
                self.key_num = 9
        elif _kind == Issac.BOMB:
            self.bomb_num += 3
            if self.bomb_num > 9:
                self.bomb_num = 9

    def SetWeaponItem(self, _kind):
        if _kind == Issac.TEAR:
            self.weapon_kind = Issac.TEAR
        elif _kind == Issac.TRIPLE:
            self.weapon_kind = Issac.TRIPLE
        elif _kind == Issac.RAZOR:
            self.weapon_kind = Issac.RAZOR

        self.isGetItem = True
    def GetIsSpaceDown(self):
        return self.isSpaceDown
    def GetWeaponKind(self):
        return self.weapon_kind
    def UseKey(self):
        if self.key_num > 0:
            self.key_num -= 1