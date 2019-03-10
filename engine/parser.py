'''
This file will receive a natural sentense. It does the following
1. Converts to lowercase
2. Remove stopwords
3. Identify the command type - insert, modify, delete, navigate
4. Identify the stickers
5. Return to driver
'''

import spacy
import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
import csv

class Parser:

    def __init__(self):
        
        print("Loading model..")
        self.nlp = spacy.load('en_core_web_sm')
        self.doc= None
        print("Model loaded")

    def parse(self,sentence):
        
        '''Convert to lower case'''
        self.sent = sentence.lower()

        '''Tokenise the sentence'''
        tokens = nltk.word_tokenize(self.sent)

        # TODO: Create the logic according to various speaking styles
        '''List of types of operations'''
        CREATE = ["create"]
        INSERT = ["modify","set","test"]

        if tokens[0] in CREATE:
            command_type = "create"
        elif tokens[0] in INSERT:
            command_type = "insert"
        else:
            command_type = "expression"
            return command_type,tokens,None

        '''Remove Stopwords'''
        stop_words = set(stopwords.words('english'))
        # TODO: Find a proper list of stopwords
        stop_words.remove("for")
        stop_words.remove("if")
        stop_words.remove("not")
        stop_words.remove("to")
        self.filtered_sentence = [w for w in tokens if not w in stop_words]
        # print(self.filtered_sentence)
        

        # TODO: Identify the position of 'variable' and find the variable for Multiple variables
        if "variable" in self.filtered_sentence:
            var_index = self.filtered_sentence.index("variable")+1
            # print("var index = ",var_index)
        
        current_variable = self.filtered_sentence[var_index]
        command = []


        if command_type == 'create':
            if self.filtered_sentence[1] == "variable":
                '''
                    Put the variables in a bucket of variables
                '''
                with open("variable_bucket.csv","w+") as var_bucket:
                    var_bucket_writer = csv.writer(var_bucket, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    var_bucket_writer.writerow([self.filtered_sentence[2]])

            '''
                Return the command and variable
            '''
            # print(self.filtered_sentence)
            command = [w for w in self.filtered_sentence if not w in stop_words and w != current_variable]
            return command_type,command,None


        elif command_type == 'insert':
            
            if self.filtered_sentence[0] == "set":
                
                '''Create the command list'''
                for i,token in enumerate(self.filtered_sentence):
                    if i < var_index:
                        command.append(token)
                
                d = dict()
                d["sticker_type"] = "variable"
                d["sticker_value"] = current_variable
                # print(command_type,command,d)
                return command_type,command,d
            
            elif self.filtered_sentence[0] == "test":
                #TODO: Find a way to return "test", then accept the expression(condition)
                #  and then get back to the test card for ifTrue and ifFales value
                pass

        elif command_type == 'delete':
            pass


        elif command_type == 'navigate':
            pass


        else:
            print("Unknown")
            return None