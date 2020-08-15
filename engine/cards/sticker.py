class Sticker():

    def __init__(self,sticker_type:str, sticker_value):
        self.sticker_id = 0#TODO: get id from somewhere which increments after card creation
        
        '''
        Sticker Types:
            variable
            number
            conditional_operator
            operator
            # TODO: add this
        
        Sticker has above set of defined types
        '''
        self.sticker_type = sticker_type

        '''
        Sticker value is the original value to be stored
        eg.
            if sticker_type is operator the sticker_value is the actual operator ('+' or '-' or '*' or '/')
            if sticker_type is variable then sticker_value is "variable name" (NOTE: not variable value)
        '''
        self.sticker_value = sticker_value