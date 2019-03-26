'''
A module that maintains the state of the program. 
'''
from engine.cards.card import Card

class ProgramStore: 

    def __init__(self):

        self.variable_list = []

        self.current_card_number = 1
        self.root = Card("parent", [None], 0)
        self.current_parent_card = self.root

        #Parent stack, to go up levels
        self.parent_stack = [self.root]


    def insert_card(self, card):
        
        self.current_card_number += 1
        self.current_parent_card.add_child(card)
        
    def insert_card_externally(self):
        self.current_card_number += 1


    def insert_external_dependant(self, card, card_parent=None):
        
        # This parent is different from parent child.
        # Here parent means neighbour of external dependant class
        if card_parent:
            current_card = card_parent
        else:
            current_card = self.get_card_by_number(self.current_card_number-1)
        
        current_card.set_external_dependant(card)
        self.current_card_number += 1
    
    def temp_external_dependant(self, card):
        current_card = self.get_card_by_number(self.current_card_number-1)
        current_card.set_external_dependant(card)
    

    def set_parent(self, card):
        self.current_parent_card = card

    def get_card_by_number(self, num):

        for card in self.root.children:
            
            if card.card_number == num:
                return card
            elif card.external_dependant is not None and card.external_dependant.card_number == num:
                return card
            for dep_card in card.internal_dependants:
                if dep_card.card_number == num:
                    return dep_card
            
            for dep_card in card.children:
                if dep_card.card_number == num:
                    return dep_card
        
        return None
    

    def generate_program(self):
        
        program_dict = {"program": []}

        for card in self.root.children:
            program_dict["program"].append(card.generate_card())
        
        return program_dict


    def generate_code(self):

        code_dict = {"code": ""}

        for card in self.root.children:
            code_dict["code"] += card.generate_code()
 
        return code_dict
