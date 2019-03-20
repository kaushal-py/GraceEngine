from trie import Trie
from parser import Parser
from expression_parser import ExpressionParser
from anytree import Node
from anytree.importer import JsonImporter
from anytree.exporter import JsonExporter

class Driver:

    def __init__(self, tree_name=""):

        ''' 
            Tree is either already created and imported through json 
            or it is created newly
        '''

        # if tree_name == "":
        #     self.root = Node("*")
        # else:
        #     self.root = self.get_tree(tree_name)
        tree_name = 'engine/trie_disk.json'
        self.root = self.get_tree(tree_name)
        

    def drive(self, natural_sentence:str):

        '''
            This function receives a natural sentence 
            and inserts it to the tree and store it to the json file
        '''

        p = Parser()
        t = Trie()
        e = ExpressionParser()

        d = {}       
        command_type,command,d = p.parse(natural_sentence)
        if command_type != "unknown" and command_type != "create":
            # print(len(command))
            code = t.traverseTree(self.root,command,len(command),0)
            print("Command Type: ",command_type)
            print("Command: ",command)
            print("Sticker Type, Variable: ",d)
            if code[0] is not None:
                #TODO: Code to create card
                print("Card ID: ",code[0])
            elif code[1] is not None:
                print("Suggestions: ",code[1])
            print("----------------------------------------------------------------")

        elif command_type == "create":
            print("Variable has been created")
            print("----------------------------------------------------------------")

        else:
            print("Command Type: ",command_type)
            print("Command:", command)
            exp_tuples = e.parseExpression(command)
            print("Expression List : ",exp_tuples)
            print("----------------------------------------------------------------")

        # t.showTree(self.root)

        # exporter = JsonExporter(indent=4, sort_keys=True)
        # file_data = exporter.export(self.root)

        # tree_file = open("trie.json", "w")
        # tree_file.write(file_data)
        # tree_file.close()

    def get_tree(self, file_name):

        ''' This function is used to import json file and return anytree Node '''
        importer = JsonImporter()
        tree_file = open(file_name, "r")
        data = tree_file.read()
        tree_file.close()
        return importer.import_(data)

if __name__ == "__main__":
    d = Driver()
    d.drive("Create variable temperature")
    d.drive("Set")
    d.drive("Set the")
    d.drive("Set the variable")
    d.drive("Set the variable temperature to")
    d.drive("the number 20")
    d.drive("Set the variable temperature to")
    d.drive("the variable temperature plus the number 10")
    d.drive("if")
    d.drive("the variable temperature is less than the number 25")
    d.drive("else")