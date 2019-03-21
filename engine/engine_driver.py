import sys

from anytree import Node
from anytree.importer import JsonImporter
from anytree.exporter import JsonExporter

# Loacal modules
sys.path.insert(0, '../')
from engine.trie import Trie
from engine.parser import Parser
from engine.expression_parser import ExpressionParser

from engine.program_store import ProgramStore

from engine.cards.variable_setter import VariableSetter
from engine.cards.expression import Expression


class Driver:


    def __init__(self, tree_name="engine/trie_disk.json"):
        ''' 
        Tree is either already created and imported through json 
        or it is created newly
        '''
        self.root = self.get_tree(tree_name)

        # initialise all parsers.
        self.p = Parser()
        self.t = Trie()
        self.e = ExpressionParser()

        # initialise program store
        self.store = ProgramStore()
        


    def update_state(self, natural_sentence:str):
        '''
        This function receives a natural sentence 
        and inserts it to the tree and store it to the json file
        '''
        # dictionary for storing stickers
        d = {}

        # parse the natural sentence
        command_type,command,d = self.p.parse(natural_sentence)


        if command_type != "unknown" and command_type != "create":

            # parse through the trie
            code = self.t.traverseTree(self.root,command,len(command),0)

            print("+"*10)
            print(code[0], code[1])
            print(command)

            ### Terminal and leaf of trie ###
            # Generate card and add to program 
            if code[0] is not None and code[1] is None:

                if code[0] == "variable_setter":

                    c = VariableSetter(d["sticker_value"], self.store.current_card_number)
                    self.store.insert_card(c)


            ### Terminal but not leaf ###
            # Undecidable whether to create card or not
            elif code[0] is not None and code[1] is not None:
                print("Undecidable")
                pass

            
            ### Non-terminal and not leaf ###
            # Returns a suggestion
            elif code[1] is not None:
                pass
                print("Suggestions: ",code[1])
                

        elif command_type == "create":
            self.store.variable_list.append(d["variable_name"])

        else:
            (exp_tuples, isComplete) = self.e.parseExpression(command)
            if isComplete:
                c = Expression(exp_tuples, self.store.current_card_number)
                self.store.insert_external_dependant(c)

    

    def get_program(self):
        return self.store.generate_program()
    



    def get_code(self):
        return self.store.generate_code()
            
            

    def get_tree(self, file_name):
        ''' 
        This function is used to import json file and return anytree Node 
        '''
        importer = JsonImporter()
        tree_file = open(file_name, "r")
        data = tree_file.read()
        tree_file.close()
        return importer.import_(data)


if __name__ == "__main__":
    d = Driver(tree_name="../engine/trie_disk.json")
    d.update_state("Set")
    d.update_state("Set the")
    d.update_state("Set the variable")
    d.update_state("Set the variable temp")
    d.update_state("Set the variable temp to")
    # d.update_state("Create variable temperature")
    # d.update_state("Set the variable temperature to")
    # d.drive("the number 20")
    # d.drive("Set the variable temperature to")
    # d.update_state("the variable temperature plus 10")

    print(d.store.generate_program())

    d.update_state("number")
    d.update_state("number 10")
    d.update_state("number 10 plus")
    d.update_state("number 10 plus number 20 minus number 30 grace")

    print(d.store.generate_program())

