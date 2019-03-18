from trie import Trie
from parser import Parser
from cards.variable_setter import VariableSetter

from anytree import Node
from anytree.importer import JsonImporter
from anytree.exporter import JsonExporter

class Driver:

    def __init__(self, tree_name="trie_disk.json"):

        ''' 
            Tree is either already created and imported through json 
            or it is created newly
        '''
        self.root = self.get_tree(tree_name)
        

    def drive(self, natural_sentence:str):

        '''
            This function receives a natural sentence 
            and inserts it to the tree and store it to the json file
        '''

        p = Parser()
        t=Trie()

        d = {}       
        command_type,command,d = p.parse(natural_sentence)
        if command_type != "expression":
            code = t.traverseTree(self.root,command,len(command),0)

            if code == "variable_setter":
                v = VariableSetter(d["sticker_value"],0)
                print(v.generate_code())
        else:
            print("Command:", command)


if __name__ == "__main__":
    d = Driver()
    # d.drive("Create variable temperature")
    d.drive("Set the variable temperature to")
    # d.drive("the number 20")
    # d.drive("Set the variable temperature to")
    # d.drive("the expression temperature plus 10")