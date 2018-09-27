from pico2d import *
def handle_events():
    global running
    global speed
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
            elif e.key == SDLK_LEFT:
                speed -= 1;
            elif e.key == SDLK_RIGHT:
                speed += 1;
                
class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def draw(self):
        self.image.clip_draw(frame * 100, 0, 100, 100, x, y)
        
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 2
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 30)

open_canvas()
frame = 0
x = 0
y = 90
grass = Grass()
boy = Boy()
running = True


while (True == running):
    boy.update()

    clear_canvas()
    boy.draw()
    grass.draw()

    update_canvas()
    handle_events()
    
