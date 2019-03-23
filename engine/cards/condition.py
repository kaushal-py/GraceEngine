from card import Card
from sticker import Sticker
from expression import Expression

class Condition(Card):

    '''
    For information on card and attributes and methods, 
    refer parent class Card in card.py
    '''

    def __init__(self, condition_list:list, card_number:int):
        card_id = "condition"
        card_type = [False, False, True, False, False, False, 2]
        self.condition_list = condition_list
        super(Condition, self).__init__(card_id, card_type, card_number)
        self.condition_stickers = []
        self.set_internal_dependants()

    def set_internal_dependants(self):
        for item in self.condition_list:
            if isinstance(item, Sticker):
                self.condition_stickers.append(item)
            else:
                self.internal_dependants.append(item)

    def generate_card(self):
        self.card_dict["card_id"] = self.card_id
        self.card_dict["card_number"] = self.card_number
        self.card_dict["card_type"] = self.card_type
        self.card_dict["card_color"] = "color_logic"
        self.card_dict["display"] =[]
        for item in self.condition_list:
            if isinstance(item, Sticker):
                sticker_text = {
                    "val_type": "sticker",
                    "sticker_name": item.sticker_type,
                    "sticker_value": item.sticker_value
                }
                self.card_dict["display"].append(sticker_text)
            else:
                expression_text = {
                    "val_type":"internal_dependant",
                    "dependant" : item.generate_card()
                }
                self.card_dict["display"].append(expression_text)
        
        self.card_dict["external_dependant"] = {}
        self.card_dict["children"] = []

        return self.card_dict

    def generate_code(self):
        self.code = ""
        for item in self.condition_list:
            if isinstance(item, Sticker):
                self.code += " " + item.sticker_value
            else:
                self.code += item.generate_code()

        return self.code

if __name__ == "__main__":
    test_card_ex1 = Expression([("variable","count"),("operator", "+"),("number", "2")],1)
    test_card_ex2 = Expression([("variable","apple"),("operator", "-"),("number", "2")],2)
    test_sticker = Sticker("conditional_operator","==")
    cond_list = [test_card_ex1,test_sticker,test_card_ex2]
    test_card = Condition(cond_list,3)
    print(test_card.generate_card())
    print(test_card.generate_code())