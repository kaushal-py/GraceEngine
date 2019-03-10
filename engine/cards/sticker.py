class Sticker():

    def __init__(self,sticker_type:str, sticker_value):
        self.sticker_id = 0#TODO: get id from somewhere which increments after card creation
        
        '''
        Sticker Types:
            Variable
            Number
            Conditional operator

        Sticker has set of defined types(variable,value,etc.) from which 1 can be selected
        TODO: write this comment well also explain sticker_value
        '''

        self.sticker_type = sticker_type
        self.sticker_value = sticker_value