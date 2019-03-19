from card import Card
from sticker import Sticker

class Condition(Card):

    def __init__(self, card_id:str, condition:Sticker, card_number:int):
        card_type = [False, False, True, False, False, False, 2]
        self.condition = condition
        super(Condition, self).__init__(card_id, card_type, card_number)