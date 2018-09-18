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

open_canvas()

grass = pico2d.load_image('grass.png')
character = pico2d.load_image('run_animation.png')




x = 0
y = 90
Dir = 0
Mode = True
angle = 0
rad = 0
frame = 0
button = False
while (True):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    frame = (frame + 1) % 8
    update_canvas()
    delay(0.01)
    if (True == Mode):
        if (0 == Dir):
            x = x + 2
            if (800 <= x):
                Dir = 1
            if (x >= 390 and x <400 and button == True):
                Mode = False
                button = False
        elif (1 == Dir):
            y = y + 2
            if (600 <= y):
                Dir = 2
        elif (2 == Dir):
            x = x - 2
            if (0 >= x):
                Dir = 3
        elif (3 == Dir):
            y = y - 2
            if (90 >= y):
                Dir = 0
                button = True
                

    else:
        angle = (angle + 5)
        if (angle <= 90 and angle >= 0):
            rad = math.radians(angle)
            x = 400 + math.sin(rad) * 255
            y = 345 - math.cos(rad) * 255 
        elif (angle > 90 and angle <= 180):
            rad = math.radians(angle - 90)
            x = 400 + 255 * math.cos(rad)
            y = 345 + math.sin(rad) * 255
        elif (angle > 180 and angle <= 270):
            rad = math.radians(angle - 180)
            x = 400 - math.sin(rad) * 255
            y = 345 + math.cos(rad) * 255
        elif (angle > 270 and angle < 360):
            rad = math.radians(angle - 270)
            x = 400 - 255 * math.cos(rad)
            y = 345 - 255 * math.sin(rad)
        elif (angle == 360):
            angle = 0
            Mode = True
            
# fill here
    
close_canvas()
