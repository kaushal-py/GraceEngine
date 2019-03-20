class Card():
    
    def __init__(self,card_id:str, card_type:list, card_number:int):
        
        '''
        Each card has a ID and a Type.
        ID is unique number for each card.

        == Card types ==
        1. Top Tape - TT
        2. Bottom Tape - BT        
        3. Left Punch - LP
        4. Right Punch - RP
        5. Left Hole - LH    
        6. Right Hole- RH    
        7. Left Inner Punch (along with count) - nLIP    

        The type of card is stored as a list of 5 boolean values and 1 integer value as given below
        -> [Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Integer]
        The values in the list depend on whether or not the card has that type
        A card can be any combination of these types.
        Suppose a card has multiple types, it can be specified by using '-'.
        
        For example: 
        [True,True, False, False, False, True, 0]
        
        The order of the types is specified using the priority specified in the above list.
        '''
        
        ''' This is to identify the card '''
        self.card_id = card_id
        self.card_type = card_type

        ''' This is a card number which will be displayed to the user '''
        self.card_number = card_number
        self.card_dict = {}
    

    def get_internal_dependants(self):
        return []
    
    def get_external_dependant(self):
        return None
    
    def get_children(self):
        return []