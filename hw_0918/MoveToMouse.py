from pico2d import *
import math


# 왼쪽 키를 누르면 속도 감소
# 오른쪽 키를 누르면 속도가 증가하게 만들었습니다.
# 다만 기울기를 이용한 식으로 움직이게 만들어
# 마우스X좌표와 캐릭터의 X좌표가 겹칠 때
# 순식간에 움직이는 부분은 해결하지 못하였습니다.
 


def handle_events():
    global running, MouseX, MouseY, speed
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            speed+=1;
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            speed-=1;
        
        elif event.type == SDL_MOUSEMOTION:
            MouseX = event.x
            MouseY = 600 - event.y


def Move():
    global MouseX, MouseY, x, y, speed
    if (0 != MouseX - x):
        alpha = (MouseY - y) / (MouseX - x)
    elif MouseX - x == 0:
        if MouseY > y:
            return y + speed / 100
        else:
            return y - speed / 100
        
    beta = y - alpha*x
    
    if MouseX > x :
        return alpha * (x + speed) + beta
    else:
        return alpha * (x - speed) + beta
    
open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')



running = True

frame = 0
x = 400
y = 90
MouseX = 0
MouseY = 0
speed = 1

while (True == running):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    handle_events()
    y = Move()
    if MouseX > x:
        x = x + speed
    else:
        x = x - speed        
    frame = (frame + 1) % 8
    delay(0.02)
    
                    
close_canvas()
