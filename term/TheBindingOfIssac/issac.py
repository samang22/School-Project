from pico2d import *
import tear
import bomb

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


RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP, W_DOWN, A_DOWN, S_DOWN, D_DOWN, SHIFT_DOWN, E_DOWN = range(14) 

ISSAC_ARROW_BASIC = 0


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


    #(SDL_KEYUP, SDLK_w): W_UP,
    #(SDL_KEYUP, SDLK_a): A_UP,
    #(SDL_KEYUP, SDLK_s): S_UP,
    #(SDL_KEYUP, SDLK_d): D_UP,
}

class Issac:
    def __init__(self):
        print("Creating..")
        self.x = 400
        self.y = 300
        self.speed = 2
        self.head_frame = 0
        self.body_frame = 0
        self.image_head = load_image('../resource/Issac.png')
        self.image_body = load_image('../resource/Issac.png')

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

        self.life_num = 5
        self.key_num = 0
        self.arrow_kind = ISSAC_ARROW_BASIC

    def draw(self):
        # 몸
        if self.isMove == False:
            self.image_body.clip_draw(0,                                    self.body_state * ISSAC_IMAGE_SIZE, ISSAC_IMAGE_WIDTH, ISSAC_IMAGE_SIZE, self.x, self.y)
        else:
            self.image_body.clip_draw(self.body_frame * ISSAC_IMAGE_WIDTH,  self.body_state * ISSAC_IMAGE_SIZE, ISSAC_IMAGE_WIDTH, ISSAC_IMAGE_SIZE, self.x, self.y)
        # 머리
        self.image_head.clip_draw(self.head_frame * ISSAC_IMAGE_WIDTH, 5 * ISSAC_IMAGE_SIZE, ISSAC_IMAGE_WIDTH, ISSAC_IMAGE_SIZE, self.x, self.y + 18)

        # 눈물(총알)
        if len(self.tearlist) > 0:
            for t in self.tearlist:
                t.draw()

        # 폭탄
        if len(self.bomblist) > 0:
            for b in self.bomblist:
                b.draw()
    
    def update(self):
        #self.head_frame = (self.frame + 1) % 8
        self.body_frame = (self.body_frame + 1) % 8
        if self.isMove == True:
            if self.isLeft == True and self.isRight == False:
                self.x -= self.speed
            if self.isLeft == False and self.isRight == True:
                self.x += self.speed
            if self.isUp == True and self.isDown == False:
                self.y += self.speed
            if self.isUp == False and self.isDown == True:
                self.y -= self.speed

        # 눈물(총알)
        if len(self.tearlist) > 0:
            for t in self.tearlist:
                t.update()
        # 폭탄
        if len(self.bomblist) > 0:
            for b in self.bomblist:
                b.update()

        self.Check_Tear_Collision_Map()
        self.Delete_Tear()
        self.Shoot_Cooltime_Count()

        if self.isLeft == False and self.isRight == False and self.isUp == False and self.isDown == False:
            self.Move_Stop()
 
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
                self.Shoot_Up()
            elif key_event == A_DOWN: 
                self.Shoot_Left()
            elif key_event == S_DOWN: 
                self.Shoot_Down()
            elif key_event == D_DOWN: 
                self.Shoot_Right()

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
        temp_tear.SetXYDir(self.x, self.y, tear.TEAR_DIRECTION_UP)
        self.tearlist.append(temp_tear)
        self.head_frame = ISSAC_SHOOT_UP
    def Shoot_Down(self):
        temp_tear = tear.Tear()
        temp_tear.SetXYDir(self.x, self.y, tear.TEAR_DIRECTION_DOWN)
        self.tearlist.append(temp_tear)
        self.head_frame = ISSAC_SHOOT_DOWN
    def Shoot_Left(self):
        temp_tear = tear.Tear()
        temp_tear.SetXYDir(self.x, self.y, tear.TEAR_DIRECTION_LEFT)
        self.tearlist.append(temp_tear)
        self.head_frame = ISSAC_SHOOT_LEFT
    def Shoot_Right(self):
        temp_tear = tear.Tear()
        temp_tear.SetXYDir(self.x, self.y, tear.TEAR_DIRECTION_RIGHT)
        self.tearlist.append(temp_tear)
        self.head_frame = ISSAC_SHOOT_RIGHT

    def Check_Tear_Collision_Map(self):
        for t in self.tearlist:
            if t.GetX() < 100 or t.GetX() > 700 or t.GetY() < 100 or t.GetY() > 500:
                t.SetPop()

    def Delete_Tear(self):
        for t in self.tearlist:
            if t.GetIsPop() == True:
                self.tearlist.remove(t)
                print("Delete Tear")
                break

    def Plant_Bomb(self):
        if self.bomb_num > 0:
            tempbomb = bomb.Bomb()
            tempbomb.SetXY(self.x, self.y)
            self.bomblist.append(tempbomb)
            self.bomb_num -= 1

    def Delete_Bomb(self):
        for b in self.bomblist:
            if t.IsEnd() == True:
                self.bomblist.remove(t)
                print("Delete Bomb")
                break
    def GetLifeNum(self):
        return self.life_num
    def GetBombNum(self):
        return self.bomb_num
    def GetKeyNum(self):
        return self.key_num
    def GetArrowKind(self):
        return self.arrow_kind
    def GetX(self):
        return self.x
    def GetY(self):
        return self.y

    def get_bb(self):
        return self.x - (ISSAC_IMAGE_SIZE / 2), self.y - (ISSAC_IMAGE_SIZE / 2),self.x + (ISSAC_IMAGE_SIZE / 2),self.y + (ISSAC_IMAGE_SIZE / 2)


