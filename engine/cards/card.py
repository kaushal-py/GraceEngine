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

        ''' Each card has a type as mentioned above'''
        self.card_type = card_type

        ''' This is a unique card number which will be displayed to the user to access the cards'''
        self.card_number = card_number

        ''' This is a dictionary of card object which is to be sent to the UI as json '''
        self.card_dict = {}

        ''' A card may or may not have external dependants '''
        self.external_dependant = None

        ''' A card may or may not have internal dependants'''
        self.internal_dependants = []

        ''' A card may or may not have children '''
        self.children = []

        ''' Each card has a valid line(s) of code which is stored in this variable '''
        self.code = ""

        '''
        More information on card and its attributes can be found in the documention at TODO : idhar documentation ka link ayega
        '''

    ''' 
    Each card has a generate_code() method 
    which generates the code for that card 
    and stores it the code variable of that card 
    '''
    def generate_code(self):
        # Every card type has to implement this method
        raise NotImplementedError
    
    '''
    Each card has a generate_card() method 
    which generates the dictionary to be sent to UI for that card 
    and stores it the card_dict variable of that card 
    '''
    def generate_card(self):
        # Every card type has to implement this method
        raise NotImplementedError
    
    def add_child(self, card):
        # if this method is not found in inherited classes, then this is used as the default implementation
        self.children.append(card)