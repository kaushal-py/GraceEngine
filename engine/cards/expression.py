from card import Card

class Expression(Card):

    ''' This is will be the list of variables, numbers, operators '''
    expression = []
    def __init__(self, expression:str):
        expression = expression.split()
        for item in expression:
            try:
                num = int(item)
                #TODO: This should be sticker, but sticker outside bana hai na 
                self.expression.append(num)
            except:
                self.expression.append(item)
        card_id = "expression"
        card_type=[True,True,True,False,0,False] #TODO: DO THIS
        super(Expression,self).__init__(card_id, card_type)
    
if __name__ == "__main__":
    expr = Expression("5 + 4")
    for item in expr.expression:
        print(item,type(item))

