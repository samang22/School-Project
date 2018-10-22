from pico2d import *
import issac 

def handle_events():
    global play_issac
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
                play_issac.Move_Left()
            #else:
            #    play_issac.Move_Left_Off()
            if e.key == SDLK_RIGHT:
                play_issac.Move_Right()
            #else:
            #    play_issac.Move_Right_Off()
            if e.key == SDLK_UP:
                play_issac.Move_Up()
            #else:
            #    play_issac.Move_Up_Off()
            if e.key == SDLK_DOWN:
                play_issac.Move_Down()
            #else:
            #    play_issac.Move_Down_Off()
        else:
            play_issac.Move_Stop()
            

def enter():
    global play_issac
    open_canvas()
    play_issac = issac.Issac()


def draw():
    global play_issac
    clear_canvas()
    play_issac.draw()
    update_canvas()

def update():
    play_issac.update()
    delay(0.03)

# fill here

def exit():
    close_canvas()

if __name__ == '__main__':
    main()
