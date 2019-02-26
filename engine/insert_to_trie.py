from trie import Trie
from spacy_parser import Parser
from anytree import Node

class TrieInsert:

    def insert_to_trie(natural_sentence:str):

        p = Parser()
        p.parse(natural_sentence)

        # preorder traversal of tokens
        tokens = p.preorder_traverse()
        filtered_sentence = p.remove_stopwords(tokens)

        root = Node("*")
        Trie.addNode(root,filtered_sentence,len(filtered_sentence),0)

if __name__ == "__main__":
    TrieInsert.insert_to_trie("Create a list of 10 integers")