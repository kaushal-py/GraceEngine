import sys
from engine.trie import Trie
from engine.parser import Parser
from engine.expression_parser import ExpressionParser
from engine.demo_driver import Driver
from anytree import Node
from anytree.importer import JsonImporter
from anytree.exporter import JsonExporter

p = Parser()
t = Trie()
e = ExpressionParser()
dr = Driver()

class Suggestions:

    def __init__(self, tree_name=""):
        tree_name = 'engine/trie_disk.json'
        self.root = dr.get_tree(tree_name)

    def suggest(self, query:str):
        
        d = {}
        command_type,command,d = p.parse(query)
        if command_type != "unknown" and command_type != "create":
            code = t.traverseTree(self.root,command,len(command),0)
            if code[0] is not None:
                print("Card ID: ",code[0])
            elif code[1] is not None:
                # print("Suggestions: ",code[1])
                return code[1]

        elif command_type == "create":
            print("Variable has been created")
            # print("----------------------------------------------------------------")

        else:
            # print("Command Type: ",command_type)
            # print("Command:", command)
            exp_tuples = e.parseExpression(command)
            # print("Expression List : ",exp_tuples)
            # print("----------------------------------------------------------------")

        return ""
    
if __name__ == "__main__":
    s = Suggestions()
    s.suggest("set")