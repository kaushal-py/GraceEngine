from card import Card
from sticker import Sticker

class VariableSetter(Card):

    def __init__(self, variable_name:str, variable_value):
        card_id = "variable_setter"
        card_type=[True,True,True,False,0,False] #TODO: verify this
        super(VariableSetter, self).__init__(card_id, card_type)

        stick_variable_name = Sticker("Variable",variable_name) # TODO: Not sure how to pass sticker type
        stick_variable_value = Sticker("Value",variable_value) # TODO: Object Expression
        self.variable_name = stick_variable_name
        self.variable_value = stick_variable_value

if __name__ == "__main__":
    test_card = VariableSetter("count",10)
    print(test_card.card_id)