from pico2d import *
import issac 
import fly
import meat
import hopper
import UI
import game_world
import ID
import game_framework

def handle_events():
#    global play_issac, meatlist, hopperlist
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            #game_framework.change_state(title_state)
            game_framework.pop_state()
        elif e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
            game_framework.pop_state()
        #elif e.type == SDL_KEYDOWN and e.key == SDLK_m:
        #    if len(meatlist) > 0:
        #        for m in meatlist:
        #            m.Hit()
        #elif e.type == SDL_KEYDOWN and e.key == SDLK_h:
        #    if len(hopperlist) > 0:
        #        for h in hopperlist:
        #            h.Hit()

        else:
            for o in game_world.issac_objects():
                if o.GetID() == ID.ISSAC:
                    o.handle_event(e)
                    break

    for o in game_world.background_objects():
        for i in game_world.issac_objects():
            if o.GetID() == ID.UI and i.GetID() == ID.ISSAC:
                o.SetData(i.GetBombNum(), i.GetLifeNum(),i.GetKeyNum(), i.GetArrowKind())

    #play_UI.SetData(play_issac.GetBombNum(), play_issac.GetLifeNum(),play_issac.GetKeyNum(), play_issac.GetArrowKind())
            

def enter():
#    global play_issac, play_UI, flylist, meatlist, hopperlist
    global play_UI
    open_canvas()
    play_issac = issac.Issac()
    play_UI = UI.UI()
    play_fly = fly.Fly()
    play_hopper = hopper.Hopper()
    play_meat = meat.Meat()
    
    #flylist = []
    #flylist.append(fly.Fly())

#    meatlist = []
#    meatlist.append(meat.Meat())

#    hopperlist = []
#    hopperlist.append(hopper.Hopper())
    
    game_world.add_object(play_issac, game_world.LAYER_ISSAC)
    game_world.add_object(play_fly,game_world.LAYER_MONSTER)
    game_world.add_object(play_hopper,game_world.LAYER_MONSTER)
    game_world.add_object(play_meat,game_world.LAYER_MONSTER)

    game_world.add_object(play_UI,game_world.LAYER_BG)



    play_UI.SetData(play_issac.GetBombNum(), play_issac.GetLifeNum(),play_issac.GetKeyNum(), play_issac.GetArrowKind())

def collides(a, b):
    if not hasattr(a, 'get_bb'): return False
    if not hasattr(b, 'get_bb'): return False

    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()
    if la > ra: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False
    return True

def draw():
#    global play_issac, play_UI, flylist, meatlist, hopperlist
    clear_canvas()

    #play_UI.draw()
    #play_issac.draw()
    #if len(flylist) > 0:
    #   for f in flylist:
    #     f.draw()
    #if len(meatlist) > 0:
    #   for m in meatlist:
    #     m.draw()
    #if len(hopperlist) > 0:
    #   for h in hopperlist:
    #     h.draw()

    for o in game_world.all_objects():
        o.draw()
    update_canvas()

def update():
    #play_issac.update()
    #if len(flylist) > 0:
    #   for f in flylist:
    #     f.update()
    #     f.SetIssacPos(play_issac.GetX(), play_issac.GetY())

    #if len(meatlist) > 0:
    #   for m in meatlist:
    #     m.update()
    #     m.SetIssacPos(play_issac.GetX(), play_issac.GetY())
    #if len(hopperlist) > 0:
    #   for h in hopperlist:
    #     h.update()
    
    #for issac_object in game_world.object_at_layer(game_world.LAYER_ISSAC):
    #    for monster_object in game_world.object_at_layer(game_world.LAYER_MONSTER):
    #        if 

    for o in game_world.all_objects():
        if hasattr(o, "GetIsEnd"):
            if o.GetIsEnd():
                game_world.remove_object(o)

    for m in game_world.monster_objects():
        if hasattr(m, "SetIssacPos"):
            for i in game_world.issac_objects():
                if hasattr(i, "GetX"):
                    m.SetIssacPos(i.GetX(), i.GetY())


    for o in game_world.all_objects():
        o.update()

    # 충돌체크
    for i in game_world.issac_objects():
        for m in game_world.monster_objects():
            if i.GetID() == ID.TEAR or i.GetID() == ID.BOMB:
                if collides(i, m):
                    m.Hit(i.GetDamage())
                    if i.GetID() == ID.TEAR:
                        i.SetPop()
                    print(m.ID)


    delay(0.03)

# fill here

def exit():
    for o in game_world.all_objects():
        game_world.remove_object(o)
    close_canvas()

if __name__ == '__main__':
    main()
