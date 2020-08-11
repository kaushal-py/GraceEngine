from engine.cards.card import Card
from engine.cards.sticker import Sticker
from engine.cards.array_numbers import ArrayNumbers

# from card import Card
# from sticker import Sticker
# from array_numbers import ArrayNumbers

class ArraySetter(Card):

    '''
    For information on card and attributes and methods, 
    refer parent class Card in card.py
    '''

    def __init__(self, array_name:str, card_number:int):
        '''
        array_name : Name of array Variable
        '''

        card_id = "array_setter"
        card_type = [True,True, False, False, False, True, 0]
        super(ArraySetter, self).__init__(card_id, card_type, card_number)

        self.sticker_array = Sticker("Array",array_name)
    
    def generate_card(self):
        self.card_dict["card_id"] = self.card_id
        self.card_dict["card_number"] = self.card_number
        self.card_dict["card_type"] = self.card_type
        self.card_dict["card_color"] = "color_normal"

        set_text = {
            "val_type":"text",
            "text":"Set"
        }
        sticker_text = {
            "val_type": "sticker",
            "sticker_name": "array",
            "sticker_value": self.sticker_array.sticker_value
        }
        to_text = {
            "val_type": "text",
            "text": "to"
        }

        self.card_dict["display"] = [set_text, sticker_text, to_text]
        if bool(self.external_dependant):
            self.card_dict["external_dependant"] = self.external_dependant.generate_card()
        else:
            self.card_dict["external_dependant"] = {}
        self.card_dict["children"] = []
        
        return self.card_dict
    
    def set_external_dependant(self, array_card):
        self.external_dependant = array_card
        self.card_dict["external_dependant"] = self.external_dependant.generate_card()
    
    def generate_code(self, nesting_level = 0):
        self.code = self.sticker_array.sticker_value + " ="
        if bool(self.external_dependant):
            self.code += self.external_dependant.generate_code() + "\n"
        else:
            self.code += " None\n"
        return self.code

if __name__ == "__main__":
    
    test_card = ArraySetter("list_num", 0)
    print("Card: \n", test_card.generate_card())
    print("Code: \n", test_card.generate_code())
    test_card_numbers = ArrayNumbers([("number","1"),("number", "2"),("number", "3")],0)
    test_card.set_external_dependant(test_card_numbers)
    print("Card: \n", test_card.generate_card())
    print("Code: \n", test_card.generate_code())