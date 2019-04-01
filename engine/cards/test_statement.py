from engine.cards.card import Card
from engine.cards.condition import Condition
from engine.cards.expression import Expression
from engine.cards.sticker import Sticker
from engine.cards.display import Display

# from card import Card
# from condition import Condition
# from expression import Expression
# from sticker import Sticker
# from display import Display

class TestStatement(Card):

    '''
    For information on card and attributes and methods, 
    refer parent class Card in card.py
    '''

    def __init__(self, card_number:int):
        card_id = "test_statement"
        card_type = [True, False, False, False, False, True, 0]
        super(TestStatement,self).__init__(card_id,card_type,card_number)
    
    def generate_card(self):
        self.card_dict["card_id"] = self.card_id
        self.card_dict["card_number"] = self.card_number
        self.card_dict["card_type"] = self.card_type
        self.card_dict["card_color"] = "color_logic"
        if_text = {
            "val_type":"text",
            "text":"if"
        }
        self.card_dict["display"] =[if_text]
        if bool(self.external_dependant):
            self.card_dict["external_dependant"] = self.external_dependant.generate_card()
        else:
            self.card_dict["external_dependant"] = {}
        if not self.children:
            self.card_dict["children"] = []

        return self.card_dict

    def generate_code(self, nesting_level = 0):
        nesting_level += 1
        if bool(self.external_dependant):
            self.code = "if" + self.external_dependant.generate_code() + ":\n"
        else:
            self.code = "if True:\n"
        for child in self.children:
            self.code += "    "*nesting_level
            self.code += child.generate_code(nesting_level)
        return self.code
    
    def set_external_dependant(self, condition:Condition):
        self.external_dependant = condition
        self.card_dict["external_dependant"] = self.external_dependant.generate_card()    

    def add_child(self,child, position):
        if position is None:
            self.children.append(child)
            self.card_dict["children"].append(child.generate_card())
        else:
            self.children.insert(position, child)
            self.card_dict["children"].insert(position, child.generate_card())

if __name__ == "__main__":
    test_card = TestStatement(0)

    print("Card: \n",test_card.generate_card())
    print("Code: \n",test_card.generate_code())

    test_card_ex1 = Expression([[("variable","count"),("operator", "+"),("number", "2")]],1)
    test_card_ex2 = Expression([[("variable","apple"),("operator", "-"),("number", "2")]],2)
    test_sticker = Sticker("conditional_operator","==")
    cond_list = [test_card_ex1,test_sticker,test_card_ex2]
    test_card_cond = Condition(cond_list,3)

    test_card_ch1 = Display(("text","Hello World!"), 0)
    test_card.add_child(test_card_ch1)
    test_card_ch2 = Display(("variable","count"), 0)
    test_card.add_child(test_card_ch2)

    test_card.set_external_dependant(test_card_cond)

    print("Card: \n",test_card.generate_card())
    print("Code: \n",test_card.generate_code())