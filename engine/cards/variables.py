from card import Card

class Variable_Setter(Card):

    '''
    A card that allows user to set a value to a variable
    '''

    def __init__(self, variable_name):
        
        self.id="Variable_Setter"
        self.ctype="TT-BT-RP"
        super().__init__(self.id, self.ctype)

        self.stickers["variable_name"] = variable_name
    
        self.card_links["TT"] = None
        self.card_links["BT"] = None
        self.card_links["RP"] = None



class Variable_Getter(Card):

    '''
    A card that allows user to get the value of a variable
    '''
    
    def __init__(self, variable_name):

        self.id="Variable_Getter"
        self.type="LP"
        super().__init__(self.id, self.ctype)

        self.stickers["variable_name"] = variable_name

        self.card_links["LP"] = None






if __name__ == "__main__":
    v = Variable_Setter("count")
    assert isinstance(v, Card)