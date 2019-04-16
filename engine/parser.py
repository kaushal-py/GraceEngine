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
import csv

class Parser:

    def __init__(self):
        
        ### Spacy models not required
        # print("Loading model..")
        # self.nlp = spacy.load('en_core_web_sm')
        # self.doc= None
        # print("Model loaded")
        self.stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
        '''Remove Stopwords'''
        # TODO: Find a proper list of stopwords
        self.stop_words.remove("for")
        self.stop_words.remove("if")
        self.stop_words.remove("not")
        self.stop_words.remove("to")
        self.stop_words.remove("while")

    def parse(self,sentence):
        
        '''Convert to lower case'''
        self.sent = sentence.lower()

        '''Tokenise the sentence'''
        tokens = nltk.word_tokenize(self.sent)

        # TODO: Create the logic according to various speaking styles
        '''List of types of operations'''
        CREATE = ["create"]
        INSERT = ["modify","set","test","if","print","repeat"]
        NAVIGATE = ["end", "go"]

        '''List of keywords'''
        KEYWORDS = ["variable","expression","text"]

        
        if tokens[0] in CREATE:
            command_type = "create"
        elif tokens[0] in INSERT:
            command_type = "insert"
        elif tokens[0] in NAVIGATE:
            command_type = "navigate"
        else:
            command_type = "unknown"
            return command_type,tokens,None

        self.filtered_sentence = [w for w in tokens if not w in self.stop_words]
        # print(self.filtered_sentence)
        
        
        command = []

        if command_type == 'create':
            
            if self.filtered_sentence[1] == "variable":
                '''
                    Put the variables in a bucket of variables
                '''
                ''' 
                Deprecated : Use of csv to store the variables.
                The variables are now stored in the program object.
                '''
                # with open("engine/variable_bucket.csv","w+") as var_bucket:
                #     var_bucket_writer = csv.writer(var_bucket, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                #     var_bucket_writer.writerow([self.filtered_sentence[2]])
                
                var_index = self.filtered_sentence.index("variable")+1
                current_variable = self.filtered_sentence[var_index]

            '''
                Return the command and variable
            '''
            # print(self.filtered_sentence)
            command = [w for w in self.filtered_sentence if not w in self.stop_words and w != current_variable]
            return command_type,command,{"variable_name":current_variable}


        elif command_type == 'insert':
            
            # TODO: Identify the position of 'variable' and find the variable for Multiple variables
            # TODO: Use KEYWORDS instead of "variable"
            if "variable" in self.filtered_sentence:
                var_index = self.filtered_sentence.index("variable")+1
                
                if var_index >= len(self.filtered_sentence):
                    return command_type, self.filtered_sentence, None
                
                current_variable = self.filtered_sentence[var_index]
                
                '''Create the command list'''
                for i,token in enumerate(self.filtered_sentence):
                    if i != var_index:
                        command.append(token)
                
                d = dict()
                d["sticker_type"] = "variable"
                d["sticker_value"] = current_variable

                return command_type,command,d

            if "text" in self.filtered_sentence:
                # TODO: Fix the stopwords issue: Stopwords should'nt be removed from the text
                
                '''Append commands to the command list'''
                for i,token in enumerate(self.filtered_sentence):
                    print_index = self.filtered_sentence.index("text")
                    if i <= print_index:
                        command.append(token)

                '''Append text to the text list'''
                text_string = ""
                for i,token in enumerate(self.filtered_sentence):
                    if i > print_index:
                        text_string += (str(token)+str(" "))

                '''Create the dictionary'''
                d = dict()
                d["sticker_type"] = "text"
                d["sticker_value"] = text_string

                return command_type,command,d
            
            else:
                return command_type, self.filtered_sentence, None

        
        elif command_type == 'delete':
            pass


        elif command_type == 'navigate':
            
            d = {}

            if self.filtered_sentence[0] == "end":
                command = "POP_PARENT"

            
            elif self.filtered_sentence[0] == "go":

                for index in range(len(self.filtered_sentence)):
                    if self.filtered_sentence[index] == "number":
                        index+=1
                        if index < len(self.filtered_sentence):
                            command = "GOTO"
                            num = int(self.filtered_sentence[index])
                            d = {"card_number": num}
                            break
            
            return command_type, command, d


        else:
            print("Unknown")
            return None