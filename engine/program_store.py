'''
A module that maintains the state of the program. 
'''

class ProgramStore: 

    def __init__(self):

        self.variable_list = []
        self.card_list = []

        self.current_card_number = 1
    

    def insert_card(self, card):
        
        self.current_card_number += 1
        self.card_list.append(card)
        
    

    def insert_external_dependant(self, card):
        
        current_card = self.get_card_by_number(self.current_card_number-1)
        current_card.set_external_dependant(card)
        self.current_card_number += 1

    def get_card_by_number(self, num):

        for card in self.card_list:

            if card.card_number == num:
                return card
            elif card.get_external_dependant() is not None and card.get_external_dependant().card_number == num:
                return card
            for dep_card in card.get_internal_dependants():
                if dep_card.card_number == num:
                    return dep_card
            
            for dep_card in card.get_children():
                if dep_card.card_number == num:
                    return dep_card
        
        return None
    

    def generate_program(self):
        
        program_dict = {"program": []}

        for card in self.card_list:
            program_dict["program"].append(card.generate_card())
        
        return program_dict


    def generate_code(self):

        code_dict = {"code": ""}

        for card in self.card_list:
            code_dict["code"] += card.generate_code()
        
        return code_dict
