from cards.card import Card
from cards.sticker import Sticker
from cards.expression import Expression

class VariableSetter(Card):

    def __init__(self, variable_name:str, card_number:int):
        card_id = "variable_setter"
        card_type = [True,True, False, False, False, True, 0]
        super(VariableSetter, self).__init__(card_id, card_type, card_number)

        
        self.sticker_variable = Sticker("Variable",variable_name)
        self.expression_card = Expression()
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
            "sticker_value": self.sticker_variable.sticker_type
        }
        to_text = {
            "val_type": "text",
            "text": "to"
        }

        self.card_dict["display"] = [set_text, sticker_text, to_text]
        self.card_dict["external_dependant"] = self.expression_card.generate_card()
        self.card_dict["children"] = []
        
        return self.card_dict
    
    def set_expression(self, expression:list, card_number:int):
        self.expression_card = Expression(expression, card_number)
        self.card_dict["external_dependant"] = self.expression_card.generate_card()
    
    def generate_code(self):
        self.code = self.sticker_variable.sticker_value + " ="
        if self.expression_card.generate_code():
            self.code += self.expression_card.generate_code()
        else:
            self.code += " None"
        return self.code


if __name__ == "__main__":
    test_card = VariableSetter("count", 0)
    print("Card: \n", test_card.generate_card())
    print("Code: \n", test_card.generate_code())
    test_card.set_expression([("variable","count"),("operator", "+"),("number", "1")], 1)
    print("Card: \n", test_card.generate_card())
    print("Code: \n", test_card.generate_code())