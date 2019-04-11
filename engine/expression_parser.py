import spacy
import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
import csv

class ExpressionParser:

    def __init__(self):
        
        pass

    def parseExpression(self,expression):
        
        '''Create the list of tuples'''
        expression_tuples = []
        expression_tuples.append([])

        '''A dictionary to map operators'''
        # TODO: Create a extensive dictionary of operators
        operators = {
            "+": "+",
            "plus" : "+",
            "minus" : "-",
            "into" : "*",
            "times" : "*",
            "divided" : "/",
            "remainder" : "%",
        }

        conditional_operators = {
            "less" : "<",
            "greater" : ">",
            "equals" : "==",
        }

        logical_operators = {
            "and": "and",
            "or": "or",
            "not": "not"
        }

        '''Remove Stopwords'''
        stop_words = set(stopwords.words('english'))
        # TODO: Find a proper list of stopwords
        stop_words.remove("for")
        stop_words.remove("if")
        stop_words.remove("not")
        stop_words.remove("to")
        stop_words.remove("into")
        filtered_exp = [w for w in expression if not w in stop_words]
        # print(filtered_exp)

        if filtered_exp[-1] == "done":

            for index in range(len(filtered_exp)):
                
                if filtered_exp[index] == "variable":
                    index += 1

                    # TODO: Check if the variable is present in the variable bucket


                    ## DEPRECATED : Use of CSV for storing variables
                    # with open("variable_bucket.csv","r") as f:
                    #     rows = csv.reader(f)
                    #     flag = 0
                    #     for row in rows:
                    #         if filtered_exp[var_index] == row[0]:
                    #             flag = 1
                    #     if flag == 0:
                    #         print("The variable has not yet been defined")
                    #         # TODO: Ask the user to create a variable
                    if index  <= len(filtered_exp):
                        expression_tuples[-1].append(("variable",filtered_exp[index]))

                if filtered_exp[index] in operators:
                    expression_tuples[-1].append(("operator",operators[filtered_exp[index]]))
                
                if filtered_exp[index] in conditional_operators:
                    expression_tuples.append(("condition",conditional_operators[filtered_exp[index]]))
                    expression_tuples.append([])
                
                if filtered_exp[index] in logical_operators:
                    # TODO: Nothing done for logical expressions
                    expression_tuples.append(("logic",logical_operators[filtered_exp[index]]))
                
                if filtered_exp[index] == "number":
                    index += 1
                    if index  <= len(filtered_exp):
                        expression_tuples[-1].append(("number",filtered_exp[index]))


            # print(expression_tuples)
            return (expression_tuples, True)
    
        else:
            return (None, False)
        
