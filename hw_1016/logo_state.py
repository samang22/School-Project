from pico2d import *
import game_framework
import time
import title_state

class Logo:
    def __init__(self):
        self.image = load_image('../res/kpu_credit.png')
        self.count = 0
        print(self.image)
    def draw(self):
        self.image.draw(400, 300)


def handle_events():
    global logo
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.quit()

def enter():
    global logo
    open_canvas()
    logo = Logo()


def draw():
    global logo
    clear_canvas()
    logo.draw()
    update_canvas()

def update():
    delay(0.01);
    logo.count+=1
    if logo.count >= 100:
        game_framework.change_state(title_state)


def exit():
    close_canvas()

if __name__ == '__main__':
    main()
