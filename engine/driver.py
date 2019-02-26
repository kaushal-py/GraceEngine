from trie import Trie
from spacy_parser import Parser
from anytree import Node

class Driver:

    def drive(natural_sentence:str):

        p = Parser()
        p.parse(natural_sentence)

        # preorder traversal of tokens
        tokens = p.preorder_traverse()
        filtered_sentence = p.remove_stopwords(tokens)

        root = Node("*")
        t=Trie()
        t.addNode(root,filtered_sentence,len(filtered_sentence),0)
        t.showTree(root)


if __name__ == "__main__":
    Driver.drive("Create a list of 10 integers")