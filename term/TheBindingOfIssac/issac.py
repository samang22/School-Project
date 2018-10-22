from pico2d import *
import tear

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

        if len(self.tearlist) > 0:
            for t in self.tearlist:
                t.update()
        
        self.Check_Tear_Collision_Map()
        self.Delete_Tear()
        self.Cooltime_Count()


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

    def Move_Left(self):
        self.body_state = ISSAC_IMAGE_LEFT
        self.direction = ISSAC_DIRECTION_LEFT
        self.isMove = True
        self.isLeft = True
        self.isRight = False
    def Move_Left_Off(self):
        self.isLeft = False

    def Move_Right(self):
        self.body_state = ISSAC_IMAGE_RIGHT
        self.direction = ISSAC_DIRECTION_RIGHT
        self.isMove = True
        self.isLeft = False
        self.isRight = True
    def Move_Right_Off(self):
        self.isRight = False

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

    def Cooltime_Count(self):
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