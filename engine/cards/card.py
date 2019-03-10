class Card():
    
    def __init__(self,card_id:str, card_type:list):
        
        '''
        Each card has a ID and a Type.
        ID is unique number for each card.

        == Card types ==
        1. Top Tape - TT
        2. Bottom Tape - BT
        3. Right Punch - RP
        4. Left Punch - LP
        5. Left Inner Punch (along with count) - nLIP
        6. Nested Tape - NT

        The type of card is stored as a list of 5 boolean values and 1 integer value as given below
        -> [Boolean, Boolean, Boolean, Boolean, Integer, Boolean]
        The values in the list depend on whether or not the card has that type
        A card can be any combination of these types.
        Suppose a card has multiple types, it can be specified by using '-'.
        For example: 
        If the card has a top and a bottom tape and a right punch and 3 Left inner punches,
        the type of the card will be "[True,True,True,False,3,False]".
        
        The order of the types is specified using the priority specified in the above list.
        '''
        
        ''' This is to identify the card '''
        self.card_id = card_id
        self.card_type = card_type

        ''' This is a card number which will be displayed to the user '''
        self.card_number = 0 # TODO: mechanism for card number