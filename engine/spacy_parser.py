import spacy
from nltk.corpus import wordnet

class Parser:

    def __init__(self):
        
        print("Loading model..")
        self.nlp = spacy.load('en_core_web_sm')
        self.doc= None
        print("Model loaded")
    

    def parse(self, sentences):

        # single line statement which does tokenising,
        # lexical analysis and parsing
        self.doc = self.nlp(sentences)
        self.sents = list(self.doc.sents)
    
    def get_sent_root(self, pos=0):
        return self.sents[pos].root


    def return_tokens(self, pos=0):
        
        # creates a list of all the tokens and returns the list
        tokens = [token for token in self.sents[pos]]
        return tokens


    def return_noun_chunks(self, pos=0):
        
        # creaes a list of noun chunks and returns the list
        noun_chunks = [chunk for chunk in self.sents[pos].noun_chunks]
        return noun_chunks


    def preorder_util(self, root):

        if root is not None:
            #print(root.text)
            self.process_node(root)
            for left in root.lefts:
                self.preorder_util(left)
            for right in root.rights:
                self.preorder_util(right)

    
    def preorder_traverse(self, pos=0):
        root = self.get_sent_root(pos)
        self.preorder_util(root)


    def process_node(self, node):
        syns= wordnet.synsets(node.text)
        
        synonyms = set()

        print("\n++", node.text, "++")

        for word in syns:
            for l in word.lemmas():
                synonyms.add(l.name())
        
        print(synonyms)
            

if __name__ == "__main__":

    p=Parser()
    p.parse("Display the value of apple")

    print(p.return_tokens())
    print(p.return_noun_chunks())
    p.preorder_traverse()