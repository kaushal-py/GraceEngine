from card import Card
from expression import Expression
from display import Display
from sticker import Sticker
from condition import Condition

class WhileLoop(Card):
    
    '''
    For information on card and attributes and methods, 
    refer parent class Card in card.py
    '''

    def __init__(self, card_number:int):
        card_id = "while_loop"
        card_type = [] # TODO : complete this

        super(WhileLoop,self).__init__(card_id, card_type, card_number)

    def generate_card(self):
        self.card_dict["card_id"] = self.card_id
        self.card_dict["card_number"] = self.card_number
        self.card_dict["card_type"] = self.card_type
        self.card_dict["card_color"] = "color_loop"
        repeat_text = {
            "val_type":"text",
            "text":"repeat while"
        }
        self.card_dict["display"] =[repeat_text]
        if bool(self.external_dependant):
            self.card_dict["external_dependant"] = self.external_dependant.generate_card()
        else:
            self.card_dict["external_dependant"] = {}
        if not self.children:
            self.card_dict["children"] = []

        return self.card_dict
    
    def generate_code(self):
        if bool(self.external_dependant):
            self.code = "while" + self.external_dependant.generate_code() + ":<br>"
        else:
            self.code = "while True:<br>"
        for child in self.children:
            self.code += "&nbsp&nbsp" + child.generate_code()
        return self.code

    def set_external_dependant(self, condition):
        self.external_dependant = condition
        self.card_dict["external_dependant"] = self.external_dependant.generate_card()   
    
    def add_child(self, child):
        self.children.append(child)
        self.card_dict["children"].append(child.generate_card())

if __name__ == "__main__":
    test_card = WhileLoop(0)

    print("Card: \n",test_card.generate_card())
    print("Code: \n",test_card.generate_code())

    test_card_ex1 = Expression([("variable","count"),("operator", "+"),("number", "2")],1)
    test_card_ex2 = Expression([("variable","apple"),("operator", "-"),("number", "2")],2)
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