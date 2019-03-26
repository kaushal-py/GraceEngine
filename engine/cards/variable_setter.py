from engine.cards.card import Card
from engine.cards.sticker import Sticker
from engine.cards.expression import Expression

# from card import Card
# from sticker import Sticker
# from expression import Expression

class VariableSetter(Card):

    '''
    For information on card and attributes and methods, 
    refer parent class Card in card.py
    '''

    def __init__(self, variable_name:str, card_number:int):
        card_id = "variable_setter"
        card_type = [True,True, False, False, False, True, 0]
        super(VariableSetter, self).__init__(card_id, card_type, card_number)

        
        self.sticker_variable = Sticker("Variable",variable_name)
        self.code = ""

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
            "sticker_name": "variable",
            "sticker_value": self.sticker_variable.sticker_value
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
    
    def set_external_dependant(self, expression_card):
        self.external_dependant = expression_card
        self.card_dict["external_dependant"] = self.external_dependant.generate_card()
        self.has_expression = True
    

    def generate_code(self):
        self.code = self.sticker_variable.sticker_value + " ="
        if bool(self.external_dependant):
            self.code += self.external_dependant.generate_code() + "\n"
        else:
            self.code += " None\n"
        return self.code


if __name__ == "__main__":
    test_card = VariableSetter("count", 0)
    print("Card: \n", test_card.generate_card())
    print("Code: \n", test_card.generate_code())
    expression_card = Expression([("variable","count"),("operator", "+"),("number", "1")],1)
    test_card.set_external_dependant(expression_card)
    print("Card: \n", test_card.generate_card())
    print("Code: \n", test_card.generate_code())