from trie import Trie
from parser import Parser
from anytree import Node
from anytree.importer import JsonImporter
from anytree.exporter import JsonExporter

class Driver:

    def __init__(self, tree_name=""):

        ''' 
            Tree is either already created and imported through json 
            or it is created newly
        '''

        if tree_name == "":
            self.root = Node("*")
        else:
            self.root = self.get_tree(tree_name)

    def drive(self, natural_sentence:str):

        '''
            This function receives a natural sentence 
            and inserts it to the tree and store it to the json file
        '''

        p = Parser()
        

        t=Trie()
        d = dict()        
        command_type,command,d = p.parse(natural_sentence)
        if command_type != "expression":
            t.traverseTree(self.root,command,len(command),0)
            t.showTree(self.root)

        exporter = JsonExporter(indent=4, sort_keys=True)
        file_data = exporter.export(self.root)

        tree_file = open("trie.json", "w")
        tree_file.write(file_data)
        tree_file.close()

    def get_tree(self, file_name):

        ''' This function is used to import json file and return anytree Node '''
        importer = JsonImporter()
        tree_file = open(file_name, "r")
        data = tree_file.read()
        tree_file.close()
        return importer.import_(data)

if __name__ == "__main__":
    trie = Driver()
    trie.drive("Create variable temperature")
    trie.drive("Set the variable temperature to")
    trie.drive("the number 20")
    trie.drive("Set the variable temperature to")
    trie.drive("the expression temperature plus 10")