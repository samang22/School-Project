from pico2d import *
import issac 
import fly
import meat
import hopper
import UI
import game_world
import ID
import game_framework
import room
import json
import item

GAMESTATE_READY, GAMESTATE_INPLAY, GAMESTATE_PAUSED, GAMESTETE_GAMEOVER = range(4)
CAVE_0, CAVE_1, CAVE_2, CAVE_3, CABIN_0, CABIN_1, CABIN_2, CABIN_3 = range(8) 
gameState = GAMESTATE_READY
roomNum = CAVE_0

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
                o.SetData(i.GetBombNum(), i.GetLifeNum(),i.GetKeyNum(), i.GetWeaponKind())

    #play_UI.SetData(play_issac.GetBombNum(), play_issac.GetLifeNum(),play_issac.GetKeyNum(), play_issac.GetArrowKind())
            

def enter():
    global play_UI, monster_data
    open_canvas()
    play_UI = UI.UI()
    play_issac = issac.Issac()
    play_room = room.Room()
    play_UI.SetData(play_issac.GetBombNum(), play_issac.GetLifeNum(), play_issac.GetKeyNum(), play_issac.GetWeaponKind())
    game_world.add_object(play_issac, game_world.LAYER_ISSAC)
    game_world.add_object(play_UI, game_world.LAYER_BG)
    game_world.add_object(play_room, game_world.LAYER_BG)
    ready_game()



#def start_game():
#    global gameState
#    gameState = GAMESTATE_INPLAY

    #global music_bg
    # music_bg.set_volume(64)
    # music_bg.repeat_play()

def goto_next_room(_room):
    global roomNum
    roomNum = _room
    ready_game()

def ready_game():
    #global gameState
    #gameState = GAMESTATE_READY
    game_world.remove_objects_at_layer(game_world.LAYER_MONSTER)
    game_world.remove_all_item()                

    f = open('monster.json', 'r')
    monster_data = json.load(f)
    f.close()

    f = open('room.json', 'r')
    room_data = json.load(f)
    f.close()

    monster_arr = None
    item_data = None
    # 방, 몬스터 정보 받기      
    for o in game_world.background_objects():
        if o.GetID() == ID.ROOM:
            if roomNum == CAVE_0:
                monster_arr = monster_data['cave_0']    
                room_info = room_data['cave_0']    
                o.SetRoom(CAVE_0)
            elif roomNum == CAVE_1:
                monster_arr = monster_data['cave_1']
                room_info = room_data['cave_1']    
                o.SetRoom(CAVE_1)
            elif roomNum == CAVE_2:
                monster_arr = monster_data['cave_2']
                room_info = room_data['cave_2']    
                o.SetRoom(CAVE_2)
            elif roomNum == CAVE_3:
                monster_arr = monster_data['cave_3']
                room_info = room_data['cave_3']    
                o.SetRoom(CAVE_3)
            elif roomNum == CABIN_0:
                monster_arr = monster_data['cabin_0']
                room_info = room_data['cabin_0']    
                o.SetRoom(CABIN_0)
            elif roomNum == CABIN_1:
                monster_arr = monster_data['cabin_1']
                room_info = room_data['cabin_1']    
                o.SetRoom(CABIN_1)
            elif roomNum == CABIN_2:
                monster_arr = monster_data['cabin_2']
                room_info = room_data['cabin_2']    
                o.SetRoom(CABIN_2)
            elif roomNum == CABIN_3:
                monster_arr = monster_data['cabin_3']
                room_info = room_data['cabin_3']    
                o.SetRoom(CABIN_3)
            break;


    for o in game_world.background_objects():
        if o.GetID() == ID.ROOM:
            if not o.GetIsClear():    
                # 몬스터 생성
                for d in monster_arr:
                    if d["ID"] == ID.FLY:
                        _monster = fly.Fly(d["x"], d["y"])
                    elif d["ID"] == ID.MEAT:
                        _monster = meat.Meat(d["x"], d["y"])
                    elif d["ID"] == ID.HOPPER:
                        _monster = hopper.Hopper(d["x"], d["y"])
                    game_world.add_object(_monster, game_world.LAYER_MONSTER)
                # 아이템 미리 생성
                item_data = item.Item(room_info["item"], 400, 150)
                game_world.add_object(item_data, game_world.LAYER_BG)
                break;

    # 문 생성
    for o in game_world.background_objects():
        if o.GetID() == ID.ROOM:
            o.SetDoor(room_info["left"], room_info["right"], room_info["up"], room_info["down"], room_info["stage"])

#def end_game():
#    global gameState
#    gameState = GAMESTETE_GAMEOVER


def collides(a, b):
    if not hasattr(a, 'get_bb'): return False
    if not hasattr(b, 'get_bb'): return False

    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()
    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False
    return True

def door_collides(d, b):
    if not hasattr(b, 'get_bb'): return False

    ld, bd, rd, td = d
    lb, bb, rb, tb = b.get_bb()
    if ld > rb: return False
    if rd < lb: return False
    if td < bb: return False
    if bd > tb: return False
    return True

def draw():
    clear_canvas()

    for o in game_world.all_objects():
        o.draw()
    update_canvas()

