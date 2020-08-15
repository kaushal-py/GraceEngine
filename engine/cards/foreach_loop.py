from engine.cards.card import Card
from engine.cards.display import Display
from engine.cards.sticker import Sticker

# from card import Card
# from display import Display
# from sticker import Sticker

class ForeachLoop(Card):
    
    '''
    For information on card and attributes and methods, 
    refer parent class Card in card.py
    '''

    def __init__(self, array_sticker:tuple ,card_number:int):
        card_id = "foreach_loop"
        card_type = [True, False, False, False, False, True, 0]
        super(ForeachLoop,self).__init__(card_id, card_type, card_number)

        (sticker_type,sticker_value) = array_sticker
        self.array_sticker = Sticker(sticker_type, sticker_value)

    def generate_card(self):
        self.card_dict["card_id"] = self.card_id
        self.card_dict["card_number"] = self.card_number
        self.card_dict["card_type"] = self.card_type
        self.card_dict["card_color"] = "color_loop"
        foreach_text = {
            "val_type":"text",
            "text":"for each"
        }
        loop_variable = {
            "val_type":"sticker",
            "sticker_name":"variable",
            "sticker_value":"item"
        }
        in_text = {
            "val_type":"text",
            "text":"in"
        }
        array_variable = {
            "val_type":"sticker",
            "sticker_name": self.array_sticker.sticker_type,
            "sticker_value": self.array_sticker.sticker_value
        }
        self.card_dict["display"] = [foreach_text, loop_variable, in_text, array_variable]
        
        self.card_dict["external_dependant"] = {}
        
        if not self.children:
            self.card_dict["children"] = []

        return self.card_dict
    
    def generate_code(self, nesting_level = 0):
        nesting_level += 1
        self.code = "for item in " + self.array_sticker.sticker_value + ":\n"
        if not self.children:
            self.code += "    " * nesting_level
            self.code += "pass"
        else:
            for child in self.children:
                self.code += "    " * nesting_level 
                self.code += child.generate_code(nesting_level)
        return self.code
    
    def add_child(self, child, position):
        if position is None:
            self.children.append(child)
            self.card_dict["children"].append(child.generate_card())
        else:
            self.children.insert(position, child)
            self.card_dict["children"].insert(position, child.generate_card())

if __name__ == "__main__":
    test_card = ForeachLoop(("Array","array_name"),0)
    print(test_card.generate_card())
    print(test_card.generate_code())

    test_card_display = Display(("variable","item"), 1)
    test_card.add_child(test_card_display,None)
    print(test_card.generate_card())
    print(test_card.generate_code())