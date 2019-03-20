from cards.card import Card
from cards.sticker import Sticker

class Expression(Card):

    ''' This is will be the list of variables, numbers, operators '''
    expression = []
    def __init__(self, expression:str="", card_number:int=0):
        expression = expression.split()
        for item in expression:
            try:
                num = int(item)
                sticker_num = Sticker("number",num)
                self.expression.append(sticker_num)
            except:
                sticker_operator = Sticker("operator",item)
                self.expression.append(sticker_operator)

        card_id = "expression"
        card_type = [False, False, True, False, False, False, 0]
        super(Expression,self).__init__(card_id, card_type, card_number)
    
    def generate_card(self):
        self.card_dict["card_id"] = self.card_id
        self.card_dict["card_number"] = self.card_number
        self.card_dict["card_type"] = self.card_type
        self.card_dict["card_color"] = "color_math"
        self.card_dict["display"] = []
        for x in self.expression:
            sticker = {
                "val_type":"sticker",
                "sticker_name":x.sticker_type,
                "sticker_value":x.sticker_value
            }
            self.card_dict["display"].append(sticker)
        self.card_dict["external_dependant"] = {}
        self.card_dict["children"] = []

        return self.card_dict

if __name__ == "__main__":
    test_card = Expression("5 + 4",0)
    for item in test_card.expression:
        print(item.sticker_type, item.sticker_value,type(item))
    print(test_card.generate_card())

