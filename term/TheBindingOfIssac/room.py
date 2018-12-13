from pico2d import *
import config
import game_world
import ID
import game_framework



class Room:
    ROOM_WIDTH = 800
    ROOM_HEIGHT = 500
    DOOR_WIDTH = 50
    DOOR_HEIGHT = 50


    CAVE_0, CAVE_1, CAVE_2, CAVE_3, CABIN_0, CABIN_1, CABIN_2, CABIN_3 = range(8)

    #CAVE_0 = 0
    #CAVE_1 = 1
    #CAVE_2 = 2
    #CAVE_3 = 3
    
    #CABIN_0 = 4
    #CABIN_1 = 5
    #CABIN_2 = 6
    #CABIN_3 = 7

    DOOR_OPEN, DOOR_CLOSED, DOOR_LOCK, DOOR_ABSENCE = range(4)
    LEFT_DOOR_X = 50
    LEFT_DOOR_Y = 250

    RIGHT_DOOR_X = 750
    RIGHT_DOOR_Y = 250

    UP_DOOR_X = 400
    UP_DOOR_Y = 450

    DOWN_DOOR_X = 400
    DOWN_DOOR_Y = 50

    IMAGE_SIZE = 50

    isDone_CAVE_0 = False
    isDone_CAVE_1 = False
    isDone_CAVE_2 = False
    isDone_CAVE_3 = False

    isDone_CABIN_0 = False
    isDone_CABIN_1 = False
    isDone_CABIN_2 = False
    isDone_CABIN_3 = False

    def __init__(self):
        print("Creating Room")
        self.x = 400
        self.y = 250

        self.cave_image0 = load_image('../resource/Cave_0.png')
        self.cave_image1 = load_image('../resource/Cave_1.png')
        self.cave_image2 = load_image('../resource/Cave_2.png')
        self.cave_image3 = load_image('../resource/Cave_3.png')

        self.cabin_image0 = load_image('../resource/Cabin_0.png')
        self.cabin_image1 = load_image('../resource/Cabin_1.png')
        self.cabin_image2 = load_image('../resource/Cabin_2.png')
        self.cabin_image3 = load_image('../resource/Cabin_3.png')

        self.opendoor_up = load_image('../resource/OpenDoor_Up.png')
        self.opendoor_down = load_image('../resource/OpenDoor_Down.png')
        self.opendoor_left = load_image('../resource/OpenDoor_Left.png')
        self.opendoor_right = load_image('../resource/OpenDoor_Right.png')

        self.closeddoor_up = load_image('../resource/ClosedDoor_Up.png')
        self.closeddoor_down = load_image('../resource/ClosedDoor_Down.png')
        self.closeddoor_left = load_image('../resource/ClosedDoor_Left.png')
        self.closeddoor_right = load_image('../resource/ClosedDoor_Right.png')

        self.lockdoor_up = load_image('../resource/LockDoor_Up.png')
        self.lockdoor_down = load_image('../resource/LockDoor_Down.png')
        self.lockdoor_left = load_image('../resource/LockDoor_Left.png')
        self.lockdoor_right = load_image('../resource/LockDoor_Right.png')

        self.current_room = Room.CAVE_0

        self.up_door_state = 0
        self.down_door_state = 0
        self.left_door_state = 0
        self.right_door_state = 0

        self.ID = ID.ROOM
        self.isClear = False

    def draw(self):
        # 방
        if self.current_room == Room.CAVE_0:
            self.cave_image0.clip_draw(0, 0, Room.ROOM_WIDTH, Room.ROOM_HEIGHT, self.x, self.y)
        elif self.current_room == Room.CAVE_1:
            self.cave_image1.clip_draw(0, 0, Room.ROOM_WIDTH, Room.ROOM_HEIGHT, self.x, self.y)
        elif self.current_room == Room.CAVE_2:
            self.cave_image2.clip_draw(0, 0, Room.ROOM_WIDTH, Room.ROOM_HEIGHT, self.x, self.y)
        elif self.current_room == Room.CAVE_3:
            self.cave_image3.clip_draw(0, 0, Room.ROOM_WIDTH, Room.ROOM_HEIGHT, self.x, self.y)

        elif self.current_room == Room.CABIN_0:
            self.cabin_image0.clip_draw(0, 0, Room.ROOM_WIDTH, Room.ROOM_HEIGHT, self.x, self.y)
        elif self.current_room == Room.CABIN_1:
            self.cabin_image1.clip_draw(0, 0, Room.ROOM_WIDTH, Room.ROOM_HEIGHT, self.x, self.y)
        elif self.current_room == Room.CABIN_2:
            self.cabin_image2.clip_draw(0, 0, Room.ROOM_WIDTH, Room.ROOM_HEIGHT, self.x, self.y)
        elif self.current_room == Room.CABIN_3:
            self.cabin_image3.clip_draw(0, 0, Room.ROOM_WIDTH, Room.ROOM_HEIGHT, self.x, self.y)

        # 왼쪽 문
        if self.left_door_state == Room.DOOR_OPEN:
            self.opendoor_left.clip_draw(0, 0, Room.DOOR_WIDTH, Room.DOOR_HEIGHT, Room.LEFT_DOOR_X, Room.LEFT_DOOR_Y)
        elif self.left_door_state == Room.DOOR_CLOSED:
            self.closeddoor_left.clip_draw(0, 0, Room.DOOR_WIDTH, Room.DOOR_HEIGHT, Room.LEFT_DOOR_X, Room.LEFT_DOOR_Y)
        elif self.left_door_state == Room.DOOR_LOCK:
            self.lockdoor_left.clip_draw(0, 0, Room.DOOR_WIDTH, Room.DOOR_HEIGHT, Room.LEFT_DOOR_X, Room.LEFT_DOOR_Y)

        # 오른쪽 문
        if self.right_door_state == Room.DOOR_OPEN:
            self.opendoor_right.clip_draw(0, 0, Room.DOOR_WIDTH, Room.DOOR_HEIGHT, Room.RIGHT_DOOR_X, Room.RIGHT_DOOR_Y)
        elif self.right_door_state == Room.DOOR_CLOSED:
            self.closeddoor_right.clip_draw(0, 0, Room.DOOR_WIDTH, Room.DOOR_HEIGHT, Room.RIGHT_DOOR_X, Room.RIGHT_DOOR_Y)
        elif self.right_door_state == Room.DOOR_LOCK:
            self.lockdoor_right.clip_draw(0, 0, Room.DOOR_WIDTH, Room.DOOR_HEIGHT, Room.RIGHT_DOOR_X, Room.RIGHT_DOOR_Y)

        # 위쪽 문
        if self.up_door_state == Room.DOOR_OPEN:
            self.opendoor_up.clip_draw(0, 0, Room.DOOR_WIDTH, Room.DOOR_HEIGHT, Room.UP_DOOR_X, Room.UP_DOOR_Y)
        elif self.up_door_state == Room.DOOR_CLOSED:
            self.closeddoor_up.clip_draw(0, 0, Room.DOOR_WIDTH, Room.DOOR_HEIGHT, Room.UP_DOOR_X, Room.UP_DOOR_Y)
        elif self.up_door_state == Room.DOOR_LOCK:
            self.lockdoor_up.clip_draw(0, 0, Room.DOOR_WIDTH, Room.DOOR_HEIGHT, Room.UP_DOOR_X, Room.UP_DOOR_Y)

        # 아래쪽 문
        if self.down_door_state == Room.DOOR_OPEN:
            self.opendoor_down.clip_draw(0, 0, Room.DOOR_WIDTH, Room.DOOR_HEIGHT, Room.DOWN_DOOR_X, Room.DOWN_DOOR_Y)
        elif self.down_door_state == Room.DOOR_CLOSED:
            self.closeddoor_down.clip_draw(0, 0, Room.DOOR_WIDTH, Room.DOOR_HEIGHT, Room.DOWN_DOOR_X, Room.DOWN_DOOR_Y)
        elif self.down_door_state == Room.DOOR_LOCK:
            self.lockdoor_down.clip_draw(0, 0, Room.DOOR_WIDTH, Room.DOOR_HEIGHT, Room.DOWN_DOOR_X, Room.DOWN_DOOR_Y)


        # BB 그리기
        #if config.draws_bounding_box:
        #    draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
