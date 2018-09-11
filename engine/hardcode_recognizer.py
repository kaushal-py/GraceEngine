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
        ASSIGN = ["equals", "equal", "set", "=", "assign"]


        # Convert the string to lowercase.
        data_string = data_string.lower()
        # Split the string into words.
        datalist = list(data_string.split())

        output_string = ''
        

        ########## Logic to handle print statements #############
        if self._has(datalist, PRINT):
            
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
        


        ############## Logic to handle assignment operations ###############
        elif self._has(datalist, ASSIGN):
            
            if datalist[0] in ["assign", "set"]:
                
                temp_command = datalist[0]
                del datalist[0]

                in_string = ' '.join(datalist)
                [variable, expression] = list(in_string.split(" to "))
                
                if temp_command == "assign":
                    variable, expression = expression, variable
                            
            else:
                variable = datalist[0]
                del datalist[0]
                del datalist[1]

                expression = ' '.join(datalist)

            output_string = variable + " = " + self._eval_expression(expression)
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
    

    def _has(self, listA, listB):
        
        for element in listA:
            if element in listB:
                return True
        return False
    
    def _eval_expression(self, expression):
        
        if self._isnumber(expression):
            return expression
        elif expression in self.identifiers:
            return expression
        else:
            return '\"' + expression + '\"'