from card import Card
from sticker import Sticker

class Condition(Card):

    def __init__(self, card_id:str, condition:str, card_number:int):
        card_type = [False, False, True, False, False, False, 2]
        cond_sticker = Sticker("condition",condition)
        self.condition = cond_sticker
        super(Condition, self).__init__(card_id, card_type, card_number)