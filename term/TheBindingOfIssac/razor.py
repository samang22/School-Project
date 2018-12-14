from pico2d import *
import config
import ID
import game_framework



#RAZOR_DIRECTION_UP = 1
#RAZOR_DIRECTION_DOWN = 2
#RAZOR_DIRECTION_LEFT = 3
#RAZOR_DIRECTION_RIGHT = 4

RAZOR_IMAGE_SIZE = 64



class Razor:
    RAZOR_DIRECTION_UP, RAZOR_DIRECTION_DOWN, RAZOR_DIRECTION_LEFT, RAZOR_DIRECTION_RIGHT = range(4)

    #tear_image = None
    def __init__(self, _direction, _x, _y):
        print("Creating Tear")
        self.x = _x
        self.y = _y
        self.direction = _direction
        self.razor_image = load_image('../resource/Razor.png')
        self.damage = 2

        self.exist_count = 10

        self.ID = ID.RAZOR
        self.isEnd = False
    def draw(self):
        #Boy.line_image.clip_composite_draw(0, 0, 134, 43, math.atan2(Boy.MouseY - self.y, Boy.MouseX - self.x), '', (Boy.MouseX + self.x) / 2, (Boy.MouseY + self.y) / 2, math.sqrt((Boy.MouseX - self.x) ** 2 + (Boy.MouseY - self.y) ** 2), 2)
        
        GoalX, GoalY = 200, 200
        if self.direction == Razor.RAZOR_DIRECTION_UP:
            GoalX = self.x
            GoalY = 425
        elif self.direction == Razor.RAZOR_DIRECTION_DOWN:
            GoalX = self.x
            GoalY = 75
        elif self.direction == Razor.RAZOR_DIRECTION_LEFT:
            GoalX = 75
            GoalY = self.y
        elif self.direction == Razor.RAZOR_DIRECTION_RIGHT:
            GoalX = 725
            GoalY = self.y
        self.razor_image.clip_composite_draw(0, 0, 64, 128, math.atan2(GoalY - self.y, GoalX - self.x), '', (GoalX + self.x) / 2, (GoalY + self.y) / 2, math.sqrt((GoalX - self.x) ** 2 + (GoalY - self.y) ** 2), 2)
        #self.razor_image.clip_composite_draw(0, 0, 64, 64, math.atan2(425 - self.y,     0), '',             self.x,             (425 + self.y) / 2, math.sqrt((425 - self.y) ** 2), 2)
        # BB 그리기
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())


    def update(self):
        self.exist_count -= 1
        if self.exist_count < 0:
            self.isEnd = True

    def GetIsEnd(self):
        return self.isEnd
    def GetX(self):
        return self.x
    def GetY(self):
        return self.y
    def get_bb(self):
        if self.direction == Razor.RAZOR_DIRECTION_UP:
            return self.x - (RAZOR_IMAGE_SIZE / 4), self.y, self.x + (RAZOR_IMAGE_SIZE / 4), 425
        elif self.direction == Razor.RAZOR_DIRECTION_DOWN:
            return self.x - (RAZOR_IMAGE_SIZE / 4), 75, self.x + (RAZOR_IMAGE_SIZE / 4), self.y
        elif self.direction == Razor.RAZOR_DIRECTION_LEFT:
            return 75, self.y - (RAZOR_IMAGE_SIZE / 4), self.x, self.y + (RAZOR_IMAGE_SIZE / 4)
        elif self.direction == Razor.RAZOR_DIRECTION_RIGHT:
            return self.x, self.y - (RAZOR_IMAGE_SIZE / 4), 725, self.y + (RAZOR_IMAGE_SIZE / 4)
    def GetDamage(self):
        return self.damage

    def GetID(self):
        return self.ID