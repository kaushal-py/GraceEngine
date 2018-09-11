'''
A natural language recognizer which has a fixed set of rules to handle the text.
This approach mainly acts as a baseline for comparison, or a prototype for the entire idea.
'''

class HardCodeRecognizer:

    '''
    Initialise all data structures.
    identifiers - A list to store the history of variables that the program has seen.
    '''
    def __init__(self):

        # a list for storing the list of variables that have already been defined
        # in the program.
        self.identifiers = [""]
    
    
    '''
    Take an input string in raw English, and convert
    it into corresponding python code by a if/else logic.
    '''
    def recognize(self, data_string):

        # Intents
        PRINT = ["print", "display", "show"]

        # Convert the string to lowercase.
        data_string = data_string.lower()
        # Split the string into words.
        datalist = list(data_string.split())

        output_string = ''
        
        ## Logic to handle print statements
        if datalist[0] in PRINT:
            del datalist[0]

            # if user explicitly specifies to print string
            if datalist[0] == "string":    
                del datalist[0]
                output_string = ' '.join(datalist)
                output_string = "print(\""+output_string+"\")"
            
            # Else Identify what to print
            else:
                # check if user has used conjunctions
                if "and" in datalist:
                    in_string = ' '.join(datalist)
                    individual_tokens = list(in_string.split(" and "))

                    for token in individual_tokens:
                        
                        # Identify if it is an identifier or a string
                        if token in self.identifiers:
                            output_string += token+", "
                        else:
                            output_string += '\"'+token+"\", "
                    
                    output_string = "print("+output_string+")"
                
                else:
                    output_string = ' '.join(datalist)
                    if datalist[0] in self.identifiers:
                        output_string = "print("+output_string+")"
                    else:
                        output_string = "print(\""+output_string+"\")"
        ## end print logic
        
        # Logic to handle assignment operations
        elif datalist[0] in ["assign", "set"] or "=" in datalist:

            if datalist[0] in ["assign", "set"]:
                del datalist[0]
                del datalist[1]
            else:
                del datalist[1]
            
            output_string = datalist[0]+" = "

            # check if it is a number
            if self._isnumber(datalist[1]):
                output_string += datalist[1]
            # check if it is an identifier
            elif datalist[1] in self.identifiers:
                output_string += datalist[1]
            # it is a string
            else:
                output_string += '\"'+datalist[1]+'\"' 
            
            self.identifiers.append(datalist[0])
        ## end assignment logic
           
        return output_string
    

    '''
    Helper method:
    Check if a given word is a number or not.
    The number can be int, long, float or complex.
    Return true if a number.
    '''
    def _isnumber(self, s):
        try:
            complex(s) # for int, long, float and complex
        except ValueError:
            return False

        return True