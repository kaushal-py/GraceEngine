from engine.cards.card import Card
from engine.cards.sticker import Sticker

# from card import Card
# from sticker import Sticker

class ArrayNumbers(Card):

    '''
    For information on card and attributes and methods, 
    refer parent class Card in card.py
    '''

    def __init__(self, number_list:list, card_number:int):
        '''
        number_list : list of tuples (sticker_type, sticker_value)
            sticker_type : "number"
            sticker_value : "/some_number/"
        '''
        card_id = "array_numbers"
        card_type = [False, False, True, False, False, False, 0]
        super(ArrayNumbers, self).__init__(card_id, card_type, card_number)

        self.number_list = []
        for item in number_list:
            (sticker_type, sticker_value) = item
            sticker =Sticker(sticker_type,sticker_value)
            self.number_list.append(sticker)
    
    def generate_card(self):
        self.card_dict["card_id"] = self.card_id
        self.card_dict["card_number"] = self.card_number
        self.card_dict["card_type"] = self.card_type
        self.card_dict["card_color"] = "color_math"
        self.card_dict["display"] = [{
            "val_type":"text",
            "text":"["
        }]
        for x in self.number_list:
            sticker = {
                "val_type":"sticker",
                "sticker_name":x.sticker_type,
                "sticker_value":x.sticker_value
            }
            comma = {
                "val_type":"text",
                "text":","
            }
            self.card_dict["display"].append(sticker)
            self.card_dict["display"].append(comma)
        self.card_dict["display"].append({
            "val_type":"text",
            "text":"]"
        })
        self.card_dict["external_dependant"] = {}
        self.card_dict["children"] = []

        return self.card_dict
    
    def generate_code(self, nesting_level = 0):
        self.code = " [ "
        if self.number_list == []:
            self.code += "]"
            return None
        self.code += self.number_list[0].sticker_value
        for i, item in enumerate(self.number_list):
            if i == 0:
                continue
            self.code += ", " + item.sticker_value
        self.code += " ]"
        return self.code

if __name__ == "__main__":
    test_card = ArrayNumbers([("number","1"),("number", "2"),("number", "3")],0)
    for item in test_card.number_list:
        print(item.sticker_type, item.sticker_value,type(item))
    print("Card: \n",test_card.generate_card())
    print("Code: \n",test_card.generate_code())