#        return self.x - (MEAT_IMAGE_SIZE / 2) + 15, self.y - (MEAT_IMAGE_SIZE / 2) + 15,self.x + (MEAT_IMAGE_SIZE / 2) - 15,self.y + (MEAT_IMAGE_SIZE / 2) - 15
        pass
    def left_get_bb(self):
        return Room.LEFT_DOOR_X - (Room.IMAGE_SIZE / 2), Room.LEFT_DOOR_Y - (Room.IMAGE_SIZE / 2), Room.LEFT_DOOR_X + (Room.IMAGE_SIZE / 2) - 15, Room.LEFT_DOOR_Y + (Room.IMAGE_SIZE  / 2)

    def right_get_bb(self):
        return Room.RIGHT_DOOR_X - (Room.IMAGE_SIZE / 2), Room.RIGHT_DOOR_Y - (Room.IMAGE_SIZE / 2), Room.RIGHT_DOOR_X + (Room.IMAGE_SIZE / 2) - 15, Room.RIGHT_DOOR_Y + (Room.IMAGE_SIZE  / 2)

    def up_get_bb(self):
        return Room.UP_DOOR_X - (Room.IMAGE_SIZE / 2), Room.UP_DOOR_Y - (Room.IMAGE_SIZE / 2), Room.UP_DOOR_X + (Room.IMAGE_SIZE / 2) - 15, Room.UP_DOOR_Y + (Room.IMAGE_SIZE  / 2)

    def down_get_bb(self):
        return Room.DOWN_DOOR_X - (Room.IMAGE_SIZE / 2), Room.DOWN_DOOR_Y - (Room.IMAGE_SIZE / 2), Room.DOWN_DOOR_X + (Room.IMAGE_SIZE / 2) - 15, Room.DOWN_DOOR_Y + (Room.IMAGE_SIZE  / 2)


    def GetID(self):
        return self.ID
    def SetRoom(self, _Room):
        self.current_room = _Room
    def SetClear(self, _clear):
        self.isClear = _clear
    def GetClear(self):
        if Room.CAVE_0 == self.current_room:
            return Room.isDone_CAVE_0
        elif Room.CAVE_1 == self.current_room:
            return Room.isDone_CAVE_1
        elif Room.CAVE_2 == self.current_room:
            return Room.isDone_CAVE_2
        elif Room.CAVE_3 == self.current_room:
            return Room.isDone_CAVE_3
        elif Room.CABIN_0 == self.current_room:
            return Room.isDone_CABIN_0
        elif Room.CABIN_1 == self.current_room:
            return Room.isDone_CABIN_1
        elif Room.CABIN_2 == self.current_room:
            return Room.isDone_CABIN_2
        elif Room.CABIN_3 == self.current_room:
            return Room.isDone_CABIN_3
    def GetRoom(self):
        return self.current_room

    def GetLeftDoorState(self):
        return self.left_door_state
    def GetRightDoorState(self):
        return self.right_door_state
    def GetUpDoorState(self):
        return self.up_door_state
    def GetDownDoorState(self):
        return self.down_door_state

    def SetDoor(self, _left, _right, _up, _down):
        self.left_door_state = _left
        self.right_door_state = _right
        self.up_door_state = _up
        self.down_door_state = _down

    def RoomClear(self):
        if self.left_door_state == Room.DOOR_CLOSED:
            self.left_door_state = Room.DOOR_OPEN
        if self.right_door_state == Room.DOOR_CLOSED:
            self.right_door_state = Room.DOOR_OPEN
        if self.up_door_state == Room.DOOR_CLOSED:
            self.up_door_state = Room.DOOR_OPEN
        if self.down_door_state == Room.DOOR_CLOSED:
            self.down_door_state = Room.DOOR_OPEN

        if Room.CAVE_0 == self.current_room:
            Room.isDone_CAVE_0 = True
        elif Room.CAVE_1 == self.current_room:
            Room.isDone_CAVE_1 = True
        elif Room.CAVE_2 == self.current_room:
            Room.isDone_CAVE_2 = True
        elif Room.CAVE_3 == self.current_room:
            Room.isDone_CAVE_3 = True
        elif Room.CABIN_0 == self.current_room:
            Room.isDone_CABIN_0 = True
        elif Room.CABIN_1 == self.current_room:
            Room.isDone_CABIN_1 = True
        elif Room.CABIN_2 == self.current_room:
            Room.isDone_CABIN_2 = True
        elif Room.CABIN_3 == self.current_room:
            Room.isDone_CABIN_3 = True
    
    def InitDoorWithRoom(self):
        # 처음 방
        if self.current_room == Room.CAVE_0:
            self.left_door_state = Room.DOOR_ABSENCE
            self.right_door_state = Room.DOOR_CLOSED
            self.up_door_state = Room.DOOR_ABSENCE
            self.down_door_state = Room.DOOR_ABSENCE
        # 중간 방
        if self.current_room == Room.CAVE_1:
            self.left_door_state = Room.DOOR_CLOSED
            self.right_door_state = Room.DOOR_CLOSED
            self.up_door_state = Room.DOOR_CLOSED
            self.down_door_state = Room.DOOR_LOCK
        # 윗 방
        if self.current_room == Room.CAVE_2:
            self.left_door_state = Room.DOOR_ABSENCE
            self.right_door_state = Room.DOOR_ABSENCE
            self.up_door_state = Room.DOOR_ABSENCE
            self.down_door_state = Room.DOOR_CLOSED
        # 오른쪽방 (보스방)
        if self.current_room == Room.CAVE_3:
            self.left_door_state = Room.DOOR_CLOSED
            self.right_door_state = Room.DOOR_ABSENCE
            self.up_door_state = Room.DOOR_ABSENCE
            self.down_door_state = Room.DOOR_ABSENCE
            # 다음 스테이지 문 추가

        # 스테이지 2
        # 시작 방
        if self.current_room == Room.CABIN_0:
            self.left_door_state = Room.DOOR_CLOSED
            self.right_door_state = Room.DOOR_ABSENCE
            self.up_door_state = Room.DOOR_ABSENCE
            self.down_door_state = Room.DOOR_ABSENCE
        # 중간 방
        if self.current_room == Room.CABIN_1:
            self.left_door_state = Room.DOOR_CLOSED
            self.right_door_state = Room.DOOR_CLOSED
            self.up_door_state = Room.DOOR_ABSENCE
            self.down_door_state = Room.DOOR_LOCK
        # 아랫방
        if self.current_room == Room.CABIN_2:
            self.left_door_state = Room.DOOR_ABSENCE
            self.right_door_state = Room.DOOR_ABSENCE
            self.up_door_state = Room.DOOR_CLOSED
            self.down_door_state = Room.DOOR_ABSENCE
        # 왼쪽방 (보스방)
        if self.current_room == Room.CABIN_3:
            self.left_door_state = Room.DOOR_ABSENCE
            self.right_door_state = Room.DOOR_CLOSED
            self.up_door_state = Room.DOOR_ABSENCE
            self.down_door_state = Room.DOOR_ABSENCE
            