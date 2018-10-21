from pico2d import *


# 가만히 있으면 -1
ISSAC_STOP = 4
# 아래나 위로 움직이면 0
ISSAC_DOWN = 3
# 오른쪽으로 가면 1
ISSAC_RIGHT = 2
# 왼쪽으로 가면 2
ISSAC_LEFT = 1


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
        self.body_state = ISSAC_DOWN
        
    def draw(self):
        # 몸
        self.image_body.clip_draw(self.body_frame * 32, self.body_state * 32, 32, 32, self.x, self.y)
        # 머리
        self.image_head.clip_draw(self.head_frame * 32, self.head_state * 32, 32, 32, self.x, self.y + 10)

    def update(self):
        #self.head_frame = (self.frame + 1) % 8
        self.body_frame = (self.body_frame + 1) % 8

    def Move_Up(self):
        self.y += 1

    def Move_Down(self):
        self.y -= 1

    def Move_Left(self):
        self.x -= 1

    def Move_Right(self):
        self.x += 1

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
