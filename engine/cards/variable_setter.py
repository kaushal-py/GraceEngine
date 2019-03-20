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
    
    def set_expression(self, expression:str, card_number):
        self.expression_card = Expression(expression, card_number)
        self.card_dict["external_dependant"] = self.expression_card.generate_card()


if __name__ == "__main__":
    test_card = VariableSetter("count", 0)
    print(test_card.generate_card())
    test_card.set_expression("5 + 4", 1)
    print(test_card.sticker_variable.sticker_value, end=' = ')
    for item in test_card.expression_card.expression:
        print(item.sticker_value, end = ' ')
    print()
    print(test_card.generate_card())
