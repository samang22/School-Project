from pico2d import *
import issac 
import fly
import meat
import hopper
import UI

def handle_events():
    global play_issac, hopperlist, meatlist

    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            #game_framework.change_state(title_state)
            game_framework.pop_state()
        elif e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
            game_framework.pop_state()
        elif e.type == SDL_KEYDOWN and e.key == SDLK_m:
            if len(meatlist) > 0:
                for m in meatlist:
                    m.Hit()
        elif e.type == SDL_KEYDOWN and e.key == SDLK_h:
            if len(hopperlist) > 0:
                for h in hopperlist:
                    h.Hit()

        else:
            play_issac.handle_event(e)

    play_UI.SetData(play_issac.GetBombNum(), play_issac.GetLifeNum(),play_issac.GetKeyNum(), play_issac.GetArrowKind())
            

def enter():
    global play_issac, play_UI, flylist, meatlist, hopperlist
    open_canvas()
    play_issac = issac.Issac()
    play_UI = UI.UI()
    
    flylist = []
    flylist.append(fly.Fly())

    meatlist = []
    meatlist.append(meat.Meat())

    hopperlist = []
    hopperlist.append(hopper.Hopper())

    play_UI.SetData(play_issac.GetBombNum(), play_issac.GetLifeNum(),play_issac.GetKeyNum(), play_issac.GetArrowKind())

def draw():
    global play_issac, play_UI, flylist, meatlist
    clear_canvas()
    play_UI.draw()
    play_issac.draw()
    if len(flylist) > 0:
       for f in flylist:
         f.draw()
    if len(meatlist) > 0:
       for m in meatlist:
         m.draw()
    if len(hopperlist) > 0:
       for h in hopperlist:
         h.draw()
    update_canvas()

def update():
    play_issac.update()
    if len(flylist) > 0:
       for f in flylist:
         f.update()
         f.SetIssacPos(play_issac.GetX(), play_issac.GetY())

    if len(meatlist) > 0:
       for m in meatlist:
         m.update()
         m.SetIssacPos(play_issac.GetX(), play_issac.GetY())

    if len(hopperlist) > 0:
       for h in hopperlist:
         h.update()
    
    delay(0.03)

# fill here

def exit():
    close_canvas()

if __name__ == '__main__':
    main()
