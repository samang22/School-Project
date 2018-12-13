from pico2d import *
import config
import ID
import game_framework

class Item:
    HEART = 0
    BOOM = 1
    KEY = 2
    TEAR = 3
    TRIPLE = 4
    RAZOR = 5    

    ITEM_SIZE = 32

    def __init__(self, _id, _x, _y):
        print("Creating Tear")
        self.x = _x
        self.y = _y

        self.heart_image = load_image('../resource/Heart_Item.png')
        self.boom_image = load_image('../resource/Boom_Item.png')
        self.key_image = load_image('../resource/Key_Item.png')
        self.tear_image = load_image('../resource/Tear_Item.png')
        self.triple_image = load_image('../resource/Triple_Item.png')
        self.razor_image = load_image('../resource/Razor_Item.png')

        self.item_id = _id
        self.ID = ID.ITEM
        self.isExposed = False
        self.isEnd = False
    def draw(self):
        if self.isExposed:
            if Item.HEART == self.item_id:
                self.heart_image.clip_draw(0, 0, Item.ITEM_SIZE, Item.ITEM_SIZE, self.x, self.y)
            elif Item.BOOM == self.item_id:
                self.boom_image.clip_draw(0, 0, Item.ITEM_SIZE, Item.ITEM_SIZE, self.x, self.y)
            elif Item.KEY == self.item_id:
                self.key_image.clip_draw(0, 0, Item.ITEM_SIZE, Item.ITEM_SIZE, self.x, self.y)
            elif Item.TEAR == self.item_id:
                self.tear_image.clip_draw(0, 0, Item.ITEM_SIZE, Item.ITEM_SIZE, self.x, self.y)
            elif Item.TRIPLE == self.item_id:
                self.triple_image.clip_draw(0, 0, Item.ITEM_SIZE, Item.ITEM_SIZE, self.x, self.y)
            elif Item.RAZOR == self.item_id:
                self.razor_image.clip_draw(0, 0, Item.ITEM_SIZE, Item.ITEM_SIZE, self.x, self.y)
            
        # BB 그리기
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())


    def update(self):
        pass

    def GetX(self):
        return self.x

    def GetY(self):
        return self.y

    def get_bb(self):
        if self.isExposed:
            return self.x - (Item.ITEM_SIZE / 2), self.y - (Item.ITEM_SIZE / 2), self.x + (Item.ITEM_SIZE / 2), self.y + (Item.ITEM_SIZE / 2)
        else:
            return 0, 0, 0, 0
    def SetEnd(self):
        self.isEnd = True
    def SetExposed(self):
        self.isExposed = True
    def GetIsEnd(self):
        return self.isEnd

    def GetID(self):
        return self.ID
    def GetItemID(self):
        return self.item_id
