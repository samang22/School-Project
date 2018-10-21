from pico2d import *

ISSAC_IMAGE_STOP = 4
ISSAC_IMAGE_DOWN = 3
ISSAC_IMAGE_RIGHT = 2
ISSAC_IMAGE_LEFT = 1

ISSAC_DIRECTION_UP = 4
ISSAC_DIRECTION_DOWN = 3
ISSAC_DIRECTION_RIGHT = 2
ISSAC_DIRECTION_LEFT = 1



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

    def draw(self):
        # 몸
        if self.isMove == False:
            self.image_body.clip_draw(0, self.body_state * 32, 32, 32, self.x, self.y)
        else:
            self.image_body.clip_draw(self.body_frame * 32, self.body_state * 32, 32, 32, self.x, self.y)
        # 머리
        self.image_head.clip_draw(self.head_frame * 32, 5 * 32, 32, 32, self.x, self.y + 10)

    def update(self):
        #self.head_frame = (self.frame + 1) % 8
        self.body_frame = (self.body_frame + 1) % 8
        if self.isMove == True:
            if self.direction == ISSAC_DIRECTION_UP:
                self.y+=1
            elif self.direction == ISSAC_DIRECTION_DOWN:
                self.y-=1
            elif self.direction == ISSAC_DIRECTION_LEFT:
                self.x-=1
            elif self.direction == ISSAC_DIRECTION_RIGHT:
                self.x+=1

    def Move_Up(self):
        self.body_state = ISSAC_IMAGE_DOWN
        self.direction = ISSAC_DIRECTION_UP
        self.isMove = True

    def Move_Down(self):
        self.body_state = ISSAC_IMAGE_DOWN
        self.direction = ISSAC_DIRECTION_DOWN
        self.isMove = True

    def Move_Left(self):
        self.body_state = ISSAC_IMAGE_LEFT
        self.direction = ISSAC_DIRECTION_LEFT
        self.isMove = True

    def Move_Right(self):
        self.body_state = ISSAC_IMAGE_RIGHT
        self.direction = ISSAC_DIRECTION_RIGHT
        self.isMove = True

    def Move_Stop(self):
        self.isMove = False

def handle_events():
    global issac
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            #game_framework.change_state(title_state)
            game_framework.pop_state()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                #game_framework.change_state(title_state)
                game_framework.pop_state()
            if e.key == SDLK_LEFT:
                issac.Move_Left()
            if e.key == SDLK_RIGHT:
                issac.Move_Right()
            if e.key == SDLK_UP:
                issac.Move_Up()
            if e.key == SDLK_DOWN:
                issac.Move_Down()
        else:
            issac.Move_Stop()
            

def enter():
    global issac
    open_canvas()
    issac = Issac()


def draw():
    global issac
    clear_canvas()
    issac.draw()
    update_canvas()

def update():
    issac.update()
    delay(0.03)

# fill here

def exit():
    close_canvas()

if __name__ == '__main__':
    main()
