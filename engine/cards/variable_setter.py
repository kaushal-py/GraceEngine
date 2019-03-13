from card import Card
from sticker import Sticker

class VariableSetter(Card):

    def __init__(self, variable_name:str):
        card_id = "variable_setter"
        card_type=[True,True,True,False,0,False] #TODO: verify this
        super(VariableSetter, self).__init__(card_id, card_type)

        stick_variable_name = Sticker("Variable",variable_name) # TODO: Not sure how to pass sticker type
        # stick_variable_value = Sticker("Value",variable_value) # TODO: Object Expression
        self.variable_name = stick_variable_name
        # self.variable_value = stick_variable_value
    

    def generate_card(self, card_number):

        card_dict = {}
        card_dict["card_type"] = self.card_id
        card_dict["card_number"] = card_number

        set_text = {
            "val_type":"text",
            "text":"Set"
        }
        sticker_text = {
            "val_type": "sticker",
            "sticker_name": "variable",
            "sticker_value": self.variable_name
        }
        to_text = {
            "val_type": "text",
            "text": "to"
        }

        card_dict["values"] = [set_text, sticker_text, to_text]

        return card_dict


if __name__ == "__main__":
    test_card = VariableSetter("count")
    print(test_card.generate_card(1))