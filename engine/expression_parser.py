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

        '''A dictionary to map operators'''
        # TODO: Create a extensive dictionary of operators
        operators = {
            "plus" : "+",
            "minus" : "-",
            "into" : "*",
            "divided" : "/",
            "less" : "<",
            "greater" : ">",
            "equal" : "==",
        }

        '''Remove Stopwords'''
        stop_words = set(stopwords.words('english'))
        # TODO: Find a proper list of stopwords
        stop_words.remove("for")
        stop_words.remove("if")
        stop_words.remove("not")
        stop_words.remove("to")
        filtered_exp = [w for w in expression if not w in stop_words]
        print(filtered_exp)

        if "variable" in filtered_exp:
            var_index = filtered_exp.index("variable")+1
            # TODO: Check if the variable is present in the variable bucket
            with open("variable_bucket.csv","r") as f:
                rows = csv.reader(f)
                flag = 0
                for row in rows:
                    if filtered_exp[var_index] == row[0]:
                        flag = 1
                if flag == 0:
                    print("The variable has not yet been defined")
                    # TODO: Ask the user to create a variable
            expression_tuples.append(("variable",filtered_exp[var_index]))

        for idx,w in enumerate(filtered_exp):
            if w in operators:
                expression_tuples.append(("operator",operators[w]))

        if "number" in filtered_exp:
            num_index = filtered_exp.index("number")+1
            expression_tuples.append(("number",filtered_exp[num_index]))

        return expression_tuples
