from pico2d import *
import math

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
                

            
# fill here
    
close_canvas()
