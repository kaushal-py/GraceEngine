import re

class Card:

    def __init__(self, id, ctype):
        
        '''
        Each card has a ID and a Type.
        ID is unique number for each card.

        == Card types ==
        1. Top Tape - TT
        2. Bottom Tape - BT
        3. Right Punch - RP
        4. Left Punch - LP
        5. Left Inner Punch (along with count) - xLIP
        6. Nested Tape - NT

        A card can be any combination of these types.
        Suppose a card has multiple types, it can be specified by using '-'.
        For example: 
        If the card has a top and a bottom tape and a right punch and 3 Left inner punches,
        the type of the card will be "TT-BT-RP-3LIP".
        
        The order of the types is specified using the priority specified in the above list.
        '''

        self.id = id
        self.ctype = ctype

        self.stickers = {}

        self.card_links = {}


    def __validate_and_set_type(self):

        ctype_list = self.ctype.split('-')
        valid_list=["TT","BT","RP","LP","LIP","NT"]

        #TODO: Write RE to verify correctness of type.



    '''
    Getter and setter methods for the stickers of the card
    '''
    def set_sticker_val(self, sticker_key, sticker_val):
        self.stickers[sticker_key] = sticker_val

    def get_sticker_val(self, sticker_key):
        return self.stickers[sticker_key]
    

    '''
    Getter and setter methods to update the card links. 
    This is used to combine cards to create a complete program.
    '''
    def set_card_link(self, ctype, card_link):

        assert isinstance(card_link, Card)
        self.card_links[ctype] = card_link
    
    def get_card_link(self, ctype):
        return self.card_links[ctype]
    
    

if __name__ == "__main__":
    c = Card("Variable_setter", "Hello")




        
    