def update():
    # 삭제될 오브젝트들 삭제
    for o in game_world.all_objects():
        if hasattr(o, "GetIsEnd"):
            if o.GetIsEnd():
                game_world.remove_object(o)

    # 몬스터들에게 아이작 좌표 전달
    for m in game_world.monster_objects():
        if hasattr(m, "SetIssacPos"):
            for i in game_world.issac_objects():
                if hasattr(i, "GetX"):
                    m.SetIssacPos(i.GetX(), i.GetY())

    # 오브젝트 업데이트
    for o in game_world.all_objects():
        o.update()

    # 충돌체크
    # 아이작 눈물, 폭탄
    for i in game_world.issac_objects():
        for m in game_world.monster_objects():
            if i.GetID() == ID.TEAR or i.GetID() == ID.BOMB or i.GetID() == ID.RAZOR:
                if collides(i, m):
                    m.Hit(i.GetDamage())
                    if i.GetID() == ID.TEAR:
                        i.SetPop()
                    print(m.ID)

    # 아이작, 몬스터
    for i in game_world.issac_objects():
        for m in game_world.monster_objects():
            if i.GetID() == ID.ISSAC:
                if collides(i, m):
                    i.Hit(m.GetDamage())


    # 아이작, 아이템
    for i in game_world.issac_objects():
        for m in game_world.bg_objects():
            if i.GetID() == ID.ISSAC and m.GetID() == ID.ITEM:
                if collides(i, m):
                    if m.GetItemID() == item.Item.HEART or m.GetItemID() == item.Item.KEY or m.GetItemID() == item.Item.BOMB:
                        i.GetConsumableItem(m.GetItemID())
                        m.SetEnd()
                    elif m.GetItemID() == item.Item.TEAR or m.GetItemID() == item.Item.TRIPLE or m.GetItemID() == item.Item.RAZOR:
                        if i.GetIsSpaceDown():
                            if i.GetY() > 250:  
                                temp_item = item.Item(i.GetWeaponKind(), i.GetX(), i.GetY() - 100)
                            else:
                                temp_item = item.Item(i.GetWeaponKind(), i.GetX(), i.GetY() + 100)
                            temp_item.SetExposed()
                            game_world.add_object(temp_item, game_world.LAYER_BG)
                            i.SetWeaponItem(m.GetItemID())
                            m.SetEnd()
                            

    # 클리어할 경우 열린문과 충돌 체크후 방 넘어가기
    for o in game_world.background_objects():
        if o.GetID() == ID.ROOM:
            if o.GetIsClear() == True:
                for i in game_world.issac_objects():
                    if i.GetID() == ID.ISSAC:
                        if door_collides(o.left_get_bb(), i) and o.GetLeftDoorState() == room.Room.DOOR_OPEN:
                            if o.GetRoom() == room.Room.CAVE_1:
                                goto_next_room(room.Room.CAVE_0)
                            elif o.GetRoom() == room.Room.CAVE_3:
                                goto_next_room(room.Room.CAVE_1)
                            elif o.GetRoom() == room.Room.CABIN_0:
                                goto_next_room(room.Room.CABIN_1)
                            elif o.GetRoom() == room.Room.CABIN_1:
                                goto_next_room(room.Room.CABIN_3)
                            i.SetPos(675, 250)
                        elif door_collides(o.left_get_bb(), i) and o.GetLeftDoorState() == room.Room.DOOR_LOCK:
                            pass
                        if door_collides(o.right_get_bb(), i) and o.GetRightDoorState() == room.Room.DOOR_OPEN:
                            if o.GetRoom() == room.Room.CAVE_0:
                                goto_next_room(room.Room.CAVE_1)
                            elif o.GetRoom() == room.Room.CAVE_1:
                                goto_next_room(room.Room.CAVE_3)
                            elif o.GetRoom() == room.Room.CABIN_1:
                                goto_next_room(room.Room.CABIN_0)
                            elif o.GetRoom() == room.Room.CABIN_3:
                                goto_next_room(room.Room.CABIN_1)
                            i.SetPos(125, 250)
                        if door_collides(o.up_get_bb(), i) and o.GetUpDoorState() == room.Room.DOOR_OPEN:
                            if o.GetRoom() == room.Room.CAVE_1:
                                goto_next_room(room.Room.CAVE_2)
                            elif o.GetRoom() == room.Room.CABIN_2:
                                goto_next_room(room.Room.CABIN_1)
                            i.SetPos(400, 125)

                        elif door_collides(o.up_get_bb(), i) and o.GetUpDoorState() == room.Room.DOOR_LOCK:
                            if i.GetKeyNum() > 0:
                                i.UseKey()
                                if o.GetRoom() == room.Room.CAVE_1:
                                    goto_next_room(room.Room.CAVE_2)
                                    i.SetPos(400, 125)

                        if door_collides(o.down_get_bb(), i) and o.GetDownDoorState() == room.Room.DOOR_OPEN:
                            if o.GetRoom() == room.Room.CAVE_2:
                                goto_next_room(room.Room.CAVE_1)
                            elif o.GetRoom() == room.Room.CABIN_1:
                                goto_next_room(room.Room.CABIN_2)
                            i.SetPos(400, 425)
                        elif door_collides(o.down_get_bb(), i) and o.GetDownDoorState() == room.Room.DOOR_LOCK:
                            if i.GetKeyNum() > 0:
                                i.UseKey()
                                if o.GetRoom() == room.Room.CABIN_1:
                                    goto_next_room(room.Room.CABIN_2)
                                    i.SetPos(400, 425)
                        if door_collides(o.stage_get_bb(), i) and o.GetStageDoorState() == room.Room.DOOR_OPEN:
                            if o.GetRoom() == room.Room.CAVE_3:
                                goto_next_room(room.Room.CABIN_0)
    
    room_clear()

    delay(0.03)

def room_clear():
    if 0 == game_world.GetMonsterNum():
        for o in game_world.background_objects():
            if o.GetID() == ID.ROOM:
                o.RoomClear()
                # 아이템 보이게
                for i in game_world.background_objects():
                    if i.GetID() == ID.ITEM:
                        i.SetExposed()
def exit():
    for o in game_world.all_objects():
        game_world.remove_object(o)
    close_canvas()

if __name__ == '__main__':
    main()
