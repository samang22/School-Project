from pico2d import *

class Tear:
    tear_image = None
    def __init__(self):
        print("Creating Tear")
        self.x = 0
        self.y = 0
        self.speed = 2
        self.tear_frame = 0
        self.image_tear = load_image('../resource/Tear.png')

    def draw(self):
        #터지기 전
        if self.isMove == False:
            self.tear_image.clip_draw(0, self.body_state * 32, 32, 32, self.x, self.y)
        else:
            self.image_body.clip_draw(self.body_frame * 32, self.body_state * 32, 32, 32, self.x, self.y)
        # 터지는 중
        self.image_head.clip_draw(self.head_frame * 32, 5 * 32, 32, 32, self.x, self.y + 10)

    def update(self):
        #self.head_frame = (self.frame + 1) % 8
        self.body_frame = (self.body_frame + 1) % 8
        if self.isMove == True:
            #if self.direction == ISSAC_DIRECTION_UP:
            #    self.y+=1
            #elif self.direction == ISSAC_DIRECTION_DOWN:
            #    self.y-=1
            #elif self.direction == ISSAC_DIRECTION_LEFT:
            #    self.x-=1
            #elif self.direction == ISSAC_DIRECTION_RIGHT:
            #    self.x+=1

            if self.isLeft == True and self.isRight == False:
                self.x -= 1
            if self.isLeft == False and self.isRight == True:
                self.x += 1
            if self.isUp == True and self.isDown == False:
                self.y += 1
            if self.isUp == False and self.isDown == True:
                self.y -= 1

