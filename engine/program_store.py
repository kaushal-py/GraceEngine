'''
A module that maintains the state of the program. 
'''
import sys
from io import StringIO

from engine.cards.card import Card

class ProgramStore: 

    def __init__(self):

        self.variable_list = []

        self.new_card_number = 1
        self.current_card_number = 0
        self.root = Card("parent", [None], 0)
        self.current_position = -1
        self.current_neighbour = None

        #Parent stack, to go up levels
        self.parent_stack = [self.root]


    def insert_card(self, card):
        
        print("Current position: ", self.current_position)
        self.current_position += 1
        self.current_card_number = self.new_card_number
        self.new_card_number += 1

        # Add child to topmost element of parent stack
        self.parent_stack[-1].add_child(card, self.current_position)
        
    def insert_card_externally(self):
        self.current_card_number += 1
        self.new_card_number += 1


    def insert_external_dependant(self, card):
        
        # This parent is different from parent child.
        # Here parent means neighbour of external dependant class
        
        self.current_neighbour.set_external_dependant(card)
        self.current_card_number = self.new_card_number
        self.new_card_number += 1
        
    
    def temp_external_dependant(self, card):
        current_card = self.get_card_by_number(self.new_card_number-1)
        current_card.set_external_dependant(card)
    
    # def get_current_card(self):
    #     # current parent and current position can give current card
    #     print(self.parent_stack[-1].card_id)
    #     print(self.current_position)
    #     return self.parent_stack[-1].children[self.current_position]

    def push_parent(self, card):
        self.current_parent_card = card
        self.parent_stack.append(self.current_parent_card)
    
    def pop_parent(self):
        if len(self.parent_stack) > 1:
            self.parent_stack.pop()
            self.current_parent_card = self.parent_stack[-1]

    def get_card_by_number(self, num, card_root):
        for card in card_root.children:
            if card.card_number == num:
                return card
            elif card.external_dependant is not None and card.external_dependant.card_number == num:
                return card
            for dep_card in card.internal_dependants:
                if dep_card.card_number == num:
                    return dep_card
            if len(card.children) != 0:
                return self.get_card_by_number(num,card)
        
        return None
    
    def goto_card_by_number(self, num, card_root):

        if card_root == self.root:
            self.parent_stack = []

        self.push_parent(card_root)

        for k, card in enumerate(card_root.children):
            
            if card.card_number == num:
                self.current_card_number = card.card_number
                self.current_neighbour = card
                return k, card

            elif card.external_dependant is not None and card.external_dependant.card_number == num:
                self.current_card_number = card.card_number
                self.current_neighbour = card
                self.push_parent(card)
                return k, card

            for dep_card in card.internal_dependants:
                if dep_card.card_number == num:
                    return dep_card

            if len(card.children) != 0:
                return self.goto_card_by_number(num, card)
        
        self.pop_parent()
        return None, None
    
    # delete card
    def delete_card_by_number(self, num):

        current_position, card = self.goto_card_by_number(num, self.root)
        del self.parent_stack[-1].children[current_position]
        self.current_position = current_position - 1
        self.current_card_number = self.parent_stack[-1].children[current_position].card_number
        
    

    def print_stack(self):
        print("+++Parent stack+++")
        for card in self.parent_stack:
            print(card.card_id)
        print("++++++")


    def generate_program(self):
        
        program_dict = {
            "program": [],
            "inserted_card_number" : self.new_card_number - 1,
            "current_card_number" : self.current_card_number,
        }

        for card in self.root.children:
            program_dict["program"].append(card.generate_card())
        
        return program_dict


    def generate_code(self):

        code_dict = {"code": ""}

        for card in self.root.children:
            code_dict["code"] += card.generate_code()
 
        return code_dict
    

    def generate_output(self):

        code_string = self.generate_code()["code"]

        # create file-like string to capture output
        codeOut = StringIO()
        codeErr = StringIO()

        # capture output and errors
        sys.stdout = codeOut
        sys.stderr = codeErr

        exec(code_string)

        # restore stdout and stderr
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        s_error = codeErr.getvalue()
        s_out = codeOut.getvalue()

        output_string = s_out + '\n' + s_error

        codeOut.close()
        codeErr.close()

        output_dict = {"output" : output_string}

        return output_dict
