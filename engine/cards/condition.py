from card import Card

class Condition(Card):

    def __init__(self,card_id, card_type, condition):
        self.condition = condition #TODO: Make this sticker
        super().__init__(card_id, card_type)