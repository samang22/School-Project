from pico2d import *
import issac 
import UI

def handle_events():
    global play_issac
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            #game_framework.change_state(title_state)
            game_framework.pop_state()
        elif e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
                game_framework.pop_state()
        else:
            play_issac.handle_event(e)
        #    elif e.key == SDLK_LEFT:
        #        play_issac.Move_Left()
        #        #return
        #    elif e.key == SDLK_RIGHT:
        #        play_issac.Move_Right()
        #        #return
        #    elif e.key == SDLK_UP:
        #        play_issac.Move_Up()
        #        #return
        #    elif e.key == SDLK_DOWN:
        #        play_issac.Move_Down()
        #        #return
        #    ## 총알 발사
        #    if e.key == SDLK_w:
        #        play_issac.Shoot(issac.tear.TEAR_DIRECTION_UP)
        #        #return
        #    if e.key == SDLK_a:
        #        play_issac.Shoot(issac.tear.TEAR_DIRECTION_LEFT)
        #        #return
        #    if e.key == SDLK_s:
        #        play_issac.Shoot(issac.tear.TEAR_DIRECTION_DOWN)
        #        #return
        #    if e.key == SDLK_d:
        #        play_issac.Shoot(issac.tear.TEAR_DIRECTION_RIGHT)
        #        #return
        #    if e.key == SDLK_e:
        #        play_issac.Plant_Bomb()
        #elif e.type == SDL_KEYUP:
        #    if e.key == SDLK_UP:
        #        play_issac.Move_Up_Off()
        #        return
        #    if e.key == SDLK_DOWN:
        #        play_issac.Move_Down_Off()
        #        return
        #    if e.key == SDLK_LEFT:
        #        play_issac.Move_Left_Off()
        #        return
        #    if e.key == SDLK_UP:
        #        play_issac.Move_Right_Off()
        #        return
        #else:
        #    play_issac.Move_Stop()
    play_UI.SetData(play_issac.GetBombNum(), play_issac.GetLifeNum(),play_issac.GetKeyNum(), play_issac.GetArrowKind())
            

def enter():
    global play_issac, play_UI
    open_canvas()
    play_issac = issac.Issac()
    play_UI = UI.UI()
    play_UI.SetData(play_issac.GetBombNum(), play_issac.GetLifeNum(),play_issac.GetKeyNum(), play_issac.GetArrowKind())

def draw():
    global play_issac, play_UI
    clear_canvas()
    play_UI.draw()
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
