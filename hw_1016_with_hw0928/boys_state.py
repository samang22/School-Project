from pico2d import *
import game_framework
import random
from enum import Enum

IDLE, RUN, SLEEP = range(3)

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, TIME_OUT = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT) : LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT) : RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT) : LEFT_DOWN,
}

next_state_table = {
    IDLE: {RIGHT_UP: RUN, LEFT_UP: RUN, RIGHT_DOWN: RUN, LEFT_DOWN:RUN, TIME_OUT: SLEEP},
    RUN: {RIGHT_UP: IDLE, LEFT_UP: IDLE, RIGHT_DOWN: IDLE, LEFT_DOWN:IDLE},
    SLEEP: {LEFT_DOWN: RUN, RIGHT_DOWN: RUN}
}



class Grass:
    def __init__(self):
        self.image = load_image('../res/grass.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 30)



class Boy:
    boy_image = None




    def __init__(self):
        print("Creating..")
        self.x = random.randint(0, 200)
        self.y = random.randint(90, 550)
        self.speed = random.uniform(1.0, 3.0)
        self.frame = random.randint(0, 7)
        self.cur_state = Boy.enter_state
        self.dir = 0
        #self.isRun = False
        #self.isLeft = False
        self.state = 0
        if Boy.boy_image == None:
            Boy.boy_image = load_image('../res/run_animation.png')
    def draw(self):
        self.draw_state[self.cur_state](self)

    def update(self):
        self.update_state[self.cur_state](self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.change_state(next_state_table[self.cur_state][event])
    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event == RIGHT_DOWN:
                self.speed += 1
            elif key_event == LEFT_DOWN:
                self.speed -= 1
            elif key_event == RIGHT_UP:
                self.speed -= 1
            elif key_event == LEFT_DOWN:
                self.speed += 1
            self.add_event(key_event)

    def enter_IDLE(self):
        self.timer = 1000
        self.frame = 0
    def exit_IDLE(self):
        pass
    def update_IDLE(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(SLEEP_TIMER)
    def draw_IDLE(self):
        if self.dir == 1:
            #self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
            Boy.boy_image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)        
        else:
            #self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
            Boy.boy_image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

    def enter_RUN(self):
        self.frame = 0
        self.dir = self.speed

    def exit_RUN(self):
        pass
    def update_RUN(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.speed
        self.x = clamp(25, self.x, 800 - 25)

    def draw_RUN(self):
        if self.speed == 1:
            #self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
            Boy.boy_image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)        
        else:
            #self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
            Boy.boy_image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)        

    def enter_SLEEP(self):
        self.frame = 0

    def exit_SLEEP(self):
        pass
    def update_SLEEP(self):
        self.frame = (self.frame + 1) % 8

    def draw_SLEEP(self):
        if self.dir== 1:
            #self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
            Boy.boy_image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592/2, '', self.x-25, self.y-25, self.x, self.y)        
        else:
            #self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
            Boy.boy_image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592/2, '', self.x+25, self.y-25, self.x, self.y)        


    def change_state(self, state):
        self.exit_state[self.cur_state](self)
        self.enter_state[state](self)
        self.cur_state = state
    enter_state =   {IDLE: enter_IDLE, RUN: enter_RUN, SLEEP: enter_SLEEP}
    exit_state =    {IDLE: exit_IDLE, RUN: exit_RUN, SLEEP: exit_SLEEP}
    update_state =  {IDLE: update_IDLE, RUN: update_RUN, SLEEP: update_SLEEP}
    draw_state =    {IDLE: draw_IDLE, RUN: draw_RUN, SLEEP: draw_SLEEP}





#span = 50

def handle_events():
    global boy
    #global span
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.pop_state()
            elif e.key in range(SDLK_1, SDLK_9 + 1):
                span = 20 * (e.key - SDLK_0)

        #elif e.type == SDL_MOUSEBUTTONDOWN:
        #    if e.button == SDL_BUTTON_LEFT:
        #        tx, ty = e.x, 600 - e.y
        #        for b in boys:
        #            bx = tx + random.randint(-span, span)
        #            by = ty + random.randint(-span, span)
        #            b.waypoints += [ (bx, by) ]
        #    else:
        #        for b in boys:
        #            b.waypoints = []

def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()


# def main():
#     global running
#     enter()
#     while running:
#         handle_events()
#         print(running)
#         update()
#         draw()
#     exit()

def draw():
    global grass, boys
    clear_canvas()
    grass.draw()
    for b in boys:
        if b.image != None:
            b.draw()
    update_canvas()

def update():
    global boy
    boy.update()
    #    if b.image == None: b.image = boyimage
    #    if b.wp == None: b.wp = wpimage

            
    delay(0.01)

# fill here

def exit():
    pass

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]  
    open_canvas()
    game_framework.run(current_module)
    close_canvas()